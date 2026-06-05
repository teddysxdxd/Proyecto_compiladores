# Generated from gramatica_v4.g4 by ANTLR 4.13.1
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


    # Visit a parse tree produced by CalculadoraParser#importStatement.
    def visitImportStatement(self, ctx:CalculadoraParser.ImportStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#InstruccionDeclaracion.
    def visitInstruccionDeclaracion(self, ctx:CalculadoraParser.InstruccionDeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#EjecutarAsignacion.
    def visitEjecutarAsignacion(self, ctx:CalculadoraParser.EjecutarAsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#EjecutarPrint.
    def visitEjecutarPrint(self, ctx:CalculadoraParser.EjecutarPrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#InstruccionSwitch.
    def visitInstruccionSwitch(self, ctx:CalculadoraParser.InstruccionSwitchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#InstruccionIf.
    def visitInstruccionIf(self, ctx:CalculadoraParser.InstruccionIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#InstruccionWhile.
    def visitInstruccionWhile(self, ctx:CalculadoraParser.InstruccionWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#InstruccionFor.
    def visitInstruccionFor(self, ctx:CalculadoraParser.InstruccionForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#InstruccionReturn.
    def visitInstruccionReturn(self, ctx:CalculadoraParser.InstruccionReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#InstruccionFuncion.
    def visitInstruccionFuncion(self, ctx:CalculadoraParser.InstruccionFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#InstruccionStruct.
    def visitInstruccionStruct(self, ctx:CalculadoraParser.InstruccionStructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#InstruccionExpresion.
    def visitInstruccionExpresion(self, ctx:CalculadoraParser.InstruccionExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#BreakStmt.
    def visitBreakStmt(self, ctx:CalculadoraParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#ContinueStmt.
    def visitContinueStmt(self, ctx:CalculadoraParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#InstruccionBloque.
    def visitInstruccionBloque(self, ctx:CalculadoraParser.InstruccionBloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#declaracion.
    def visitDeclaracion(self, ctx:CalculadoraParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#asignacion.
    def visitAsignacion(self, ctx:CalculadoraParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#returnStmt.
    def visitReturnStmt(self, ctx:CalculadoraParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#funcionDecl.
    def visitFuncionDecl(self, ctx:CalculadoraParser.FuncionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#params.
    def visitParams(self, ctx:CalculadoraParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#structDecl.
    def visitStructDecl(self, ctx:CalculadoraParser.StructDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#structFieldDecl.
    def visitStructFieldDecl(self, ctx:CalculadoraParser.StructFieldDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#whileStatement.
    def visitWhileStatement(self, ctx:CalculadoraParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#forStatement.
    def visitForStatement(self, ctx:CalculadoraParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#block.
    def visitBlock(self, ctx:CalculadoraParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#ifStatement.
    def visitIfStatement(self, ctx:CalculadoraParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#switchStatement.
    def visitSwitchStatement(self, ctx:CalculadoraParser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#caseClause.
    def visitCaseClause(self, ctx:CalculadoraParser.CaseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#defaultClause.
    def visitDefaultClause(self, ctx:CalculadoraParser.DefaultClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#lvalue.
    def visitLvalue(self, ctx:CalculadoraParser.LvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#Numero.
    def visitNumero(self, ctx:CalculadoraParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#Corchetes.
    def visitCorchetes(self, ctx:CalculadoraParser.CorchetesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#Variable.
    def visitVariable(self, ctx:CalculadoraParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#CastExplicito.
    def visitCastExplicito(self, ctx:CalculadoraParser.CastExplicitoContext):
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


    # Visit a parse tree produced by CalculadoraParser#MultiplicacionDivisisionMod.
    def visitMultiplicacionDivisisionMod(self, ctx:CalculadoraParser.MultiplicacionDivisisionModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#Booleano.
    def visitBooleano(self, ctx:CalculadoraParser.BooleanoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#SumaResta.
    def visitSumaResta(self, ctx:CalculadoraParser.SumaRestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#AndOrLogico.
    def visitAndOrLogico(self, ctx:CalculadoraParser.AndOrLogicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#Relacional.
    def visitRelacional(self, ctx:CalculadoraParser.RelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#LlamadaFuncion.
    def visitLlamadaFuncion(self, ctx:CalculadoraParser.LlamadaFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#Ternario.
    def visitTernario(self, ctx:CalculadoraParser.TernarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#LlamadaModulo.
    def visitLlamadaModulo(self, ctx:CalculadoraParser.LlamadaModuloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#args.
    def visitArgs(self, ctx:CalculadoraParser.ArgsContext):
        return self.visitChildren(ctx)



del CalculadoraParser