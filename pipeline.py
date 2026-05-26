import sys
import subprocess
import time
import os
from contextlib import contextmanager

from antlr4 import *
from antlr4.tree.Trees import Trees
from CalculadoraLexer import CalculadoraLexer
from CalculadoraParser import CalculadoraParser
from custom_errors import MyErrorListener, LexerErrorListener
from semantic_visitor import SemanticVisitor
from interpreter_visitor import InterpreterVisitor
from tac_generator import TACGenerator
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from ir_generator import IRGenerator
from optimizer import optimizar_ir_archivo_o3
from binary_generator import generar_binarios_desde_ir


@contextmanager
def medir_fase(nombre, metricas):
    inicio = time.perf_counter()
    print(f"\n[INICIO] {nombre}")
    try:
        yield
    finally:
        fin = time.perf_counter()
        duracion = fin - inicio
        metricas[nombre] = duracion
        print(f"[FIN] {nombre} - Duración: {duracion:.6f} segundos")


def imprimir_resumen(metricas):
    print("\n" + "=" * 40)
    print("RESUMEN DE TIEMPOS DEL PIPELINE")
    print("=" * 40)

    total = sum(metricas.values())

    for fase, duracion in metricas.items():
        print(f"{fase}: {duracion:.6f} segundos")

    print("-" * 40)
    print(f"TOTAL: {total:.6f} segundos")
    print("=" * 40)


def run_pipeline(archivo_entrada, targets_fase8=("linux", "windows")):
    metricas = {}

    archivo_tac = os.path.splitext(archivo_entrada)[0] + ".tac"
    archivo_ll  = os.path.splitext(archivo_entrada)[0] + ".ll"
    archivo_opt_ll = os.path.splitext(archivo_entrada)[0] + ".opt.ll"
    base_binarios = os.path.splitext(archivo_entrada)[0]

    print(f"--- Iniciando Pipeline para: {archivo_entrada} ---")

    try:
        # 1. Fase Léxica
        with medir_fase("Fase Léxica", metricas):
            input_stream = FileStream(archivo_entrada, encoding='utf-8')
            lexer = CalculadoraLexer(input_stream)
            lexer.removeErrorListeners()
            lexer.addErrorListener(LexerErrorListener())

        # 2. Fase Sintáctica
        with medir_fase("Fase Sintáctica", metricas):
            stream = CommonTokenStream(lexer)
            parser = CalculadoraParser(stream)
            parser.removeErrorListeners()

            error_sintactico = MyErrorListener()
            parser.addErrorListener(error_sintactico)

            tree = parser.archivo()

        if error_sintactico.errors:
            print("\n[STOP] Errores Sintácticos detectados. Pipeline detenido.")
            imprimir_resumen(metricas)
            return

        # 3. Fase Semántica
        with medir_fase("Fase Semántica", metricas):
            semantic = SemanticVisitor()
            semantic.visit(tree)

        if semantic.errors:
            print("\n--- ERRORES SEMÁNTICOS ---")
            for err in semantic.errors:
                print(err)

            print("\n[STOP] Fallo en validación lógica. Pipeline detenido.")
            imprimir_resumen(metricas)
            return

        # 4. Fase TAC
        with medir_fase("Fase TAC", metricas):
            tac_gen = TACGenerator()
            tac_gen.visit(tree)
            tac_gen.save(archivo_tac)

        ir_verificado = False

        # 5. Fase LLVM IR
        with medir_fase("Fase LLVM IR", metricas):
            ir_gen = IRGenerator()
            ir_gen.visit(tree)

            if ir_gen.verify():
                ir_verificado = True
                ir_gen.save(archivo_ll)
                print(f"\n--- LLVM IR generado → {archivo_ll} ---")
                print(f"    Ejecutar con: lli {archivo_ll}")
            else:
                print("\n[ADVERTENCIA] El IR generado no pasó la verificación LLVM.")

        # 6. Intérprete
        with medir_fase("Fase de Intérprete", metricas):
            print("\nAnálisis exitoso. Iniciando ejecución...")
            print("-" * 30)

            interpreter = InterpreterVisitor()
            interpreter.visit(tree)

            print("-" * 30)
            print("Programa finalizado con éxito.")

        if not ir_verificado:
            print("\n[STOP] Fases 7 y 8 omitidas: el IR de la Fase 5 no fue verificable.")
            imprimir_resumen(metricas)
            return

        # 7. Optimización O3
        with medir_fase("Fase 7 - Optimizer O3", metricas):
            opt_result = optimizar_ir_archivo_o3(archivo_ll, archivo_opt_ll)

            print(f"[O3] IR optimizado generado → {archivo_opt_ll}")
            print(
                f"[O3] Instrucciones: {opt_result['instrucciones_antes']} -> "
                f"{opt_result['instrucciones_despues']} "
                f"(reducción {opt_result['reduccion_porcentaje']:.2f}%)"
            )

            pases = opt_result.get("pases_detectados", [])
            if pases:
                print("[O3] Pases detectados (top):")
                for p in pases[:10]:
                    print(f"      - {p}")
            else:
                print("[O3] No se detectaron pases en el reporte de timing.")

        # 8. Generación de binarios nativos
        with medir_fase("Fase 8 - Generador de Binario Nativo", metricas):
            resultados_bin = generar_binarios_desde_ir(
                archivo_opt_ll,
                base_binarios,
                targets=targets_fase8,
            )

            for target, info in resultados_bin.items():
                if info.get("ok"):
                    print(
                        f"[BIN-{target.upper()}] OK -> {info.get('binary_path')} "
                        f"(obj: {info.get('object_path')})"
                    )
                else:
                    print(f"[BIN-{target.upper()}] ERROR -> {info.get('error')}")
                    if info.get("link_cmd"):
                        print(f"    comando: {info.get('link_cmd')}")
                    if info.get("stderr"):
                        print(f"    stderr: {info.get('stderr')}")

        imprimir_resumen(metricas)

    except Exception as e:
        if "Fallo en Fase Léxica" in str(e):
            print("\n[STOP] Pipeline detenido por error léxico.")
        else:
            print(f"\n[ERROR CRÍTICO]: {e}")

        imprimir_resumen(metricas)


def seleccionar_archivo():
    root = Tk()
    root.withdraw()

    archivo = askopenfilename(
        title="Selecciona un archivo TXT",
        initialdir=os.getcwd(),
        filetypes=[("Archivos de texto", "*.txt")]
    )

    return archivo


# 🔥 STREAM (CONSOLA + INTERFAZ SIN ROMPER NADA)
def run_pipeline_stream(archivo_entrada, callback_linea=None, targets_fase8=("linux", "windows")):

    class Tee:
        def __init__(self, *streams):
            self.streams = streams

        def write(self, data):
            for s in self.streams:
                s.write(data)
            if callback_linea:
                callback_linea(data)

        def flush(self):
            for s in self.streams:
                s.flush()

    old_stdout = sys.stdout
    sys.stdout = Tee(sys.stdout)

    try:
        run_pipeline(archivo_entrada, targets_fase8=targets_fase8)
    finally:
        sys.stdout = old_stdout


if __name__ == '__main__':
    from ui_compiler import CompiladorApp
    app = CompiladorApp(seleccionar_archivo, run_pipeline_stream)
    app.run()
