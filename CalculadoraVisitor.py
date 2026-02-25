# Generated from Calculadora.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CalculadoraParser import CalculadoraParser
else:
    from CalculadoraParser import CalculadoraParser

# This class defines a complete generic visitor for a parse tree produced by CalculadoraParser.

class CalculadoraVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculadoraParser#archivo.
    def visitArchivo(self, ctx:CalculadoraParser.ArchivoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#instruccion.
    def visitInstruccion(self, ctx:CalculadoraParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#Numero.
    def visitNumero(self, ctx:CalculadoraParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#Parentesis.
    def visitParentesis(self, ctx:CalculadoraParser.ParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#MultiplicacionDivisision.
    def visitMultiplicacionDivisision(self, ctx:CalculadoraParser.MultiplicacionDivisisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#SumaResta.
    def visitSumaResta(self, ctx:CalculadoraParser.SumaRestaContext):
        return self.visitChildren(ctx)



del CalculadoraParser