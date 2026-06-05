from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List

from llvmlite import binding


def _init_llvm():
    binding.initialize_all_targets()
    binding.initialize_all_asmprinters()


def contar_instrucciones_ir(ir_texto: str) -> int:
    total = 0
    for linea in ir_texto.splitlines():
        s = linea.strip()
        if not s:
            continue
        if s.startswith(";"):
            continue
        if s in {"{", "}"}:
            continue
        if s.endswith(":"):
            continue
        if s.startswith("target ") or s.startswith("source_filename"):
            continue
        if s.startswith("define ") or s.startswith("declare "):
            continue
        if s.startswith("attributes "):
            continue
        if s.startswith("!") and " = " in s:
            continue
        if " = type " in s:
            continue
        if s.startswith("@") and " = " in s:
            continue
        total += 1
    return total


def _extraer_pases_relevantes(reporte_tiempos: str) -> List[str]:
    pases = []
    vistos = set()
    for linea in reporte_tiempos.splitlines():
        linea = linea.rstrip()
        m = re.search(r"\)\s+([A-Za-z0-9_.:-]+Pass)$", linea)
        if not m:
            continue
        nombre = m.group(1)
        if nombre in vistos:
            continue
        vistos.add(nombre)
        pases.append(nombre)
    return pases


def optimizar_ir_texto_o3(ir_texto: str) -> Dict[str, object]:
    _init_llvm()

    modulo = binding.parse_assembly(ir_texto)
    modulo.verify()

    ir_antes = str(modulo)
    inst_antes = contar_instrucciones_ir(ir_antes)

    triple = modulo.triple or binding.get_default_triple()
    target = binding.Target.from_triple(triple)
    tm = target.create_target_machine(opt=3)

    pto = binding.create_pipeline_tuning_options(speed_level=3, size_level=0)
    pb = binding.create_pass_builder(tm, pto)
    mpm = pb.getModulePassManager()

    pb.start_pass_timing()
    mpm.run(modulo, pb)
    reporte_tiempos = pb.finish_pass_timing()

    modulo.verify()
    ir_despues = str(modulo)
    inst_despues = contar_instrucciones_ir(ir_despues)

    reduccion = inst_antes - inst_despues
    porcentaje = (reduccion / inst_antes * 100.0) if inst_antes else 0.0
    pases = _extraer_pases_relevantes(reporte_tiempos)

    return {
        "ir_optimizado": ir_despues,
        "instrucciones_antes": inst_antes,
        "instrucciones_despues": inst_despues,
        "reduccion_absoluta": reduccion,
        "reduccion_porcentaje": porcentaje,
        "pases_detectados": pases,
        "reporte_tiempos": reporte_tiempos,
    }


def optimizar_ir_archivo_o3(ruta_ir_entrada: str, ruta_ir_salida: str) -> Dict[str, object]:
    entrada = Path(ruta_ir_entrada)
    salida = Path(ruta_ir_salida)

    ir_texto = entrada.read_text(encoding="utf-8")
    resultado = optimizar_ir_texto_o3(ir_texto)
    salida.write_text(resultado["ir_optimizado"], encoding="utf-8")

    resultado["ruta_ir_entrada"] = str(entrada)
    resultado["ruta_ir_salida"] = str(salida)
    return resultado
