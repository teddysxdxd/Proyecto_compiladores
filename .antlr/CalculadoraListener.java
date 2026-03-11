// Generated from /home/morales/proyecto/Proyecto_compiladores/Calculadora.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CalculadoraParser}.
 */
public interface CalculadoraListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CalculadoraParser#archivo}.
	 * @param ctx the parse tree
	 */
	void enterArchivo(CalculadoraParser.ArchivoContext ctx);
	/**
	 * Exit a parse tree produced by {@link CalculadoraParser#archivo}.
	 * @param ctx the parse tree
	 */
	void exitArchivo(CalculadoraParser.ArchivoContext ctx);
	/**
	 * Enter a parse tree produced by the {@code InstruccionExpresion}
	 * labeled alternative in {@link CalculadoraParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void enterInstruccionExpresion(CalculadoraParser.InstruccionExpresionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code InstruccionExpresion}
	 * labeled alternative in {@link CalculadoraParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void exitInstruccionExpresion(CalculadoraParser.InstruccionExpresionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Asignacion}
	 * labeled alternative in {@link CalculadoraParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void enterAsignacion(CalculadoraParser.AsignacionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Asignacion}
	 * labeled alternative in {@link CalculadoraParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void exitAsignacion(CalculadoraParser.AsignacionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code printStmt}
	 * labeled alternative in {@link CalculadoraParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void enterPrintStmt(CalculadoraParser.PrintStmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code printStmt}
	 * labeled alternative in {@link CalculadoraParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void exitPrintStmt(CalculadoraParser.PrintStmtContext ctx);
	/**
	 * Enter a parse tree produced by the {@code InstruccionIf}
	 * labeled alternative in {@link CalculadoraParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void enterInstruccionIf(CalculadoraParser.InstruccionIfContext ctx);
	/**
	 * Exit a parse tree produced by the {@code InstruccionIf}
	 * labeled alternative in {@link CalculadoraParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void exitInstruccionIf(CalculadoraParser.InstruccionIfContext ctx);
	/**
	 * Enter a parse tree produced by the {@code InstruccionBloque}
	 * labeled alternative in {@link CalculadoraParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void enterInstruccionBloque(CalculadoraParser.InstruccionBloqueContext ctx);
	/**
	 * Exit a parse tree produced by the {@code InstruccionBloque}
	 * labeled alternative in {@link CalculadoraParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void exitInstruccionBloque(CalculadoraParser.InstruccionBloqueContext ctx);
	/**
	 * Enter a parse tree produced by {@link CalculadoraParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(CalculadoraParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link CalculadoraParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(CalculadoraParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link CalculadoraParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(CalculadoraParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CalculadoraParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(CalculadoraParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AndOrLogico}
	 * labeled alternative in {@link CalculadoraParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterAndOrLogico(CalculadoraParser.AndOrLogicoContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AndOrLogico}
	 * labeled alternative in {@link CalculadoraParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitAndOrLogico(CalculadoraParser.AndOrLogicoContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Numero}
	 * labeled alternative in {@link CalculadoraParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterNumero(CalculadoraParser.NumeroContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Numero}
	 * labeled alternative in {@link CalculadoraParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitNumero(CalculadoraParser.NumeroContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Corchetes}
	 * labeled alternative in {@link CalculadoraParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterCorchetes(CalculadoraParser.CorchetesContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Corchetes}
	 * labeled alternative in {@link CalculadoraParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitCorchetes(CalculadoraParser.CorchetesContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Variable}
	 * labeled alternative in {@link CalculadoraParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterVariable(CalculadoraParser.VariableContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Variable}
	 * labeled alternative in {@link CalculadoraParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitVariable(CalculadoraParser.VariableContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Relacional}
	 * labeled alternative in {@link CalculadoraParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterRelacional(CalculadoraParser.RelacionalContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Relacional}
	 * labeled alternative in {@link CalculadoraParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitRelacional(CalculadoraParser.RelacionalContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Parentesis}
	 * labeled alternative in {@link CalculadoraParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterParentesis(CalculadoraParser.ParentesisContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Parentesis}
	 * labeled alternative in {@link CalculadoraParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitParentesis(CalculadoraParser.ParentesisContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Cadena}
	 * labeled alternative in {@link CalculadoraParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterCadena(CalculadoraParser.CadenaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Cadena}
	 * labeled alternative in {@link CalculadoraParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitCadena(CalculadoraParser.CadenaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code NotLogico}
	 * labeled alternative in {@link CalculadoraParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterNotLogico(CalculadoraParser.NotLogicoContext ctx);
	/**
	 * Exit a parse tree produced by the {@code NotLogico}
	 * labeled alternative in {@link CalculadoraParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitNotLogico(CalculadoraParser.NotLogicoContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MultiplicacionDivisision}
	 * labeled alternative in {@link CalculadoraParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterMultiplicacionDivisision(CalculadoraParser.MultiplicacionDivisisionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MultiplicacionDivisision}
	 * labeled alternative in {@link CalculadoraParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitMultiplicacionDivisision(CalculadoraParser.MultiplicacionDivisisionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SumaResta}
	 * labeled alternative in {@link CalculadoraParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterSumaResta(CalculadoraParser.SumaRestaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SumaResta}
	 * labeled alternative in {@link CalculadoraParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitSumaResta(CalculadoraParser.SumaRestaContext ctx);
}