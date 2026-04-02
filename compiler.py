import sys
import subprocess
from antlr4 import *
from CalculadoraLexer import CalculadoraLexer
from CalculadoraParser import CalculadoraParser
from CalculadoraVisitor import CalculadoraVisitor
from antlr4.tree.Trees import Trees


class EvaluarVisitante(CalculadoraVisitor):

    def __init__(self):
        self.memoria = {}
        self.funciones = {}

    # ---------------- PROGRAMA ----------------
    def visitArchivo(self, ctx):
        for inst in ctx.instruccion():
            self.visit(inst)
        return None

    # ---------------- INSTRUCCIONES ----------------
    def visitInstruccionExpresion(self, ctx):
        resultado = self.visit(ctx.expresion())
        if resultado is not None:
            print(f"Resultado: {resultado}")
        return resultado

    def visitEjecutarPrint(self, ctx):
        resultado = self.visit(ctx.expresion())
        if resultado is not None:
            if isinstance(resultado, (int, float)):
                print(resultado)
            else:
                print(resultado)
        return None

    def visitInstruccionDeclaracion(self, ctx):
        return self.visit(ctx.declaracion())

    def visitInstruccionIf(self, ctx):
        return self.visit(ctx.ifStatement())

    def visitInstruccionWhile(self, ctx):
        return self.visit(ctx.whileStatement())

    def visitInstruccionFor(self, ctx):
        return self.visit(ctx.forStatement())

    def visitInstruccionReturn(self, ctx):
        return self.visit(ctx.returnStmt())

    def visitInstruccionFuncion(self, ctx):
        return self.visit(ctx.funcionDecl())

    def visitInstruccionBloque(self, ctx):
        return self.visit(ctx.block())

    # ---------------- DECLARACIÓN ----------------
    def visitDeclaracion(self, ctx):
        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expresion()) if ctx.expresion() else 0
        self.memoria[nombre] = valor
        return valor

    # ---------------- ASIGNACIÓN ----------------
    def visitAsignacion(self, ctx):
        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expresion())
        self.memoria[nombre] = valor
        return valor

    # ---------------- VARIABLES ----------------
    def visitVariable(self, ctx):
        nombre = ctx.ID().getText()
        if nombre in self.memoria:
            return self.memoria[nombre]
        print(f"Error: variable '{nombre}' no definida")
        return 0

    # ---------------- BLOQUES ----------------
    def visitBlock(self, ctx):
        resultado = None
        for inst in ctx.instruccion():
            resultado = self.visit(inst)
        return resultado

    # ---------------- IF ----------------
    def visitIfStatement(self, ctx):
        condicion = self.visit(ctx.expresion())
        if float(condicion) == 1:
            return self.visit(ctx.block(0))
        elif ctx.block(1):
            return self.visit(ctx.block(1))
        return None

    # ---------------- WHILE ----------------
    def visitWhileStatement(self, ctx):
        resultado = None
        while float(self.visit(ctx.expresion())) == 1:
            resultado = self.visit(ctx.block())
        return resultado

    # ---------------- FOR ----------------
    def visitForStatement(self, ctx):
        self.visit(ctx.asignacion(0))  # inicialización
        resultado = None

        while float(self.visit(ctx.expresion())) == 1:
            resultado = self.visit(ctx.block())
            self.visit(ctx.asignacion(1))  # incremento

        return resultado

    # ---------------- RETURN ----------------
    def visitInstruccionReturn(self, ctx):
        expr = ctx.returnStmt().expresion()
        
        if expr:
            return self.visit(expr)   # return con valor
        else:
            return None              # return vacío

    # ---------------- FUNCIONES ----------------
    def visitFuncionDecl(self, ctx):
        nombre = ctx.ID().getText()
        self.funciones[nombre] = ctx
        return None

    def visitLlamadaFuncion(self, ctx):
        nombre = ctx.ID().getText()

        if nombre not in self.funciones:
            print(f"Error: función '{nombre}' no definida")
            return 0

        funcion = self.funciones[nombre]

        memoria_anterior = self.memoria.copy()

        # parámetros
        if funcion.params() and ctx.args():
            params = funcion.params().ID()
            args = ctx.args().expresion()

            for i in range(len(params)):
                self.memoria[params[i].getText()] = self.visit(args[i])

        resultado = self.visit(funcion.block())

        self.memoria = memoria_anterior

        return resultado

    # ---------------- EXPRESIONES ----------------
    def visitNumero(self, ctx):
        return float(ctx.NUMERO().getText())

    def visitCadena(self, ctx):
        texto = ctx.STRING().getText()[1:-1]
        return texto.replace('\\n', '\n').replace('\\r', '\n')

    def visitBooleano(self, ctx):
        return 1 if ctx.getText() == "true" else 0

    def visitParentesis(self, ctx):
        return self.visit(ctx.expresion())

    def visitCorchetes(self, ctx):
        return self.visit(ctx.expresion())

    def visitNotLogico(self, ctx):
        val = self.visit(ctx.expresion())
        return 1 if val == 0 else 0

    def visitMultiplicacionDivisision(self, ctx):
        izq = self.visit(ctx.expresion(0))
        der = self.visit(ctx.expresion(1))
        if ctx.op.text == '*':
            return izq * der
        return izq / der if der != 0 else 0

    def visitSumaResta(self, ctx):
        izq = self.visit(ctx.expresion(0))
        der = self.visit(ctx.expresion(1))
        if ctx.op.text == '+':
            return izq + der
        return izq - der

    def visitRelacional(self, ctx):
        izq = self.visit(ctx.expresion(0))
        der = self.visit(ctx.expresion(1))
        op = ctx.op.text

        if op == '==': return 1 if izq == der else 0
        if op in ['!=', '<>']: return 1 if izq != der else 0
        if op == '<': return 1 if izq < der else 0
        if op == '>': return 1 if izq > der else 0
        if op == '<=': return 1 if izq <= der else 0
        if op == '>=': return 1 if izq >= der else 0
        return 0

    def visitAndOrLogico(self, ctx):
        izq = self.visit(ctx.expresion(0))
        der = self.visit(ctx.expresion(1))
        if ctx.op.text == '&&':
            return 1 if (izq and der) else 0
        if ctx.op.text == '||':
            return 1 if (izq or der) else 0
        return 0


# ---------------- AST ----------------
def generar_dot(tree, parser):
    from antlr4.tree.Trees import Trees
    lineas = ["digraph AST {"]
    lineas.append('node [shape=box];')

    def recorrer(nodo, padre=None, i=0):
        nombre = f"n{i}"
        texto = Trees.getNodeText(nodo, parser.ruleNames).replace('"', '\\"')
        lineas.append(f'{nombre} [label="{texto}"];')

        if padre:
            lineas.append(f"{padre} -> {nombre};")

        j = i + 1
        for k in range(nodo.getChildCount()):
            j = recorrer(nodo.getChild(k), nombre, j)
        return j

    recorrer(tree)
    lineas.append("}")
    return "\n".join(lineas)


def guardar_ast_grafico(tree, parser, nombre_archivo="arbol_ast"):
    dot_data = generar_dot(tree, parser)
    with open(f"{nombre_archivo}.dot", "w") as f:
        f.write(dot_data)

    try:
        subprocess.run(["dot", "-Tpng", f"{nombre_archivo}.dot", "-o", f"{nombre_archivo}.png"])
        print(f"\n[ÉXITO] AST generado: {nombre_archivo}.png")
    except Exception as e:
        print(f"\n[ERROR] {e}")


# ---------------- MAIN ----------------
def main():
    input_stream = FileStream('operaciones.txt', encoding='utf-8')
    lexer = CalculadoraLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CalculadoraParser(stream)

    tree = parser.archivo()

    guardar_ast_grafico(tree, parser)

    print("\nAST:")
    print(Trees.toStringTree(tree, None, parser))

    visitante = EvaluarVisitante()
    visitante.visit(tree)


if __name__ == '__main__':
    main()