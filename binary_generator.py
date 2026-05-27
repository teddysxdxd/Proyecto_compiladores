from __future__ import annotations

import shutil
import subprocess
import time
from pathlib import Path
from typing import Dict, Iterable

from llvmlite import binding


WINDOWS_TRIPLE = "x86_64-w64-windows-gnu"


def _init_llvm():
    binding.initialize_all_targets()
    binding.initialize_all_asmprinters()


def _leer_ir(ruta_ir: str) -> str:
    return Path(ruta_ir).read_text(encoding="utf-8")


def _emitir_objeto_desde_ir(ir_texto: str, triple: str, opt: int = 2) -> bytes:
    _init_llvm()
    modulo = binding.parse_assembly(ir_texto)
    modulo.triple = triple
    modulo.verify()

    target = binding.Target.from_triple(triple)
    tm = target.create_target_machine(opt=max(0, min(3, opt)))
    return tm.emit_object(modulo)


def _ejecutar_linker(cmd):
    inicio = time.perf_counter()
    proc = subprocess.run(cmd, capture_output=True, text=True)
    fin = time.perf_counter()
    return {
        "ok": proc.returncode == 0,
        "code": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip(),
        "cmd": " ".join(cmd),
        "elapsed_ms": (fin - inicio) * 1000.0,
    }


def generar_binario_linux(ruta_ir: str, base_salida: str) -> Dict[str, object]:
    inicio_total = time.perf_counter()
    ir_texto = _leer_ir(ruta_ir)
    triple_linux = binding.get_default_triple()

    ruta_obj = f"{base_salida}.linux.o"
    ruta_bin = f"{base_salida}_linux.bin"

    inicio_obj = time.perf_counter()
    obj_bytes = _emitir_objeto_desde_ir(ir_texto, triple_linux, opt=2)
    fin_obj = time.perf_counter()
    tiempo_obj_ms = (fin_obj - inicio_obj) * 1000.0
    Path(ruta_obj).write_bytes(obj_bytes)

    linker = shutil.which("gcc") or shutil.which("cc")
    if not linker:
        fin_total = time.perf_counter()
        return {
            "ok": False,
            "target": "linux",
            "error": "No se encontró gcc/cc para enlazar binario Linux.",
            "object_path": ruta_obj,
            "binary_path": ruta_bin,
            "tiempo_objeto_ms": tiempo_obj_ms,
            "tiempo_enlazado_ms": 0.0,
            "tiempo_total_generacion_ms": (fin_total - inicio_total) * 1000.0,
        }

    link_cmd = [linker, ruta_obj, "-lm", "-o", ruta_bin, "-no-pie"]
    res = _ejecutar_linker(link_cmd)
    fin_total = time.perf_counter()
    return {
        "ok": res["ok"],
        "target": "linux",
        "linker": linker,
        "object_path": ruta_obj,
        "binary_path": ruta_bin,
        "link_cmd": res["cmd"],
        "stdout": res["stdout"],
        "stderr": res["stderr"],
        "error": None if res["ok"] else "Error al enlazar binario Linux.",
        "tiempo_objeto_ms": tiempo_obj_ms,
        "tiempo_enlazado_ms": res.get("elapsed_ms", 0.0),
        "tiempo_total_generacion_ms": (fin_total - inicio_total) * 1000.0,
    }


def generar_exe_windows(ruta_ir: str, base_salida: str) -> Dict[str, object]:
    inicio_total = time.perf_counter()
    ir_texto = _leer_ir(ruta_ir)
    ruta_obj = f"{base_salida}.windows.obj"
    ruta_exe = f"{base_salida}.exe"

    inicio_obj = time.perf_counter()
    obj_bytes = _emitir_objeto_desde_ir(ir_texto, WINDOWS_TRIPLE, opt=2)
    fin_obj = time.perf_counter()
    tiempo_obj_ms = (fin_obj - inicio_obj) * 1000.0
    Path(ruta_obj).write_bytes(obj_bytes)

    # Toolchain cruzada esperada en WSL2
    mingw = shutil.which("x86_64-w64-mingw32-gcc")
    if mingw:
        cmd = [mingw, ruta_obj, "-o", ruta_exe, "-lm"]
        res = _ejecutar_linker(cmd)
        return {
            "ok": res["ok"],
            "target": "windows",
            "linker": mingw,
            "object_path": ruta_obj,
            "binary_path": ruta_exe,
            "link_cmd": res["cmd"],
            "stdout": res["stdout"],
            "stderr": res["stderr"],
            "error": None if res["ok"] else "Error al enlazar .exe con MinGW.",
            "tiempo_objeto_ms": tiempo_obj_ms,
            "tiempo_enlazado_ms": res.get("elapsed_ms", 0.0),
            "tiempo_total_generacion_ms": (time.perf_counter() - inicio_total) * 1000.0,
        }

    # Fallback opcional con clang cross si existe
    clang = shutil.which("clang")
    if clang:
        cmd = [clang, "--target=x86_64-w64-windows-gnu", ruta_obj, "-o", ruta_exe]
        res = _ejecutar_linker(cmd)
        return {
            "ok": res["ok"],
            "target": "windows",
            "linker": clang,
            "object_path": ruta_obj,
            "binary_path": ruta_exe,
            "link_cmd": res["cmd"],
            "stdout": res["stdout"],
            "stderr": res["stderr"],
            "error": None if res["ok"] else "Error al enlazar .exe con clang cross.",
            "tiempo_objeto_ms": tiempo_obj_ms,
            "tiempo_enlazado_ms": res.get("elapsed_ms", 0.0),
            "tiempo_total_generacion_ms": (time.perf_counter() - inicio_total) * 1000.0,
        }

    fin_total = time.perf_counter()
    return {
        "ok": False,
        "target": "windows",
        "object_path": ruta_obj,
        "binary_path": ruta_exe,
        "error": (
            "No se encontró toolchain de Windows (x86_64-w64-mingw32-gcc "
            "o clang con target windows-gnu)."
        ),
        "tiempo_objeto_ms": tiempo_obj_ms,
        "tiempo_enlazado_ms": 0.0,
        "tiempo_total_generacion_ms": (fin_total - inicio_total) * 1000.0,
    }


def generar_binarios_desde_ir(
    ruta_ir: str,
    base_salida: str,
    targets: Iterable[str] = ("linux", "windows"),
) -> Dict[str, Dict[str, object]]:
    resultados: Dict[str, Dict[str, object]] = {}
    for target in targets:
        t = target.lower().strip()
        if t == "linux":
            resultados["linux"] = generar_binario_linux(ruta_ir, base_salida)
        elif t == "windows":
            resultados["windows"] = generar_exe_windows(ruta_ir, base_salida)
        else:
            resultados[t] = {"ok": False, "target": t, "error": "Target no soportado."}
    return resultados
