from __future__ import annotations

import difflib
import subprocess
import time
from pathlib import Path
from typing import Dict, Iterable, List

from llvmlite import binding

from binary_generator import generar_binario_linux, generar_binarios_desde_ir
from optimizer import contar_instrucciones_ir


PASSES_DISPONIBLES = (
    "mem2reg",
    "instcombine",
    "simplifycfg",
    "dce",
    "inline",
    "loop-unroll",
)


def _init_llvm():
    binding.initialize_all_targets()
    binding.initialize_all_asmprinters()


def _normalizar_passes(passes: Iterable[str]) -> List[str]:
    normalizados: List[str] = []
    for p in passes:
        pnorm = p.strip().lower()
        if not pnorm:
            continue
        normalizados.append(pnorm)
    return normalizados


def _agregar_pass(mpm, pass_name: str):
    if pass_name == "mem2reg":
        mpm.add_sroa_pass()
        return
    if pass_name == "instcombine":
        mpm.add_instruction_combine_pass()
        return
    if pass_name == "simplifycfg":
        mpm.add_simplify_cfg_pass()
        return
    if pass_name == "dce":
        mpm.add_dead_code_elimination_pass()
        return
    if pass_name == "inline":
        mpm.add_partial_inliner_pass()
        return
    if pass_name == "loop-unroll":
        mpm.add_loop_unroll_pass()
        return
    raise ValueError(f"Pass no soportado: {pass_name}")


def construir_diff_paralelo(ir_antes: str, ir_despues: str) -> Dict[str, object]:
    antes = ir_antes.splitlines()
    despues = ir_despues.splitlines()
    matcher = difflib.SequenceMatcher(a=antes, b=despues)

    filas: List[Dict[str, object]] = []
    resumen = {"iguales": 0, "modificadas": 0, "agregadas": 0, "eliminadas": 0}

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            for off in range(i2 - i1):
                filas.append(
                    {
                        "estado": "igual",
                        "antes_num": i1 + off + 1,
                        "antes_texto": antes[i1 + off],
                        "despues_num": j1 + off + 1,
                        "despues_texto": despues[j1 + off],
                    }
                )
                resumen["iguales"] += 1
            continue

        if tag == "replace":
            span = max(i2 - i1, j2 - j1)
            for off in range(span):
                ai = i1 + off
                bj = j1 + off
                hay_antes = ai < i2
                hay_despues = bj < j2

                if hay_antes and hay_despues:
                    estado = "modificada"
                    resumen["modificadas"] += 1
                elif hay_antes:
                    estado = "eliminada"
                    resumen["eliminadas"] += 1
                else:
                    estado = "agregada"
                    resumen["agregadas"] += 1

                filas.append(
                    {
                        "estado": estado,
                        "antes_num": (ai + 1) if hay_antes else None,
                        "antes_texto": antes[ai] if hay_antes else "",
                        "despues_num": (bj + 1) if hay_despues else None,
                        "despues_texto": despues[bj] if hay_despues else "",
                    }
                )
            continue

        if tag == "delete":
            for ai in range(i1, i2):
                filas.append(
                    {
                        "estado": "eliminada",
                        "antes_num": ai + 1,
                        "antes_texto": antes[ai],
                        "despues_num": None,
                        "despues_texto": "",
                    }
                )
                resumen["eliminadas"] += 1
            continue

        if tag == "insert":
            for bj in range(j1, j2):
                filas.append(
                    {
                        "estado": "agregada",
                        "antes_num": None,
                        "antes_texto": "",
                        "despues_num": bj + 1,
                        "despues_texto": despues[bj],
                    }
                )
                resumen["agregadas"] += 1

    return {"filas": filas, "resumen": resumen}


def optimizar_ir_manual_texto(ir_texto: str, passes: Iterable[str]) -> Dict[str, object]:
    _init_llvm()

    passes_sel = _normalizar_passes(passes)
    if not passes_sel:
        raise ValueError("Debes seleccionar al menos un pass.")

    no_soportados = [p for p in passes_sel if p not in PASSES_DISPONIBLES]
    if no_soportados:
        raise ValueError(f"Passes no soportados: {', '.join(no_soportados)}")

    modulo = binding.parse_assembly(ir_texto)
    modulo.verify()

    ir_antes = str(modulo)
    inst_antes = contar_instrucciones_ir(ir_antes)

    triple = modulo.triple or binding.get_default_triple()
    target = binding.Target.from_triple(triple)
    tm = target.create_target_machine(opt=2)
    pto = binding.create_pipeline_tuning_options(speed_level=2, size_level=0)
    pb = binding.create_pass_builder(tm, pto)
    mpm = binding.create_new_module_pass_manager()

    for pass_name in passes_sel:
        _agregar_pass(mpm, pass_name)

    inicio_opt = time.perf_counter()
    pb.start_pass_timing()
    mpm.run(modulo, pb)
    reporte_tiempos = pb.finish_pass_timing()
    fin_opt = time.perf_counter()

    modulo.verify()
    ir_despues = str(modulo)
    inst_despues = contar_instrucciones_ir(ir_despues)

    reduccion = inst_antes - inst_despues
    porcentaje = (reduccion / inst_antes * 100.0) if inst_antes else 0.0

    diff = list(
        difflib.unified_diff(
            ir_antes.splitlines(),
            ir_despues.splitlines(),
            fromfile="ir_original.ll",
            tofile="ir_manual.ll",
            lineterm="",
        )
    )
    diff_texto = "\n".join(diff) if diff else "(Sin cambios en IR)"
    diff_paralelo = construir_diff_paralelo(ir_antes, ir_despues)

    return {
        "passes_aplicados": passes_sel,
        "triple": triple,
        "ir_antes": ir_antes,
        "ir_despues": ir_despues,
        "diff": diff_texto,
        "diff_paralelo": diff_paralelo,
        "instrucciones_antes": inst_antes,
        "instrucciones_despues": inst_despues,
        "reduccion_absoluta": reduccion,
        "reduccion_porcentaje": porcentaje,
        "reporte_tiempos": reporte_tiempos,
        "tiempo_optimizacion_seg": fin_opt - inicio_opt,
    }


def optimizar_ir_manual_archivo(
    ruta_ir_entrada: str,
    ruta_ir_salida: str,
    passes: Iterable[str],
) -> Dict[str, object]:
    entrada = Path(ruta_ir_entrada)
    salida = Path(ruta_ir_salida)

    if not entrada.exists():
        raise FileNotFoundError(f"No existe IR de entrada: {entrada}")

    ir_texto = entrada.read_text(encoding="utf-8")
    resultado = optimizar_ir_manual_texto(ir_texto, passes)
    salida.write_text(resultado["ir_despues"], encoding="utf-8")

    resultado["ruta_ir_entrada"] = str(entrada)
    resultado["ruta_ir_salida"] = str(salida)
    return resultado


def ejecutar_ir_manual_linux(ruta_ir: str, base_salida: str | None = None) -> Dict[str, object]:
    ruta = Path(ruta_ir)
    if not ruta.exists():
        raise FileNotFoundError(f"No existe IR para ejecutar: {ruta}")

    base = base_salida or str(ruta.with_suffix(""))
    inicio_total = time.perf_counter()
    inicio_comp = time.perf_counter()
    compilacion = generar_binario_linux(str(ruta), base)
    fin_comp = time.perf_counter()
    if not compilacion.get("ok"):
        return {
            "ok": False,
            "fase": "compilacion",
            "tiempo_compilacion_seg": fin_comp - inicio_comp,
            "tiempo_total_seg": time.perf_counter() - inicio_total,
            **compilacion,
        }

    binario = compilacion.get("binary_path")
    inicio_ejec = time.perf_counter()
    proc = subprocess.run([binario], capture_output=True, text=True)
    fin_ejec = time.perf_counter()
    fin_total = time.perf_counter()

    return {
        "ok": proc.returncode == 0,
        "fase": "ejecucion",
        "returncode": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
        "binary_path": binario,
        "object_path": compilacion.get("object_path"),
        "link_cmd": compilacion.get("link_cmd"),
        "tiempo_compilacion_seg": fin_comp - inicio_comp,
        "tiempo_ejecucion_seg": fin_ejec - inicio_ejec,
        "tiempo_total_seg": fin_total - inicio_total,
    }


def ejecutar_ir_manual_targets(
    ruta_ir: str,
    base_salida: str | None = None,
    targets: Iterable[str] = ("linux", "windows"),
) -> Dict[str, object]:
    ruta = Path(ruta_ir)
    if not ruta.exists():
        raise FileNotFoundError(f"No existe IR para ejecutar: {ruta}")

    base = base_salida or str(ruta.with_suffix(""))
    targets_sel = [t.strip().lower() for t in targets if str(t).strip()]
    if not targets_sel:
        raise ValueError("Debes seleccionar al menos un target.")

    compilacion = generar_binarios_desde_ir(str(ruta), base, targets=tuple(targets_sel))
    resultados: Dict[str, object] = {"ok": True, "targets": {}}

    for target in targets_sel:
        info = compilacion.get(target, {"ok": False, "error": "Target sin resultado."})
        target_result = {
            "ok": bool(info.get("ok")),
            "binary_path": info.get("binary_path"),
            "object_path": info.get("object_path"),
            "error": info.get("error"),
            "stderr": info.get("stderr", ""),
            "stdout": info.get("stdout", ""),
            "tiempo_objeto_ms": info.get("tiempo_objeto_ms", 0.0),
            "tiempo_enlazado_ms": info.get("tiempo_enlazado_ms", 0.0),
            "tiempo_total_generacion_ms": info.get("tiempo_total_generacion_ms", 0.0),
        }

        if target == "linux" and target_result["ok"]:
            inicio_run = time.perf_counter()
            proc = subprocess.run([target_result["binary_path"]], capture_output=True, text=True)
            fin_run = time.perf_counter()
            target_result["run_ok"] = proc.returncode == 0
            target_result["run_returncode"] = proc.returncode
            target_result["run_stdout"] = proc.stdout
            target_result["run_stderr"] = proc.stderr
            target_result["tiempo_ejecucion_ms"] = (fin_run - inicio_run) * 1000.0
            if not target_result["run_ok"]:
                resultados["ok"] = False
        elif target == "windows" and target_result["ok"]:
            target_result["run_ok"] = None
            target_result["run_note"] = (
                "Ejecución omitida en entorno Linux/WSL; validar .exe en Windows real."
            )

        if not target_result["ok"]:
            resultados["ok"] = False

        resultados["targets"][target] = target_result

    return resultados


def exportar_ir_manual(ruta_ir_actual: str, ruta_destino: str | None = None) -> str:
    origen = Path(ruta_ir_actual)
    if not origen.exists():
        raise FileNotFoundError(f"No existe IR manual para exportar: {origen}")

    if ruta_destino:
        destino = Path(ruta_destino)
    else:
        destino = origen.with_suffix(".export.ll")
        contador = 1
        while destino.exists():
            destino = origen.with_suffix(f".export.{contador}.ll")
            contador += 1

    destino.write_text(origen.read_text(encoding="utf-8"), encoding="utf-8")
    return str(destino)
