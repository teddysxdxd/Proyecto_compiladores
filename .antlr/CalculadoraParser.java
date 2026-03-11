// Generated from /home/morales/proyecto/Proyecto_compiladores/Calculadora.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class CalculadoraParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		INICIOPROGRAMA=1, FINPROGRAMA=2, PRINTI=3, BLOCKI=4, BLOCKF=5, IFINICIO=6, 
		ELSE=7, PARENTESISI=8, PARENTESISD=9, CORCHI=10, CORCHD=11, NOTLOGICO=12, 
		MULT=13, DIV=14, SUM=15, REST=16, IGUALA=17, DIFERENTEA=18, DIFERENTEA2=19, 
		MENORQUE=20, MAYORQUE=21, MENORIGUAL=22, MAYORIGUAL=23, AND=24, OR=25, 
		NUMERO=26, STRING=27, NEWLINE=28, WS=29, ID=30, ASSIGN=31;
	public static final int
		RULE_archivo = 0, RULE_instruccion = 1, RULE_block = 2, RULE_ifStatement = 3, 
		RULE_expresion = 4;
	private static String[] makeRuleNames() {
		return new String[] {
			"archivo", "instruccion", "block", "ifStatement", "expresion"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'Program'", "'End_Program'", "'print'", "'{'", "'}'", "'simon'", 
			"'sinel'", "'('", "')'", "'['", "']'", "'!'", "'*'", "'/'", "'+'", "'-'", 
			"'=='", "'!='", "'<>'", "'<'", "'>'", "'<='", "'>='", "'&&'", "'||'", 
			null, null, null, null, null, "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "INICIOPROGRAMA", "FINPROGRAMA", "PRINTI", "BLOCKI", "BLOCKF", 
			"IFINICIO", "ELSE", "PARENTESISI", "PARENTESISD", "CORCHI", "CORCHD", 
			"NOTLOGICO", "MULT", "DIV", "SUM", "REST", "IGUALA", "DIFERENTEA", "DIFERENTEA2", 
			"MENORQUE", "MAYORQUE", "MENORIGUAL", "MAYORIGUAL", "AND", "OR", "NUMERO", 
			"STRING", "NEWLINE", "WS", "ID", "ASSIGN"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Calculadora.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public CalculadoraParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArchivoContext extends ParserRuleContext {
		public TerminalNode INICIOPROGRAMA() { return getToken(CalculadoraParser.INICIOPROGRAMA, 0); }
		public TerminalNode FINPROGRAMA() { return getToken(CalculadoraParser.FINPROGRAMA, 0); }
		public TerminalNode EOF() { return getToken(CalculadoraParser.EOF, 0); }
		public List<InstruccionContext> instruccion() {
			return getRuleContexts(InstruccionContext.class);
		}
		public InstruccionContext instruccion(int i) {
			return getRuleContext(InstruccionContext.class,i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(CalculadoraParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(CalculadoraParser.NEWLINE, i);
		}
		public ArchivoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_archivo; }
	}

	public final ArchivoContext archivo() throws RecognitionException {
		ArchivoContext _localctx = new ArchivoContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_archivo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(10);
			match(INICIOPROGRAMA);
			setState(15);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1543509336L) != 0)) {
				{
				setState(13);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case PRINTI:
				case BLOCKI:
				case IFINICIO:
				case PARENTESISI:
				case CORCHI:
				case NOTLOGICO:
				case NUMERO:
				case STRING:
				case ID:
					{
					setState(11);
					instruccion();
					}
					break;
				case NEWLINE:
					{
					setState(12);
					match(NEWLINE);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(17);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(18);
			match(FINPROGRAMA);
			setState(19);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InstruccionContext extends ParserRuleContext {
		public InstruccionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instruccion; }
	 
		public InstruccionContext() { }
		public void copyFrom(InstruccionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class InstruccionIfContext extends InstruccionContext {
		public IfStatementContext ifStatement() {
			return getRuleContext(IfStatementContext.class,0);
		}
		public InstruccionIfContext(InstruccionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PrintStmtContext extends InstruccionContext {
		public TerminalNode PRINTI() { return getToken(CalculadoraParser.PRINTI, 0); }
		public TerminalNode PARENTESISI() { return getToken(CalculadoraParser.PARENTESISI, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode PARENTESISD() { return getToken(CalculadoraParser.PARENTESISD, 0); }
		public PrintStmtContext(InstruccionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class InstruccionExpresionContext extends InstruccionContext {
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public InstruccionExpresionContext(InstruccionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AsignacionContext extends InstruccionContext {
		public TerminalNode ID() { return getToken(CalculadoraParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(CalculadoraParser.ASSIGN, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public AsignacionContext(InstruccionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class InstruccionBloqueContext extends InstruccionContext {
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public InstruccionBloqueContext(InstruccionContext ctx) { copyFrom(ctx); }
	}

	public final InstruccionContext instruccion() throws RecognitionException {
		InstruccionContext _localctx = new InstruccionContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_instruccion);
		try {
			setState(32);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				_localctx = new InstruccionExpresionContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(21);
				expresion(0);
				}
				break;
			case 2:
				_localctx = new AsignacionContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(22);
				match(ID);
				setState(23);
				match(ASSIGN);
				setState(24);
				expresion(0);
				}
				break;
			case 3:
				_localctx = new PrintStmtContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(25);
				match(PRINTI);
				setState(26);
				match(PARENTESISI);
				setState(27);
				expresion(0);
				setState(28);
				match(PARENTESISD);
				}
				break;
			case 4:
				_localctx = new InstruccionIfContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(30);
				ifStatement();
				}
				break;
			case 5:
				_localctx = new InstruccionBloqueContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(31);
				block();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockContext extends ParserRuleContext {
		public TerminalNode BLOCKI() { return getToken(CalculadoraParser.BLOCKI, 0); }
		public TerminalNode BLOCKF() { return getToken(CalculadoraParser.BLOCKF, 0); }
		public List<InstruccionContext> instruccion() {
			return getRuleContexts(InstruccionContext.class);
		}
		public InstruccionContext instruccion(int i) {
			return getRuleContext(InstruccionContext.class,i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(CalculadoraParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(CalculadoraParser.NEWLINE, i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(34);
			match(BLOCKI);
			setState(39);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1543509336L) != 0)) {
				{
				setState(37);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case PRINTI:
				case BLOCKI:
				case IFINICIO:
				case PARENTESISI:
				case CORCHI:
				case NOTLOGICO:
				case NUMERO:
				case STRING:
				case ID:
					{
					setState(35);
					instruccion();
					}
					break;
				case NEWLINE:
					{
					setState(36);
					match(NEWLINE);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(41);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(42);
			match(BLOCKF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfStatementContext extends ParserRuleContext {
		public TerminalNode IFINICIO() { return getToken(CalculadoraParser.IFINICIO, 0); }
		public TerminalNode PARENTESISI() { return getToken(CalculadoraParser.PARENTESISI, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode PARENTESISD() { return getToken(CalculadoraParser.PARENTESISD, 0); }
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(CalculadoraParser.ELSE, 0); }
		public IfStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStatement; }
	}

	public final IfStatementContext ifStatement() throws RecognitionException {
		IfStatementContext _localctx = new IfStatementContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_ifStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(44);
			match(IFINICIO);
			setState(45);
			match(PARENTESISI);
			setState(46);
			expresion(0);
			setState(47);
			match(PARENTESISD);
			setState(48);
			block();
			setState(51);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(49);
				match(ELSE);
				setState(50);
				block();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpresionContext extends ParserRuleContext {
		public ExpresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresion; }
	 
		public ExpresionContext() { }
		public void copyFrom(ExpresionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AndOrLogicoContext extends ExpresionContext {
		public Token op;
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
		}
		public TerminalNode AND() { return getToken(CalculadoraParser.AND, 0); }
		public TerminalNode OR() { return getToken(CalculadoraParser.OR, 0); }
		public AndOrLogicoContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NumeroContext extends ExpresionContext {
		public TerminalNode NUMERO() { return getToken(CalculadoraParser.NUMERO, 0); }
		public NumeroContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CorchetesContext extends ExpresionContext {
		public TerminalNode CORCHI() { return getToken(CalculadoraParser.CORCHI, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode CORCHD() { return getToken(CalculadoraParser.CORCHD, 0); }
		public CorchetesContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class VariableContext extends ExpresionContext {
		public TerminalNode ID() { return getToken(CalculadoraParser.ID, 0); }
		public VariableContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class RelacionalContext extends ExpresionContext {
		public Token op;
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
		}
		public TerminalNode IGUALA() { return getToken(CalculadoraParser.IGUALA, 0); }
		public TerminalNode DIFERENTEA() { return getToken(CalculadoraParser.DIFERENTEA, 0); }
		public TerminalNode DIFERENTEA2() { return getToken(CalculadoraParser.DIFERENTEA2, 0); }
		public TerminalNode MENORQUE() { return getToken(CalculadoraParser.MENORQUE, 0); }
		public TerminalNode MAYORQUE() { return getToken(CalculadoraParser.MAYORQUE, 0); }
		public TerminalNode MENORIGUAL() { return getToken(CalculadoraParser.MENORIGUAL, 0); }
		public TerminalNode MAYORIGUAL() { return getToken(CalculadoraParser.MAYORIGUAL, 0); }
		public RelacionalContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ParentesisContext extends ExpresionContext {
		public TerminalNode PARENTESISI() { return getToken(CalculadoraParser.PARENTESISI, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode PARENTESISD() { return getToken(CalculadoraParser.PARENTESISD, 0); }
		public ParentesisContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CadenaContext extends ExpresionContext {
		public TerminalNode STRING() { return getToken(CalculadoraParser.STRING, 0); }
		public CadenaContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NotLogicoContext extends ExpresionContext {
		public TerminalNode NOTLOGICO() { return getToken(CalculadoraParser.NOTLOGICO, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public NotLogicoContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MultiplicacionDivisisionContext extends ExpresionContext {
		public Token op;
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
		}
		public TerminalNode MULT() { return getToken(CalculadoraParser.MULT, 0); }
		public TerminalNode DIV() { return getToken(CalculadoraParser.DIV, 0); }
		public MultiplicacionDivisisionContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class SumaRestaContext extends ExpresionContext {
		public Token op;
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
		}
		public TerminalNode SUM() { return getToken(CalculadoraParser.SUM, 0); }
		public TerminalNode REST() { return getToken(CalculadoraParser.REST, 0); }
		public SumaRestaContext(ExpresionContext ctx) { copyFrom(ctx); }
	}

	public final ExpresionContext expresion() throws RecognitionException {
		return expresion(0);
	}

	private ExpresionContext expresion(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpresionContext _localctx = new ExpresionContext(_ctx, _parentState);
		ExpresionContext _prevctx = _localctx;
		int _startState = 8;
		enterRecursionRule(_localctx, 8, RULE_expresion, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PARENTESISI:
				{
				_localctx = new ParentesisContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(54);
				match(PARENTESISI);
				setState(55);
				expresion(0);
				setState(56);
				match(PARENTESISD);
				}
				break;
			case CORCHI:
				{
				_localctx = new CorchetesContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(58);
				match(CORCHI);
				setState(59);
				expresion(0);
				setState(60);
				match(CORCHD);
				}
				break;
			case NUMERO:
				{
				_localctx = new NumeroContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(62);
				match(NUMERO);
				}
				break;
			case STRING:
				{
				_localctx = new CadenaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(63);
				match(STRING);
				}
				break;
			case ID:
				{
				_localctx = new VariableContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(64);
				match(ID);
				}
				break;
			case NOTLOGICO:
				{
				_localctx = new NotLogicoContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(65);
				match(NOTLOGICO);
				setState(66);
				expresion(5);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(83);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(81);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
					case 1:
						{
						_localctx = new MultiplicacionDivisisionContext(new ExpresionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expresion);
						setState(69);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(70);
						((MultiplicacionDivisisionContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==MULT || _la==DIV) ) {
							((MultiplicacionDivisisionContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(71);
						expresion(5);
						}
						break;
					case 2:
						{
						_localctx = new SumaRestaContext(new ExpresionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expresion);
						setState(72);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(73);
						((SumaRestaContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==SUM || _la==REST) ) {
							((SumaRestaContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(74);
						expresion(4);
						}
						break;
					case 3:
						{
						_localctx = new RelacionalContext(new ExpresionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expresion);
						setState(75);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(76);
						((RelacionalContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 16646144L) != 0)) ) {
							((RelacionalContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(77);
						expresion(3);
						}
						break;
					case 4:
						{
						_localctx = new AndOrLogicoContext(new ExpresionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expresion);
						setState(78);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(79);
						((AndOrLogicoContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==AND || _la==OR) ) {
							((AndOrLogicoContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(80);
						expresion(2);
						}
						break;
					}
					} 
				}
				setState(85);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 4:
			return expresion_sempred((ExpresionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expresion_sempred(ExpresionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 4);
		case 1:
			return precpred(_ctx, 3);
		case 2:
			return precpred(_ctx, 2);
		case 3:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u001fW\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0005\u0000\u000e\b\u0000\n\u0000\f\u0000"+
		"\u0011\t\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001!\b\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0005\u0002&\b\u0002\n\u0002\f\u0002)\t\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u00034\b\u0003\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0003\u0004D\b\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004R\b\u0004\n\u0004\f\u0004"+
		"U\t\u0004\u0001\u0004\u0000\u0001\b\u0005\u0000\u0002\u0004\u0006\b\u0000"+
		"\u0004\u0001\u0000\r\u000e\u0001\u0000\u000f\u0010\u0001\u0000\u0011\u0017"+
		"\u0001\u0000\u0018\u0019c\u0000\n\u0001\u0000\u0000\u0000\u0002 \u0001"+
		"\u0000\u0000\u0000\u0004\"\u0001\u0000\u0000\u0000\u0006,\u0001\u0000"+
		"\u0000\u0000\bC\u0001\u0000\u0000\u0000\n\u000f\u0005\u0001\u0000\u0000"+
		"\u000b\u000e\u0003\u0002\u0001\u0000\f\u000e\u0005\u001c\u0000\u0000\r"+
		"\u000b\u0001\u0000\u0000\u0000\r\f\u0001\u0000\u0000\u0000\u000e\u0011"+
		"\u0001\u0000\u0000\u0000\u000f\r\u0001\u0000\u0000\u0000\u000f\u0010\u0001"+
		"\u0000\u0000\u0000\u0010\u0012\u0001\u0000\u0000\u0000\u0011\u000f\u0001"+
		"\u0000\u0000\u0000\u0012\u0013\u0005\u0002\u0000\u0000\u0013\u0014\u0005"+
		"\u0000\u0000\u0001\u0014\u0001\u0001\u0000\u0000\u0000\u0015!\u0003\b"+
		"\u0004\u0000\u0016\u0017\u0005\u001e\u0000\u0000\u0017\u0018\u0005\u001f"+
		"\u0000\u0000\u0018!\u0003\b\u0004\u0000\u0019\u001a\u0005\u0003\u0000"+
		"\u0000\u001a\u001b\u0005\b\u0000\u0000\u001b\u001c\u0003\b\u0004\u0000"+
		"\u001c\u001d\u0005\t\u0000\u0000\u001d!\u0001\u0000\u0000\u0000\u001e"+
		"!\u0003\u0006\u0003\u0000\u001f!\u0003\u0004\u0002\u0000 \u0015\u0001"+
		"\u0000\u0000\u0000 \u0016\u0001\u0000\u0000\u0000 \u0019\u0001\u0000\u0000"+
		"\u0000 \u001e\u0001\u0000\u0000\u0000 \u001f\u0001\u0000\u0000\u0000!"+
		"\u0003\u0001\u0000\u0000\u0000\"\'\u0005\u0004\u0000\u0000#&\u0003\u0002"+
		"\u0001\u0000$&\u0005\u001c\u0000\u0000%#\u0001\u0000\u0000\u0000%$\u0001"+
		"\u0000\u0000\u0000&)\u0001\u0000\u0000\u0000\'%\u0001\u0000\u0000\u0000"+
		"\'(\u0001\u0000\u0000\u0000(*\u0001\u0000\u0000\u0000)\'\u0001\u0000\u0000"+
		"\u0000*+\u0005\u0005\u0000\u0000+\u0005\u0001\u0000\u0000\u0000,-\u0005"+
		"\u0006\u0000\u0000-.\u0005\b\u0000\u0000./\u0003\b\u0004\u0000/0\u0005"+
		"\t\u0000\u000003\u0003\u0004\u0002\u000012\u0005\u0007\u0000\u000024\u0003"+
		"\u0004\u0002\u000031\u0001\u0000\u0000\u000034\u0001\u0000\u0000\u0000"+
		"4\u0007\u0001\u0000\u0000\u000056\u0006\u0004\uffff\uffff\u000067\u0005"+
		"\b\u0000\u000078\u0003\b\u0004\u000089\u0005\t\u0000\u00009D\u0001\u0000"+
		"\u0000\u0000:;\u0005\n\u0000\u0000;<\u0003\b\u0004\u0000<=\u0005\u000b"+
		"\u0000\u0000=D\u0001\u0000\u0000\u0000>D\u0005\u001a\u0000\u0000?D\u0005"+
		"\u001b\u0000\u0000@D\u0005\u001e\u0000\u0000AB\u0005\f\u0000\u0000BD\u0003"+
		"\b\u0004\u0005C5\u0001\u0000\u0000\u0000C:\u0001\u0000\u0000\u0000C>\u0001"+
		"\u0000\u0000\u0000C?\u0001\u0000\u0000\u0000C@\u0001\u0000\u0000\u0000"+
		"CA\u0001\u0000\u0000\u0000DS\u0001\u0000\u0000\u0000EF\n\u0004\u0000\u0000"+
		"FG\u0007\u0000\u0000\u0000GR\u0003\b\u0004\u0005HI\n\u0003\u0000\u0000"+
		"IJ\u0007\u0001\u0000\u0000JR\u0003\b\u0004\u0004KL\n\u0002\u0000\u0000"+
		"LM\u0007\u0002\u0000\u0000MR\u0003\b\u0004\u0003NO\n\u0001\u0000\u0000"+
		"OP\u0007\u0003\u0000\u0000PR\u0003\b\u0004\u0002QE\u0001\u0000\u0000\u0000"+
		"QH\u0001\u0000\u0000\u0000QK\u0001\u0000\u0000\u0000QN\u0001\u0000\u0000"+
		"\u0000RU\u0001\u0000\u0000\u0000SQ\u0001\u0000\u0000\u0000ST\u0001\u0000"+
		"\u0000\u0000T\t\u0001\u0000\u0000\u0000US\u0001\u0000\u0000\u0000\t\r"+
		"\u000f %\'3CQS";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}