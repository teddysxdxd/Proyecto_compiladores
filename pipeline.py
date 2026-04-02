import sys
import subprocess
from antlr4 import *
from antlr4.tree.Trees import Trees
from CalculadoraLexer import CalculadoraLexer
from CalculadoraParser import CalculadoraParser
from custom_errors import MyErrorListener, LexerErrorListener
from semantic_visitor import SemanticVisitor
from interpreter_visitor import InterpreterVisitor


def run_pipeline(archivo_entrada):
    print(f"--- Iniciando Pipeline para: {archivo_entrada} ---")
    
    try:
        # 1. Fase Léxica
        input_stream = FileStream(archivo_entrada, encoding='utf-8')
        lexer = CalculadoraLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(LexerErrorListener()) # Detiene si hay símbolos inválidos
        
        # 2. Fase Sintáctica
        stream = CommonTokenStream(lexer)
        parser = CalculadoraParser(stream)
        parser.removeErrorListeners()
        error_sintactico = MyErrorListener()
        parser.addErrorListener(error_sintactico)
        
        tree = parser.archivo()
        
        # Condición de parada: Errores Sintácticos
        if error_sintactico.errors:
            print("\n[STOP] Errores Sintácticos detectados. Pipeline detenido.")
            return       

        # 3. Fase Semántica (Type Checking)
        print("\nIniciando análisis semántico...")
        semantic = SemanticVisitor()
        semantic.visit(tree)
        
        # Condición de parada: Errores Semánticos (tipos, variables no declaradas)
        if semantic.errors:
            print("\n--- ERRORES SEMÁNTICOS ---")
            for err in semantic.errors:
                print(err)
            print("\n[STOP] Fallo en validación lógica. Pipeline detenido.")
            return

        # 4. Fase de Intérprete (Ejecución real)
        print("\nAnálisis exitoso. Iniciando ejecución...")
        print("-" * 30)
        interpreter = InterpreterVisitor()
        interpreter.visit(tree)
        print("-" * 30)
        print("Programa finalizado con éxito.")
        # 5. Fase de Intérprete (Ejecución real)
        subprocess.run(["python3", "compiler.py"], check=True)

    except Exception as e:
        if "Fallo en Fase Léxica" in str(e):
            print("\n[STOP] Pipeline detenido por error léxico.")
        else:
            print(f"\n[ERROR CRÍTICO]: {e}")

if __name__ == '__main__':
    # El archivo de entrada por defecto
    run_pipeline('operaciones.txt')