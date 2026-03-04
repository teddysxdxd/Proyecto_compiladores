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


    # Visit a parse tree produced by CalculadoraParser#InstruccionExpresion.
    def visitInstruccionExpresion(self, ctx:CalculadoraParser.InstruccionExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#printStmt.
    def visitPrintStmt(self, ctx:CalculadoraParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#InstruccionIf.
    def visitInstruccionIf(self, ctx:CalculadoraParser.InstruccionIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#InstruccionBloque.
    def visitInstruccionBloque(self, ctx:CalculadoraParser.InstruccionBloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#block.
    def visitBlock(self, ctx:CalculadoraParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#ifStatement.
    def visitIfStatement(self, ctx:CalculadoraParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#AndOrLogico.
    def visitAndOrLogico(self, ctx:CalculadoraParser.AndOrLogicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#Numero.
    def visitNumero(self, ctx:CalculadoraParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#Relacional.
    def visitRelacional(self, ctx:CalculadoraParser.RelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#Parentesis.
    def visitParentesis(self, ctx:CalculadoraParser.ParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#Cadena.
    def visitCadena(self, ctx:CalculadoraParser.CadenaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#NotLogico.
    def visitNotLogico(self, ctx:CalculadoraParser.NotLogicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#MultiplicacionDivisision.
    def visitMultiplicacionDivisision(self, ctx:CalculadoraParser.MultiplicacionDivisisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#SumaResta.
    def visitSumaResta(self, ctx:CalculadoraParser.SumaRestaContext):
        return self.visitChildren(ctx)



del CalculadoraParser