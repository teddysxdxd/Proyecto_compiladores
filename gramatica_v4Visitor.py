# Generated from gramatica_v4.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramatica_v4Parser import gramatica_v4Parser
else:
    from gramatica_v4Parser import gramatica_v4Parser

# This class defines a complete generic visitor for a parse tree produced by gramatica_v4Parser.

class gramatica_v4Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramatica_v4Parser#archivo.
    def visitArchivo(self, ctx:gramatica_v4Parser.ArchivoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#importStatement.
    def visitImportStatement(self, ctx:gramatica_v4Parser.ImportStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#InstruccionDeclaracion.
    def visitInstruccionDeclaracion(self, ctx:gramatica_v4Parser.InstruccionDeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#EjecutarAsignacion.
    def visitEjecutarAsignacion(self, ctx:gramatica_v4Parser.EjecutarAsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#EjecutarPrint.
    def visitEjecutarPrint(self, ctx:gramatica_v4Parser.EjecutarPrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#InstruccionSwitch.
    def visitInstruccionSwitch(self, ctx:gramatica_v4Parser.InstruccionSwitchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#InstruccionIf.
    def visitInstruccionIf(self, ctx:gramatica_v4Parser.InstruccionIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#InstruccionWhile.
    def visitInstruccionWhile(self, ctx:gramatica_v4Parser.InstruccionWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#InstruccionFor.
    def visitInstruccionFor(self, ctx:gramatica_v4Parser.InstruccionForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#InstruccionReturn.
    def visitInstruccionReturn(self, ctx:gramatica_v4Parser.InstruccionReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#InstruccionFuncion.
    def visitInstruccionFuncion(self, ctx:gramatica_v4Parser.InstruccionFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#InstruccionStruct.
    def visitInstruccionStruct(self, ctx:gramatica_v4Parser.InstruccionStructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#InstruccionExpresion.
    def visitInstruccionExpresion(self, ctx:gramatica_v4Parser.InstruccionExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#BreakStmt.
    def visitBreakStmt(self, ctx:gramatica_v4Parser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#ContinueStmt.
    def visitContinueStmt(self, ctx:gramatica_v4Parser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#InstruccionBloque.
    def visitInstruccionBloque(self, ctx:gramatica_v4Parser.InstruccionBloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#declaracion.
    def visitDeclaracion(self, ctx:gramatica_v4Parser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#asignacion.
    def visitAsignacion(self, ctx:gramatica_v4Parser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#returnStmt.
    def visitReturnStmt(self, ctx:gramatica_v4Parser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#funcionDecl.
    def visitFuncionDecl(self, ctx:gramatica_v4Parser.FuncionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#params.
    def visitParams(self, ctx:gramatica_v4Parser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#structDecl.
    def visitStructDecl(self, ctx:gramatica_v4Parser.StructDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#structFieldDecl.
    def visitStructFieldDecl(self, ctx:gramatica_v4Parser.StructFieldDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#whileStatement.
    def visitWhileStatement(self, ctx:gramatica_v4Parser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#forStatement.
    def visitForStatement(self, ctx:gramatica_v4Parser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#block.
    def visitBlock(self, ctx:gramatica_v4Parser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#ifStatement.
    def visitIfStatement(self, ctx:gramatica_v4Parser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#switchStatement.
    def visitSwitchStatement(self, ctx:gramatica_v4Parser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#caseClause.
    def visitCaseClause(self, ctx:gramatica_v4Parser.CaseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#defaultClause.
    def visitDefaultClause(self, ctx:gramatica_v4Parser.DefaultClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#lvalue.
    def visitLvalue(self, ctx:gramatica_v4Parser.LvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#Numero.
    def visitNumero(self, ctx:gramatica_v4Parser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#Corchetes.
    def visitCorchetes(self, ctx:gramatica_v4Parser.CorchetesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#Variable.
    def visitVariable(self, ctx:gramatica_v4Parser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#CastExplicito.
    def visitCastExplicito(self, ctx:gramatica_v4Parser.CastExplicitoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#Parentesis.
    def visitParentesis(self, ctx:gramatica_v4Parser.ParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#Cadena.
    def visitCadena(self, ctx:gramatica_v4Parser.CadenaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#NotLogico.
    def visitNotLogico(self, ctx:gramatica_v4Parser.NotLogicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#MultiplicacionDivisisionMod.
    def visitMultiplicacionDivisisionMod(self, ctx:gramatica_v4Parser.MultiplicacionDivisisionModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#Booleano.
    def visitBooleano(self, ctx:gramatica_v4Parser.BooleanoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#SumaResta.
    def visitSumaResta(self, ctx:gramatica_v4Parser.SumaRestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#AndOrLogico.
    def visitAndOrLogico(self, ctx:gramatica_v4Parser.AndOrLogicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#Relacional.
    def visitRelacional(self, ctx:gramatica_v4Parser.RelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#LlamadaFuncion.
    def visitLlamadaFuncion(self, ctx:gramatica_v4Parser.LlamadaFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#Ternario.
    def visitTernario(self, ctx:gramatica_v4Parser.TernarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#LlamadaModulo.
    def visitLlamadaModulo(self, ctx:gramatica_v4Parser.LlamadaModuloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#args.
    def visitArgs(self, ctx:gramatica_v4Parser.ArgsContext):
        return self.visitChildren(ctx)



del gramatica_v4Parser