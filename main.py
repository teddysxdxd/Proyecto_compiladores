import sys
import subprocess
from antlr4 import *
from CalculadoraLexer import CalculadoraLexer
from CalculadoraParser import CalculadoraParser
from CalculadoraVisitor import CalculadoraVisitor
from antlr4.tree.Trees import Trees

class EvaluarVisitante(CalculadoraVisitor):
    # --- Estructura del Programa ---
    def visitInstruccionExpresion(self, ctx):
        resultado = self.visit(ctx.expresion())
        
        # Si el resultado existe, lo imprimimos automáticamente
        if resultado is not None:
            if isinstance(resultado, (int, float)):
                if resultado == 1: print("Resultado: verdadero")
                elif resultado == 0: print("Resultado: falso")
                else: print(f"Resultado: {resultado}")
            else:
                print(f"Resultado: {resultado}")
        return resultado
    def visitPrintStmt(self, ctx):
        resultado = self.visit(ctx.expresion())
        if resultado is not None:
            # Imprimimos formateado: si es 1/0, verdadero/falso; si es texto o número, el valor directo
            if isinstance(resultado, (int, float)):
                if resultado == 1: print("verdadero")
                elif resultado == 0: print("falso")
                else: print(resultado)
            else:
                print(resultado)
        return None

    def visitInstruccionIf(self, ctx):
        return self.visit(ctx.ifStatement())

    def visitInstruccionBloque(self, ctx):
        return self.visit(ctx.block())

    # --- Bloques y Control de Flujo ---
    def visitBlock(self, ctx):
        resultado = None
        # Recorre cada instrucción dentro de las llaves
        for inst in ctx.instruccion():
            resultado = self.visit(inst)
        return resultado

    def visitIfStatement(self, ctx):
        condicion = self.visit(ctx.expresion())
        # Si la condición (expresion) es 1 (verdadero)
        if condicion is not None and float(condicion) == 1:
            return self.visit(ctx.block(0))
        # Si existe el bloque 'sinel' (índice 1)
        else_block = ctx.block(1)
        if else_block:
            return self.visit(else_block)
        return None

    # --- Aritmética y Lógica ---
    def visitMultiplicacionDivisision(self, ctx):
        izq = self.visit(ctx.expresion(0))
        der = self.visit(ctx.expresion(1))
        if izq is None or der is None: return 0
        if ctx.op.text == '*': return izq * der
        return izq / der if der != 0 else 0

    def visitSumaResta(self, ctx):
        izq = self.visit(ctx.expresion(0))
        der = self.visit(ctx.expresion(1))
        if izq is None or der is None: return 0
        if ctx.op.text == '+': return izq + der
        return izq - der

    def visitRelacional(self, ctx):
        izq = self.visit(ctx.expresion(0))
        der = self.visit(ctx.expresion(1))

        if izq is None or der is None: return 0
        
        val_izq = float(izq)
        val_der = float(der)

        op = ctx.op.text
        if op == '==': return 1 if izq == der else 0
        if op == '!=' or op == '<>': return 1 if izq != der else 0
        if op == '<': return 1 if izq < der else 0
        if op == '>': return 1 if izq > der else 0
        if op == '<=': return 1 if izq <= der else 0
        if op == '>=': return 1 if izq >= der else 0
        return 0

    def visitNotLogico(self, ctx):
        val = self.visit(ctx.expresion())
        return 1 if val == 0 else 0

    def visitAndOrLogico(self, ctx):
        izq = self.visit(ctx.expresion(0))
        der = self.visit(ctx.expresion(1))
        op = ctx.op.text
        if op == '&&': return 1 if (izq and der) else 0
        if op == '||': return 1 if (izq or der) else 0
        return 0

    # --- Básicos ---
    def visitNumero(self, ctx):
        return float(ctx.NUMERO().getText())

    def visitCadena(self, ctx):
        texto = ctx.STRING().getText()[1:-1]
        
        # 2. Reemplazamos la secuencia literal '\n' por el carácter de salto de línea
        return texto.replace('\\n', '\n').replace('\\r', '\n')

    def visitParentesis(self, ctx):
        return self.visit(ctx.expresion())

    def __init__(self):
        # Espeacio en memoria del programa para almacenar nuestras variables
        self.memoria = {}

        #Iplementa la asignación (ID = Expresion)
    def visitAsignacion(self, ctx):
        nombre = ctx.ID().getText() # Obtiene la variable eje: X/y
        valor = self.visit(ctx.expresion()) # Verifica el valor eje: 67
        self.memoria[nombre] = valor
        return valor

        # Implementa la varible difinida
    def visitVariable(self, ctx):
        nombre = ctx.ID().getText()
        if nombre in self.memoria:
            return self.memoria[nombre]
        print(f"Error: La variable '{nombre}'no esta definida.")
        return 0
    def visitCorchetes(self, ctx):
        return self.visit(ctx.expresion())
        
def generar_dot(tree, parser):
    """Genera el contenido en formato DOT para Graphviz"""
    from antlr4.tree.Trees import Trees
    lineas = ["digraph AST {"]
    lineas.append('  node [fontname="Arial", shape=box, style=filled, fillcolor="#e1f5fe"];')
    
    def recorrer(nodo, id_padre=0, siguiente_id=1):
        texto = Trees.getNodeText(nodo, parser.ruleNames).replace('"', '\\"')
        mi_id = siguiente_id
        lineas.append(f'  n{mi_id} [label="{texto}"];')
        if id_padre != 0:
            lineas.append(f"  n{id_padre} -> n{mi_id};")
        
        nuevo_id = mi_id + 1
        for i in range(nodo.getChildCount()):
            nuevo_id = recorrer(nodo.getChild(i), mi_id, nuevo_id)
        return nuevo_id

    recorrer(tree)
    lineas.append("}")
    return "\n".join(lineas)

def guardar_ast_grafico(tree, parser, nombre_archivo="arbol_ast"):
    dot_data = generar_dot(tree, parser)
    with open(f"{nombre_archivo}.dot", "w") as f:
        f.write(dot_data)
    try:
        # Esto genera el archivo .png automáticamente
        subprocess.run(["dot", "-Tpng", f"{nombre_archivo}.dot", "-o", f"{nombre_archivo}.png"])
        print(f"\n[ÉXITO] Árbol guardado como {nombre_archivo}.png")
    except Exception as e:
        print(f"\n[ERROR] No se pudo generar la imagen: {e}")

def main():
    try:
        input_stream = FileStream('operaciones.txt' , encoding='utf-8')
        lexer = CalculadoraLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = CalculadoraParser(stream)

        tree = parser.archivo()
        guardar_ast_grafico(tree, parser)

        print("\n" + "="*30)
        print("ESTRUCTURA DEL ÁRBOL SINTÁCTICO (AST)")
        print("="*30)
        print(Trees.toStringTree(tree, parser.ruleNames, parser))
        print("="*30 + "\n")
        
        evaluador = EvaluarVisitante()
        evaluador.visit(tree)
        
    except Exception as e:
        print(f"Error en la ejecución: {e}")

if __name__ == '__main__':
    main()