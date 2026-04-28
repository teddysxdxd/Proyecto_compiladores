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
from tkinter import Tk
from tkinter.filedialog import askopenfilename


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


def run_pipeline(archivo_entrada):
    metricas = {}

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

        # 4. Fase de Intérprete
        with medir_fase("Fase de Intérprete", metricas):
            print("\nAnálisis exitoso. Iniciando ejecución...")
            print("-" * 30)

            interpreter = InterpreterVisitor()
            interpreter.visit(tree)

            print("-" * 30)
            print("Programa finalizado con éxito.")

        # 5. Fase de Compilación / Ejecución externa
        with medir_fase("Fase Compiler.py", metricas):
            subprocess.run(
                ["python3", "compiler.py", archivo_entrada],
                check=True
            )

        imprimir_resumen(metricas)

    except Exception as e:
        if "Fallo en Fase Léxica" in str(e):
            print("\n[STOP] Pipeline detenido por error léxico.")
        else:
            print(f"\n[ERROR CRÍTICO]: {e}")

        imprimir_resumen(metricas)


def seleccionar_archivo():
    root = Tk()
    root.withdraw()  # Oculta la ventana principal

    archivo = askopenfilename(
        title="Selecciona un archivo TXT",
        initialdir=os.getcwd(),  # raíz del proyecto
        filetypes=[("Archivos de texto", "*.txt")]
    )

    return archivo


if __name__ == '__main__':
    archivo = seleccionar_archivo()

    if archivo:
        run_pipeline(archivo)
    else:
        print("No se seleccionó ningún archivo.")