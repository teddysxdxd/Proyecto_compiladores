import sys
from antlr4 import *
from CalculadoraLexer import CalculadoraLexer
from CalculadoraParser import CalculadoraParser
from CalculadoraVisitor import CalculadoraVisitor

class EvaluarVisitante(CalculadoraVisitor):
    
    # --- Operaciones Aritméticas ---
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

    # --- Operaciones Relacionales ---
    def visitRelacional(self, ctx):
        izq = self.visit(ctx.expresion(0))
        der = self.visit(ctx.expresion(1))
        op = ctx.op.text
        if op == '==': return 1 if izq == der else 0
        if op == '!=' or op == '<>': return 1 if izq != der else 0
        if op == '<': return 1 if izq < der else 0
        if op == '>': return 1 if izq > der else 0
        if op == '<=': return 1 if izq <= der else 0
        if op == '>=': return 1 if izq >= der else 0
        return 0

    # --- Operaciones Lógicas ---
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

    def visitParentesis(self, ctx):
        return self.visit(ctx.expresion())

    def visitInstruccion(self, ctx):
        return self.visit(ctx.expresion())

def main():
    try:
        input_stream = FileStream('operaciones.txt')
        lexer = CalculadoraLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = CalculadoraParser(stream)
        tree = parser.archivo()

        evaluador = EvaluarVisitante()
        
        for inst in tree.instruccion():
            res = evaluador.visit(inst)
            if res is not None:
                # Traducción a formato amigable
                if isinstance(res, (int, float)):
                    if res == 1: print("Resultado: verdadero")
                    elif res == 0: print("Resultado: falso")
                    else: print(f"Resultado: {res}")
                else:
                    print(f"Resultado: {res}")
    except Exception as e:
        print(f"Error al ejecutar: {e}")

if __name__ == '__main__':
    main()