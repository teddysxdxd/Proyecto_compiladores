// Generated from /home/ramir/proyecto1-compiladores/Proyecto_compiladores/Calculadora.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class CalculadoraLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		INICIOPROGRAMA=1, FINPROGRAMA=2, PRINTI=3, BLOCKI=4, BLOCKF=5, IFINICIO=6, 
		ELSE=7, PARENTESISI=8, PARENTESISD=9, CORCHI=10, CORCHD=11, NOTLOGICO=12, 
		MULT=13, DIV=14, SUM=15, REST=16, IGUALA=17, DIFERENTEA=18, DIFERENTEA2=19, 
		MENORQUE=20, MAYORQUE=21, MENORIGUAL=22, MAYORIGUAL=23, AND=24, OR=25, 
		NUMERO=26, STRING=27, WS=28, ID=29, ASSIGN=30;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"INICIOPROGRAMA", "FINPROGRAMA", "PRINTI", "BLOCKI", "BLOCKF", "IFINICIO", 
			"ELSE", "PARENTESISI", "PARENTESISD", "CORCHI", "CORCHD", "NOTLOGICO", 
			"MULT", "DIV", "SUM", "REST", "IGUALA", "DIFERENTEA", "DIFERENTEA2", 
			"MENORQUE", "MAYORQUE", "MENORIGUAL", "MAYORIGUAL", "AND", "OR", "NUMERO", 
			"STRING", "WS", "ID", "ASSIGN"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'Program'", "'End_Program'", "'print'", "'{'", "'}'", "'simon'", 
			"'sinel'", "'('", "')'", "'['", "']'", "'!'", "'*'", "'/'", "'+'", "'-'", 
			"'=='", "'!='", "'<>'", "'<'", "'>'", "'<='", "'>='", "'&&'", "'||'", 
			null, null, null, null, "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "INICIOPROGRAMA", "FINPROGRAMA", "PRINTI", "BLOCKI", "BLOCKF", 
			"IFINICIO", "ELSE", "PARENTESISI", "PARENTESISD", "CORCHI", "CORCHD", 
			"NOTLOGICO", "MULT", "DIV", "SUM", "REST", "IGUALA", "DIFERENTEA", "DIFERENTEA2", 
			"MENORQUE", "MAYORQUE", "MENORIGUAL", "MAYORIGUAL", "AND", "OR", "NUMERO", 
			"STRING", "WS", "ID", "ASSIGN"
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


	public CalculadoraLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Calculadora.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u001e\u00b8\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017"+
		"\u0002\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a"+
		"\u0002\u001b\u0007\u001b\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001"+
		"\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\r\u0001\r\u0001\u000e"+
		"\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015"+
		"\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0019\u0004\u0019"+
		"\u0094\b\u0019\u000b\u0019\f\u0019\u0095\u0001\u0019\u0001\u0019\u0004"+
		"\u0019\u009a\b\u0019\u000b\u0019\f\u0019\u009b\u0003\u0019\u009e\b\u0019"+
		"\u0001\u001a\u0001\u001a\u0005\u001a\u00a2\b\u001a\n\u001a\f\u001a\u00a5"+
		"\t\u001a\u0001\u001a\u0001\u001a\u0001\u001b\u0004\u001b\u00aa\b\u001b"+
		"\u000b\u001b\f\u001b\u00ab\u0001\u001b\u0001\u001b\u0001\u001c\u0001\u001c"+
		"\u0005\u001c\u00b2\b\u001c\n\u001c\f\u001c\u00b5\t\u001c\u0001\u001d\u0001"+
		"\u001d\u0001\u00a3\u0000\u001e\u0001\u0001\u0003\u0002\u0005\u0003\u0007"+
		"\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b"+
		"\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013"+
		"\'\u0014)\u0015+\u0016-\u0017/\u00181\u00193\u001a5\u001b7\u001c9\u001d"+
		";\u001e\u0001\u0000\u0004\u0001\u000009\u0003\u0000\t\n\r\r  \u0003\u0000"+
		"AZ__az\u0004\u000009AZ__az\u00bd\u0000\u0001\u0001\u0000\u0000\u0000\u0000"+
		"\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000"+
		"\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b"+
		"\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001"+
		"\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001"+
		"\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001"+
		"\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001"+
		"\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001"+
		"\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000"+
		"\u0000\u0000%\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000"+
		"\u0000)\u0001\u0000\u0000\u0000\u0000+\u0001\u0000\u0000\u0000\u0000-"+
		"\u0001\u0000\u0000\u0000\u0000/\u0001\u0000\u0000\u0000\u00001\u0001\u0000"+
		"\u0000\u0000\u00003\u0001\u0000\u0000\u0000\u00005\u0001\u0000\u0000\u0000"+
		"\u00007\u0001\u0000\u0000\u0000\u00009\u0001\u0000\u0000\u0000\u0000;"+
		"\u0001\u0000\u0000\u0000\u0001=\u0001\u0000\u0000\u0000\u0003E\u0001\u0000"+
		"\u0000\u0000\u0005Q\u0001\u0000\u0000\u0000\u0007W\u0001\u0000\u0000\u0000"+
		"\tY\u0001\u0000\u0000\u0000\u000b[\u0001\u0000\u0000\u0000\ra\u0001\u0000"+
		"\u0000\u0000\u000fg\u0001\u0000\u0000\u0000\u0011i\u0001\u0000\u0000\u0000"+
		"\u0013k\u0001\u0000\u0000\u0000\u0015m\u0001\u0000\u0000\u0000\u0017o"+
		"\u0001\u0000\u0000\u0000\u0019q\u0001\u0000\u0000\u0000\u001bs\u0001\u0000"+
		"\u0000\u0000\u001du\u0001\u0000\u0000\u0000\u001fw\u0001\u0000\u0000\u0000"+
		"!y\u0001\u0000\u0000\u0000#|\u0001\u0000\u0000\u0000%\u007f\u0001\u0000"+
		"\u0000\u0000\'\u0082\u0001\u0000\u0000\u0000)\u0084\u0001\u0000\u0000"+
		"\u0000+\u0086\u0001\u0000\u0000\u0000-\u0089\u0001\u0000\u0000\u0000/"+
		"\u008c\u0001\u0000\u0000\u00001\u008f\u0001\u0000\u0000\u00003\u0093\u0001"+
		"\u0000\u0000\u00005\u009f\u0001\u0000\u0000\u00007\u00a9\u0001\u0000\u0000"+
		"\u00009\u00af\u0001\u0000\u0000\u0000;\u00b6\u0001\u0000\u0000\u0000="+
		">\u0005P\u0000\u0000>?\u0005r\u0000\u0000?@\u0005o\u0000\u0000@A\u0005"+
		"g\u0000\u0000AB\u0005r\u0000\u0000BC\u0005a\u0000\u0000CD\u0005m\u0000"+
		"\u0000D\u0002\u0001\u0000\u0000\u0000EF\u0005E\u0000\u0000FG\u0005n\u0000"+
		"\u0000GH\u0005d\u0000\u0000HI\u0005_\u0000\u0000IJ\u0005P\u0000\u0000"+
		"JK\u0005r\u0000\u0000KL\u0005o\u0000\u0000LM\u0005g\u0000\u0000MN\u0005"+
		"r\u0000\u0000NO\u0005a\u0000\u0000OP\u0005m\u0000\u0000P\u0004\u0001\u0000"+
		"\u0000\u0000QR\u0005p\u0000\u0000RS\u0005r\u0000\u0000ST\u0005i\u0000"+
		"\u0000TU\u0005n\u0000\u0000UV\u0005t\u0000\u0000V\u0006\u0001\u0000\u0000"+
		"\u0000WX\u0005{\u0000\u0000X\b\u0001\u0000\u0000\u0000YZ\u0005}\u0000"+
		"\u0000Z\n\u0001\u0000\u0000\u0000[\\\u0005s\u0000\u0000\\]\u0005i\u0000"+
		"\u0000]^\u0005m\u0000\u0000^_\u0005o\u0000\u0000_`\u0005n\u0000\u0000"+
		"`\f\u0001\u0000\u0000\u0000ab\u0005s\u0000\u0000bc\u0005i\u0000\u0000"+
		"cd\u0005n\u0000\u0000de\u0005e\u0000\u0000ef\u0005l\u0000\u0000f\u000e"+
		"\u0001\u0000\u0000\u0000gh\u0005(\u0000\u0000h\u0010\u0001\u0000\u0000"+
		"\u0000ij\u0005)\u0000\u0000j\u0012\u0001\u0000\u0000\u0000kl\u0005[\u0000"+
		"\u0000l\u0014\u0001\u0000\u0000\u0000mn\u0005]\u0000\u0000n\u0016\u0001"+
		"\u0000\u0000\u0000op\u0005!\u0000\u0000p\u0018\u0001\u0000\u0000\u0000"+
		"qr\u0005*\u0000\u0000r\u001a\u0001\u0000\u0000\u0000st\u0005/\u0000\u0000"+
		"t\u001c\u0001\u0000\u0000\u0000uv\u0005+\u0000\u0000v\u001e\u0001\u0000"+
		"\u0000\u0000wx\u0005-\u0000\u0000x \u0001\u0000\u0000\u0000yz\u0005=\u0000"+
		"\u0000z{\u0005=\u0000\u0000{\"\u0001\u0000\u0000\u0000|}\u0005!\u0000"+
		"\u0000}~\u0005=\u0000\u0000~$\u0001\u0000\u0000\u0000\u007f\u0080\u0005"+
		"<\u0000\u0000\u0080\u0081\u0005>\u0000\u0000\u0081&\u0001\u0000\u0000"+
		"\u0000\u0082\u0083\u0005<\u0000\u0000\u0083(\u0001\u0000\u0000\u0000\u0084"+
		"\u0085\u0005>\u0000\u0000\u0085*\u0001\u0000\u0000\u0000\u0086\u0087\u0005"+
		"<\u0000\u0000\u0087\u0088\u0005=\u0000\u0000\u0088,\u0001\u0000\u0000"+
		"\u0000\u0089\u008a\u0005>\u0000\u0000\u008a\u008b\u0005=\u0000\u0000\u008b"+
		".\u0001\u0000\u0000\u0000\u008c\u008d\u0005&\u0000\u0000\u008d\u008e\u0005"+
		"&\u0000\u0000\u008e0\u0001\u0000\u0000\u0000\u008f\u0090\u0005|\u0000"+
		"\u0000\u0090\u0091\u0005|\u0000\u0000\u00912\u0001\u0000\u0000\u0000\u0092"+
		"\u0094\u0007\u0000\u0000\u0000\u0093\u0092\u0001\u0000\u0000\u0000\u0094"+
		"\u0095\u0001\u0000\u0000\u0000\u0095\u0093\u0001\u0000\u0000\u0000\u0095"+
		"\u0096\u0001\u0000\u0000\u0000\u0096\u009d\u0001\u0000\u0000\u0000\u0097"+
		"\u0099\u0005.\u0000\u0000\u0098\u009a\u0007\u0000\u0000\u0000\u0099\u0098"+
		"\u0001\u0000\u0000\u0000\u009a\u009b\u0001\u0000\u0000\u0000\u009b\u0099"+
		"\u0001\u0000\u0000\u0000\u009b\u009c\u0001\u0000\u0000\u0000\u009c\u009e"+
		"\u0001\u0000\u0000\u0000\u009d\u0097\u0001\u0000\u0000\u0000\u009d\u009e"+
		"\u0001\u0000\u0000\u0000\u009e4\u0001\u0000\u0000\u0000\u009f\u00a3\u0005"+
		"\"\u0000\u0000\u00a0\u00a2\t\u0000\u0000\u0000\u00a1\u00a0\u0001\u0000"+
		"\u0000\u0000\u00a2\u00a5\u0001\u0000\u0000\u0000\u00a3\u00a4\u0001\u0000"+
		"\u0000\u0000\u00a3\u00a1\u0001\u0000\u0000\u0000\u00a4\u00a6\u0001\u0000"+
		"\u0000\u0000\u00a5\u00a3\u0001\u0000\u0000\u0000\u00a6\u00a7\u0005\"\u0000"+
		"\u0000\u00a76\u0001\u0000\u0000\u0000\u00a8\u00aa\u0007\u0001\u0000\u0000"+
		"\u00a9\u00a8\u0001\u0000\u0000\u0000\u00aa\u00ab\u0001\u0000\u0000\u0000"+
		"\u00ab\u00a9\u0001\u0000\u0000\u0000\u00ab\u00ac\u0001\u0000\u0000\u0000"+
		"\u00ac\u00ad\u0001\u0000\u0000\u0000\u00ad\u00ae\u0006\u001b\u0000\u0000"+
		"\u00ae8\u0001\u0000\u0000\u0000\u00af\u00b3\u0007\u0002\u0000\u0000\u00b0"+
		"\u00b2\u0007\u0003\u0000\u0000\u00b1\u00b0\u0001\u0000\u0000\u0000\u00b2"+
		"\u00b5\u0001\u0000\u0000\u0000\u00b3\u00b1\u0001\u0000\u0000\u0000\u00b3"+
		"\u00b4\u0001\u0000\u0000\u0000\u00b4:\u0001\u0000\u0000\u0000\u00b5\u00b3"+
		"\u0001\u0000\u0000\u0000\u00b6\u00b7\u0005=\u0000\u0000\u00b7<\u0001\u0000"+
		"\u0000\u0000\u0007\u0000\u0095\u009b\u009d\u00a3\u00ab\u00b3\u0001\u0006"+
		"\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}