# Generated from Calculadora.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CalculadoraParser import CalculadoraParser
else:
    from CalculadoraParser import CalculadoraParser

# This class defines a complete listener for a parse tree produced by CalculadoraParser.
class CalculadoraListener(ParseTreeListener):

    # Enter a parse tree produced by CalculadoraParser#archivo.
    def enterArchivo(self, ctx:CalculadoraParser.ArchivoContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#archivo.
    def exitArchivo(self, ctx:CalculadoraParser.ArchivoContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#instruccion.
    def enterInstruccion(self, ctx:CalculadoraParser.InstruccionContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#instruccion.
    def exitInstruccion(self, ctx:CalculadoraParser.InstruccionContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#Numero.
    def enterNumero(self, ctx:CalculadoraParser.NumeroContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#Numero.
    def exitNumero(self, ctx:CalculadoraParser.NumeroContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#Parentesis.
    def enterParentesis(self, ctx:CalculadoraParser.ParentesisContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#Parentesis.
    def exitParentesis(self, ctx:CalculadoraParser.ParentesisContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#MultiplicacionDivisision.
    def enterMultiplicacionDivisision(self, ctx:CalculadoraParser.MultiplicacionDivisisionContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#MultiplicacionDivisision.
    def exitMultiplicacionDivisision(self, ctx:CalculadoraParser.MultiplicacionDivisisionContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#SumaResta.
    def enterSumaResta(self, ctx:CalculadoraParser.SumaRestaContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#SumaResta.
    def exitSumaResta(self, ctx:CalculadoraParser.SumaRestaContext):
        pass



del CalculadoraParser