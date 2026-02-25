import sys
from antlr4 import *
from CalculadoraLexer import CalculadoraLexer
from CalculadoraParser import CalculadoraParser
from CalculadoraVisitor import CalculadoraVisitor # <--- Asegúrate de que esta línea esté

class EvaluarVisitante(CalculadoraVisitor):
    def visitMultiplicacionDivisision(self, ctx):
        izq = self.visit(ctx.expresion(0))
        der = self.visit(ctx.expresion(1))
        if izq is None or der is None: return 0
        if ctx.op.text == '*': return izq * der
        return izq / der

    def visitSumaResta(self, ctx):
        izq = self.visit(ctx.expresion(0))
        der = self.visit(ctx.expresion(1))
        if izq is None or der is None: return 0
        if ctx.op.text == '+': return izq + der
        return izq - der

    def visitNumero(self, ctx):
        return float(ctx.NUMERO().getText())

    def visitParentesis(self, ctx):
        return self.visit(ctx.expresion())

    def visitInstruccion(self, ctx):
        # Visitamos la expresión dentro de la instrucción y la retornamos
        return self.visit(ctx.expresion())

def main():
    # Asegúrate de que el archivo existe
    input_stream = FileStream('operaciones.txt')
    lexer = CalculadoraLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CalculadoraParser(stream)
    tree = parser.archivo()

    evaluador = EvaluarVisitante()
    
    # Recorremos cada instrucción (línea) del archivo
    for inst in tree.instruccion():
        resultado = evaluador.visit(inst)
        if resultado is not None:
            print(f"Resultado: {resultado}")

if __name__ == '__main__':
    main()