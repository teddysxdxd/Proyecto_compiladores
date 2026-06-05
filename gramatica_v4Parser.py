# Generated from gramatica_v4.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,48,298,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        5,0,42,8,0,10,0,12,0,45,9,0,1,0,1,0,5,0,49,8,0,10,0,12,0,52,9,0,
        1,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,78,8,2,1,3,1,3,1,3,1,3,3,3,84,
        8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,95,8,3,10,3,12,3,98,
        9,3,1,3,1,3,1,3,1,3,3,3,104,8,3,1,4,1,4,1,4,1,4,1,5,1,5,3,5,112,
        8,5,1,6,1,6,1,6,1,6,3,6,118,8,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,
        5,7,128,8,7,10,7,12,7,131,9,7,1,8,1,8,1,8,1,8,5,8,137,8,8,10,8,12,
        8,140,9,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,5,12,165,
        8,12,10,12,12,12,168,9,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,3,13,179,8,13,1,14,1,14,1,14,1,14,1,14,1,14,4,14,187,8,14,11,
        14,12,14,188,1,14,3,14,192,8,14,1,14,1,14,1,15,1,15,1,15,1,15,5,
        15,200,8,15,10,15,12,15,203,9,15,1,16,1,16,1,16,5,16,208,8,16,10,
        16,12,16,211,9,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,5,17,220,8,
        17,10,17,12,17,223,9,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,244,
        8,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,5,18,254,8,18,10,18,
        12,18,257,9,18,3,18,259,8,18,1,18,1,18,1,18,1,18,3,18,265,8,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,5,18,285,8,18,10,18,12,18,288,9,18,1,19,1,
        19,1,19,5,19,293,8,19,10,19,12,19,296,9,19,1,19,0,1,36,20,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,0,4,1,0,26,28,1,
        0,29,30,1,0,31,37,1,0,38,39,326,0,43,1,0,0,0,2,56,1,0,0,0,4,77,1,
        0,0,0,6,103,1,0,0,0,8,105,1,0,0,0,10,109,1,0,0,0,12,113,1,0,0,0,
        14,122,1,0,0,0,16,132,1,0,0,0,18,143,1,0,0,0,20,146,1,0,0,0,22,152,
        1,0,0,0,24,162,1,0,0,0,26,171,1,0,0,0,28,180,1,0,0,0,30,195,1,0,
        0,0,32,204,1,0,0,0,34,212,1,0,0,0,36,264,1,0,0,0,38,289,1,0,0,0,
        40,42,3,2,1,0,41,40,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,
        0,0,0,44,46,1,0,0,0,45,43,1,0,0,0,46,50,5,4,0,0,47,49,3,4,2,0,48,
        47,1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,53,1,0,0,
        0,52,50,1,0,0,0,53,54,5,5,0,0,54,55,5,0,0,1,55,1,1,0,0,0,56,57,5,
        2,0,0,57,58,5,47,0,0,58,3,1,0,0,0,59,78,3,6,3,0,60,78,3,8,4,0,61,
        62,5,6,0,0,62,63,5,20,0,0,63,64,3,36,18,0,64,65,5,21,0,0,65,78,1,
        0,0,0,66,78,3,28,14,0,67,78,3,26,13,0,68,78,3,20,10,0,69,78,3,22,
        11,0,70,78,3,10,5,0,71,78,3,12,6,0,72,78,3,16,8,0,73,78,3,36,18,
        0,74,78,5,16,0,0,75,78,5,17,0,0,76,78,3,24,12,0,77,59,1,0,0,0,77,
        60,1,0,0,0,77,61,1,0,0,0,77,66,1,0,0,0,77,67,1,0,0,0,77,68,1,0,0,
        0,77,69,1,0,0,0,77,70,1,0,0,0,77,71,1,0,0,0,77,72,1,0,0,0,77,73,
        1,0,0,0,77,74,1,0,0,0,77,75,1,0,0,0,77,76,1,0,0,0,78,5,1,0,0,0,79,
        80,5,3,0,0,80,83,5,47,0,0,81,82,5,48,0,0,82,84,3,36,18,0,83,81,1,
        0,0,0,83,84,1,0,0,0,84,104,1,0,0,0,85,86,5,3,0,0,86,87,5,22,0,0,
        87,88,5,23,0,0,88,89,5,47,0,0,89,90,5,48,0,0,90,91,5,22,0,0,91,96,
        3,36,18,0,92,93,5,40,0,0,93,95,3,36,18,0,94,92,1,0,0,0,95,98,1,0,
        0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,99,1,0,0,0,98,96,1,0,0,0,99,100,
        5,23,0,0,100,104,1,0,0,0,101,102,5,47,0,0,102,104,5,47,0,0,103,79,
        1,0,0,0,103,85,1,0,0,0,103,101,1,0,0,0,104,7,1,0,0,0,105,106,3,34,
        17,0,106,107,5,48,0,0,107,108,3,36,18,0,108,9,1,0,0,0,109,111,5,
        19,0,0,110,112,3,36,18,0,111,110,1,0,0,0,111,112,1,0,0,0,112,11,
        1,0,0,0,113,114,5,3,0,0,114,115,5,47,0,0,115,117,5,20,0,0,116,118,
        3,14,7,0,117,116,1,0,0,0,117,118,1,0,0,0,118,119,1,0,0,0,119,120,
        5,21,0,0,120,121,3,24,12,0,121,13,1,0,0,0,122,123,5,3,0,0,123,129,
        5,47,0,0,124,125,5,40,0,0,125,126,5,3,0,0,126,128,5,47,0,0,127,124,
        1,0,0,0,128,131,1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,0,130,15,1,
        0,0,0,131,129,1,0,0,0,132,133,5,14,0,0,133,134,5,47,0,0,134,138,
        5,7,0,0,135,137,3,18,9,0,136,135,1,0,0,0,137,140,1,0,0,0,138,136,
        1,0,0,0,138,139,1,0,0,0,139,141,1,0,0,0,140,138,1,0,0,0,141,142,
        5,8,0,0,142,17,1,0,0,0,143,144,5,3,0,0,144,145,5,47,0,0,145,19,1,
        0,0,0,146,147,5,15,0,0,147,148,5,20,0,0,148,149,3,36,18,0,149,150,
        5,21,0,0,150,151,3,24,12,0,151,21,1,0,0,0,152,153,5,18,0,0,153,154,
        5,20,0,0,154,155,3,8,4,0,155,156,5,1,0,0,156,157,3,36,18,0,157,158,
        5,1,0,0,158,159,3,8,4,0,159,160,5,21,0,0,160,161,3,24,12,0,161,23,
        1,0,0,0,162,166,5,7,0,0,163,165,3,4,2,0,164,163,1,0,0,0,165,168,
        1,0,0,0,166,164,1,0,0,0,166,167,1,0,0,0,167,169,1,0,0,0,168,166,
        1,0,0,0,169,170,5,8,0,0,170,25,1,0,0,0,171,172,5,9,0,0,172,173,5,
        20,0,0,173,174,3,36,18,0,174,175,5,21,0,0,175,178,3,24,12,0,176,
        177,5,10,0,0,177,179,3,24,12,0,178,176,1,0,0,0,178,179,1,0,0,0,179,
        27,1,0,0,0,180,181,5,11,0,0,181,182,5,20,0,0,182,183,3,36,18,0,183,
        184,5,21,0,0,184,186,5,7,0,0,185,187,3,30,15,0,186,185,1,0,0,0,187,
        188,1,0,0,0,188,186,1,0,0,0,188,189,1,0,0,0,189,191,1,0,0,0,190,
        192,3,32,16,0,191,190,1,0,0,0,191,192,1,0,0,0,192,193,1,0,0,0,193,
        194,5,8,0,0,194,29,1,0,0,0,195,196,5,12,0,0,196,197,3,36,18,0,197,
        201,5,42,0,0,198,200,3,4,2,0,199,198,1,0,0,0,200,203,1,0,0,0,201,
        199,1,0,0,0,201,202,1,0,0,0,202,31,1,0,0,0,203,201,1,0,0,0,204,205,
        5,13,0,0,205,209,5,42,0,0,206,208,3,4,2,0,207,206,1,0,0,0,208,211,
        1,0,0,0,209,207,1,0,0,0,209,210,1,0,0,0,210,33,1,0,0,0,211,209,1,
        0,0,0,212,221,5,47,0,0,213,214,5,41,0,0,214,220,5,47,0,0,215,216,
        5,22,0,0,216,217,3,36,18,0,217,218,5,23,0,0,218,220,1,0,0,0,219,
        213,1,0,0,0,219,215,1,0,0,0,220,223,1,0,0,0,221,219,1,0,0,0,221,
        222,1,0,0,0,222,35,1,0,0,0,223,221,1,0,0,0,224,225,6,18,-1,0,225,
        226,5,20,0,0,226,227,5,3,0,0,227,228,5,21,0,0,228,265,3,36,18,15,
        229,230,5,20,0,0,230,231,3,36,18,0,231,232,5,21,0,0,232,265,1,0,
        0,0,233,234,5,22,0,0,234,235,3,36,18,0,235,236,5,23,0,0,236,265,
        1,0,0,0,237,265,5,44,0,0,238,265,5,45,0,0,239,265,5,24,0,0,240,241,
        5,47,0,0,241,243,5,20,0,0,242,244,3,38,19,0,243,242,1,0,0,0,243,
        244,1,0,0,0,244,245,1,0,0,0,245,265,5,21,0,0,246,247,5,47,0,0,247,
        248,5,41,0,0,248,249,5,47,0,0,249,258,5,20,0,0,250,255,3,36,18,0,
        251,252,5,40,0,0,252,254,3,36,18,0,253,251,1,0,0,0,254,257,1,0,0,
        0,255,253,1,0,0,0,255,256,1,0,0,0,256,259,1,0,0,0,257,255,1,0,0,
        0,258,250,1,0,0,0,258,259,1,0,0,0,259,260,1,0,0,0,260,265,5,21,0,
        0,261,265,3,34,17,0,262,263,5,25,0,0,263,265,3,36,18,6,264,224,1,
        0,0,0,264,229,1,0,0,0,264,233,1,0,0,0,264,237,1,0,0,0,264,238,1,
        0,0,0,264,239,1,0,0,0,264,240,1,0,0,0,264,246,1,0,0,0,264,261,1,
        0,0,0,264,262,1,0,0,0,265,286,1,0,0,0,266,267,10,5,0,0,267,268,7,
        0,0,0,268,285,3,36,18,6,269,270,10,4,0,0,270,271,7,1,0,0,271,285,
        3,36,18,5,272,273,10,3,0,0,273,274,7,2,0,0,274,285,3,36,18,4,275,
        276,10,2,0,0,276,277,7,3,0,0,277,285,3,36,18,3,278,279,10,1,0,0,
        279,280,5,43,0,0,280,281,3,36,18,0,281,282,5,42,0,0,282,283,3,36,
        18,2,283,285,1,0,0,0,284,266,1,0,0,0,284,269,1,0,0,0,284,272,1,0,
        0,0,284,275,1,0,0,0,284,278,1,0,0,0,285,288,1,0,0,0,286,284,1,0,
        0,0,286,287,1,0,0,0,287,37,1,0,0,0,288,286,1,0,0,0,289,294,3,36,
        18,0,290,291,5,40,0,0,291,293,3,36,18,0,292,290,1,0,0,0,293,296,
        1,0,0,0,294,292,1,0,0,0,294,295,1,0,0,0,295,39,1,0,0,0,296,294,1,
        0,0,0,25,43,50,77,83,96,103,111,117,129,138,166,178,188,191,201,
        209,219,221,243,255,258,264,284,286,294
    ]

class gramatica_v4Parser ( Parser ):

    grammarFileName = "gramatica_v4.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'import'", "<INVALID>", "'Program'", 
                     "'End_Program'", "'print'", "'{'", "'}'", "'simon'", 
                     "'sinel'", "'switch'", "'case'", "'default'", "'struct'", 
                     "'while'", "'break'", "'continue'", "'for'", "'return'", 
                     "'('", "')'", "'['", "']'", "<INVALID>", "'!'", "'*'", 
                     "'%'", "'/'", "'+'", "'-'", "'=='", "'!='", "'<>'", 
                     "'<'", "'>'", "'<='", "'>='", "'&&'", "'||'", "','", 
                     "'.'", "':'", "'?'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "IMPORT", "TIPO", "INICIOPROGRAMA", 
                      "FINPROGRAMA", "PRINTI", "BLOCKI", "BLOCKF", "IFINICIO", 
                      "ELSE", "SWITCH", "CASE", "DEFAULT", "STRUCT", "WHILE", 
                      "BREAK", "CONTINUE", "FOR", "RETURN", "PARENTESISI", 
                      "PARENTESISD", "CORCHI", "CORCHD", "BOOLEANO", "NOTLOGICO", 
                      "MULT", "MOD", "DIV", "SUM", "REST", "IGUALA", "DIFERENTEA", 
                      "DIFERENTEA2", "MENORQUE", "MAYORQUE", "MENORIGUAL", 
                      "MAYORIGUAL", "AND", "OR", "COMA", "PUNTO", "COLON", 
                      "QUESTION", "NUMERO", "STRING", "WS", "ID", "ASSIGN" ]

    RULE_archivo = 0
    RULE_importStatement = 1
    RULE_instruccion = 2
    RULE_declaracion = 3
    RULE_asignacion = 4
    RULE_returnStmt = 5
    RULE_funcionDecl = 6
    RULE_params = 7
    RULE_structDecl = 8
    RULE_structFieldDecl = 9
    RULE_whileStatement = 10
    RULE_forStatement = 11
    RULE_block = 12
    RULE_ifStatement = 13
    RULE_switchStatement = 14
    RULE_caseClause = 15
    RULE_defaultClause = 16
    RULE_lvalue = 17
    RULE_expresion = 18
    RULE_args = 19

    ruleNames =  [ "archivo", "importStatement", "instruccion", "declaracion", 
                   "asignacion", "returnStmt", "funcionDecl", "params", 
                   "structDecl", "structFieldDecl", "whileStatement", "forStatement", 
                   "block", "ifStatement", "switchStatement", "caseClause", 
                   "defaultClause", "lvalue", "expresion", "args" ]

    EOF = Token.EOF
    T__0=1
    IMPORT=2
    TIPO=3
    INICIOPROGRAMA=4
    FINPROGRAMA=5
    PRINTI=6
    BLOCKI=7
    BLOCKF=8
    IFINICIO=9
    ELSE=10
    SWITCH=11
    CASE=12
    DEFAULT=13
    STRUCT=14
    WHILE=15
    BREAK=16
    CONTINUE=17
    FOR=18
    RETURN=19
    PARENTESISI=20
    PARENTESISD=21
    CORCHI=22
    CORCHD=23
    BOOLEANO=24
    NOTLOGICO=25
    MULT=26
    MOD=27
    DIV=28
    SUM=29
    REST=30
    IGUALA=31
    DIFERENTEA=32
    DIFERENTEA2=33
    MENORQUE=34
    MAYORQUE=35
    MENORIGUAL=36
    MAYORIGUAL=37
    AND=38
    OR=39
    COMA=40
    PUNTO=41
    COLON=42
    QUESTION=43
    NUMERO=44
    STRING=45
    WS=46
    ID=47
    ASSIGN=48

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ArchivoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INICIOPROGRAMA(self):
            return self.getToken(gramatica_v4Parser.INICIOPROGRAMA, 0)

        def FINPROGRAMA(self):
            return self.getToken(gramatica_v4Parser.FINPROGRAMA, 0)

        def EOF(self):
            return self.getToken(gramatica_v4Parser.EOF, 0)

        def importStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.ImportStatementContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.ImportStatementContext,i)


        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.InstruccionContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.InstruccionContext,i)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_archivo

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArchivo" ):
                return visitor.visitArchivo(self)
            else:
                return visitor.visitChildren(self)




    def archivo(self):

        localctx = gramatica_v4Parser.ArchivoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_archivo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 40
                self.importStatement()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46
            self.match(gramatica_v4Parser.INICIOPROGRAMA)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 193514103098056) != 0):
                self.state = 47
                self.instruccion()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 53
            self.match(gramatica_v4Parser.FINPROGRAMA)
            self.state = 54
            self.match(gramatica_v4Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(gramatica_v4Parser.IMPORT, 0)

        def ID(self):
            return self.getToken(gramatica_v4Parser.ID, 0)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_importStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportStatement" ):
                return visitor.visitImportStatement(self)
            else:
                return visitor.visitChildren(self)




    def importStatement(self):

        localctx = gramatica_v4Parser.ImportStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_importStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(gramatica_v4Parser.IMPORT)
            self.state = 57
            self.match(gramatica_v4Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_instruccion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class InstruccionSwitchContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def switchStatement(self):
            return self.getTypedRuleContext(gramatica_v4Parser.SwitchStatementContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccionSwitch" ):
                return visitor.visitInstruccionSwitch(self)
            else:
                return visitor.visitChildren(self)


    class InstruccionExpresionContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExpresionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccionExpresion" ):
                return visitor.visitInstruccionExpresion(self)
            else:
                return visitor.visitChildren(self)


    class InstruccionForContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def forStatement(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ForStatementContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccionFor" ):
                return visitor.visitInstruccionFor(self)
            else:
                return visitor.visitChildren(self)


    class EjecutarPrintContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRINTI(self):
            return self.getToken(gramatica_v4Parser.PRINTI, 0)
        def PARENTESISI(self):
            return self.getToken(gramatica_v4Parser.PARENTESISI, 0)
        def expresion(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExpresionContext,0)

        def PARENTESISD(self):
            return self.getToken(gramatica_v4Parser.PARENTESISD, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEjecutarPrint" ):
                return visitor.visitEjecutarPrint(self)
            else:
                return visitor.visitChildren(self)


    class InstruccionWhileContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def whileStatement(self):
            return self.getTypedRuleContext(gramatica_v4Parser.WhileStatementContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccionWhile" ):
                return visitor.visitInstruccionWhile(self)
            else:
                return visitor.visitChildren(self)


    class InstruccionReturnContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def returnStmt(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ReturnStmtContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccionReturn" ):
                return visitor.visitInstruccionReturn(self)
            else:
                return visitor.visitChildren(self)


    class InstruccionBloqueContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def block(self):
            return self.getTypedRuleContext(gramatica_v4Parser.BlockContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccionBloque" ):
                return visitor.visitInstruccionBloque(self)
            else:
                return visitor.visitChildren(self)


    class InstruccionIfContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ifStatement(self):
            return self.getTypedRuleContext(gramatica_v4Parser.IfStatementContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccionIf" ):
                return visitor.visitInstruccionIf(self)
            else:
                return visitor.visitChildren(self)


    class ContinueStmtContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CONTINUE(self):
            return self.getToken(gramatica_v4Parser.CONTINUE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStmt" ):
                return visitor.visitContinueStmt(self)
            else:
                return visitor.visitChildren(self)


    class EjecutarAsignacionContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def asignacion(self):
            return self.getTypedRuleContext(gramatica_v4Parser.AsignacionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEjecutarAsignacion" ):
                return visitor.visitEjecutarAsignacion(self)
            else:
                return visitor.visitChildren(self)


    class BreakStmtContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BREAK(self):
            return self.getToken(gramatica_v4Parser.BREAK, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStmt" ):
                return visitor.visitBreakStmt(self)
            else:
                return visitor.visitChildren(self)


    class InstruccionDeclaracionContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def declaracion(self):
            return self.getTypedRuleContext(gramatica_v4Parser.DeclaracionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccionDeclaracion" ):
                return visitor.visitInstruccionDeclaracion(self)
            else:
                return visitor.visitChildren(self)


    class InstruccionFuncionContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def funcionDecl(self):
            return self.getTypedRuleContext(gramatica_v4Parser.FuncionDeclContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccionFuncion" ):
                return visitor.visitInstruccionFuncion(self)
            else:
                return visitor.visitChildren(self)


    class InstruccionStructContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def structDecl(self):
            return self.getTypedRuleContext(gramatica_v4Parser.StructDeclContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccionStruct" ):
                return visitor.visitInstruccionStruct(self)
            else:
                return visitor.visitChildren(self)



    def instruccion(self):

        localctx = gramatica_v4Parser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instruccion)
        try:
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = gramatica_v4Parser.InstruccionDeclaracionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.declaracion()
                pass

            elif la_ == 2:
                localctx = gramatica_v4Parser.EjecutarAsignacionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.asignacion()
                pass

            elif la_ == 3:
                localctx = gramatica_v4Parser.EjecutarPrintContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.match(gramatica_v4Parser.PRINTI)
                self.state = 62
                self.match(gramatica_v4Parser.PARENTESISI)
                self.state = 63
                self.expresion(0)
                self.state = 64
                self.match(gramatica_v4Parser.PARENTESISD)
                pass

            elif la_ == 4:
                localctx = gramatica_v4Parser.InstruccionSwitchContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 66
                self.switchStatement()
                pass

            elif la_ == 5:
                localctx = gramatica_v4Parser.InstruccionIfContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 67
                self.ifStatement()
                pass

            elif la_ == 6:
                localctx = gramatica_v4Parser.InstruccionWhileContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 68
                self.whileStatement()
                pass

            elif la_ == 7:
                localctx = gramatica_v4Parser.InstruccionForContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 69
                self.forStatement()
                pass

            elif la_ == 8:
                localctx = gramatica_v4Parser.InstruccionReturnContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 70
                self.returnStmt()
                pass

            elif la_ == 9:
                localctx = gramatica_v4Parser.InstruccionFuncionContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 71
                self.funcionDecl()
                pass

            elif la_ == 10:
                localctx = gramatica_v4Parser.InstruccionStructContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 72
                self.structDecl()
                pass

            elif la_ == 11:
                localctx = gramatica_v4Parser.InstruccionExpresionContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 73
                self.expresion(0)
                pass

            elif la_ == 12:
                localctx = gramatica_v4Parser.BreakStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 74
                self.match(gramatica_v4Parser.BREAK)
                pass

            elif la_ == 13:
                localctx = gramatica_v4Parser.ContinueStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 75
                self.match(gramatica_v4Parser.CONTINUE)
                pass

            elif la_ == 14:
                localctx = gramatica_v4Parser.InstruccionBloqueContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 76
                self.block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIPO(self):
            return self.getToken(gramatica_v4Parser.TIPO, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v4Parser.ID)
            else:
                return self.getToken(gramatica_v4Parser.ID, i)

        def ASSIGN(self):
            return self.getToken(gramatica_v4Parser.ASSIGN, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.ExpresionContext,i)


        def CORCHI(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v4Parser.CORCHI)
            else:
                return self.getToken(gramatica_v4Parser.CORCHI, i)

        def CORCHD(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v4Parser.CORCHD)
            else:
                return self.getToken(gramatica_v4Parser.CORCHD, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v4Parser.COMA)
            else:
                return self.getToken(gramatica_v4Parser.COMA, i)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_declaracion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = gramatica_v4Parser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaracion)
        self._la = 0 # Token type
        try:
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.match(gramatica_v4Parser.TIPO)
                self.state = 80
                self.match(gramatica_v4Parser.ID)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==48:
                    self.state = 81
                    self.match(gramatica_v4Parser.ASSIGN)
                    self.state = 82
                    self.expresion(0)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.match(gramatica_v4Parser.TIPO)
                self.state = 86
                self.match(gramatica_v4Parser.CORCHI)
                self.state = 87
                self.match(gramatica_v4Parser.CORCHD)
                self.state = 88
                self.match(gramatica_v4Parser.ID)
                self.state = 89
                self.match(gramatica_v4Parser.ASSIGN)
                self.state = 90
                self.match(gramatica_v4Parser.CORCHI)
                self.state = 91
                self.expresion(0)
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==40:
                    self.state = 92
                    self.match(gramatica_v4Parser.COMA)
                    self.state = 93
                    self.expresion(0)
                    self.state = 98
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 99
                self.match(gramatica_v4Parser.CORCHD)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 101
                self.match(gramatica_v4Parser.ID)
                self.state = 102
                self.match(gramatica_v4Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvalue(self):
            return self.getTypedRuleContext(gramatica_v4Parser.LvalueContext,0)


        def ASSIGN(self):
            return self.getToken(gramatica_v4Parser.ASSIGN, 0)

        def expresion(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExpresionContext,0)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_asignacion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = gramatica_v4Parser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.lvalue()
            self.state = 106
            self.match(gramatica_v4Parser.ASSIGN)
            self.state = 107
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(gramatica_v4Parser.RETURN, 0)

        def expresion(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExpresionContext,0)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_returnStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = gramatica_v4Parser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(gramatica_v4Parser.RETURN)
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 110
                self.expresion(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIPO(self):
            return self.getToken(gramatica_v4Parser.TIPO, 0)

        def ID(self):
            return self.getToken(gramatica_v4Parser.ID, 0)

        def PARENTESISI(self):
            return self.getToken(gramatica_v4Parser.PARENTESISI, 0)

        def PARENTESISD(self):
            return self.getToken(gramatica_v4Parser.PARENTESISD, 0)

        def block(self):
            return self.getTypedRuleContext(gramatica_v4Parser.BlockContext,0)


        def params(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ParamsContext,0)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_funcionDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncionDecl" ):
                return visitor.visitFuncionDecl(self)
            else:
                return visitor.visitChildren(self)




    def funcionDecl(self):

        localctx = gramatica_v4Parser.FuncionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(gramatica_v4Parser.TIPO)
            self.state = 114
            self.match(gramatica_v4Parser.ID)
            self.state = 115
            self.match(gramatica_v4Parser.PARENTESISI)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 116
                self.params()


            self.state = 119
            self.match(gramatica_v4Parser.PARENTESISD)
            self.state = 120
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIPO(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v4Parser.TIPO)
            else:
                return self.getToken(gramatica_v4Parser.TIPO, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v4Parser.ID)
            else:
                return self.getToken(gramatica_v4Parser.ID, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v4Parser.COMA)
            else:
                return self.getToken(gramatica_v4Parser.COMA, i)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = gramatica_v4Parser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(gramatica_v4Parser.TIPO)
            self.state = 123
            self.match(gramatica_v4Parser.ID)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 124
                self.match(gramatica_v4Parser.COMA)
                self.state = 125
                self.match(gramatica_v4Parser.TIPO)
                self.state = 126
                self.match(gramatica_v4Parser.ID)
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(gramatica_v4Parser.STRUCT, 0)

        def ID(self):
            return self.getToken(gramatica_v4Parser.ID, 0)

        def BLOCKI(self):
            return self.getToken(gramatica_v4Parser.BLOCKI, 0)

        def BLOCKF(self):
            return self.getToken(gramatica_v4Parser.BLOCKF, 0)

        def structFieldDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.StructFieldDeclContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.StructFieldDeclContext,i)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_structDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructDecl" ):
                return visitor.visitStructDecl(self)
            else:
                return visitor.visitChildren(self)




    def structDecl(self):

        localctx = gramatica_v4Parser.StructDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_structDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(gramatica_v4Parser.STRUCT)
            self.state = 133
            self.match(gramatica_v4Parser.ID)
            self.state = 134
            self.match(gramatica_v4Parser.BLOCKI)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 135
                self.structFieldDecl()
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 141
            self.match(gramatica_v4Parser.BLOCKF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructFieldDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIPO(self):
            return self.getToken(gramatica_v4Parser.TIPO, 0)

        def ID(self):
            return self.getToken(gramatica_v4Parser.ID, 0)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_structFieldDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructFieldDecl" ):
                return visitor.visitStructFieldDecl(self)
            else:
                return visitor.visitChildren(self)




    def structFieldDecl(self):

        localctx = gramatica_v4Parser.StructFieldDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_structFieldDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(gramatica_v4Parser.TIPO)
            self.state = 144
            self.match(gramatica_v4Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(gramatica_v4Parser.WHILE, 0)

        def PARENTESISI(self):
            return self.getToken(gramatica_v4Parser.PARENTESISI, 0)

        def expresion(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExpresionContext,0)


        def PARENTESISD(self):
            return self.getToken(gramatica_v4Parser.PARENTESISD, 0)

        def block(self):
            return self.getTypedRuleContext(gramatica_v4Parser.BlockContext,0)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_whileStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = gramatica_v4Parser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(gramatica_v4Parser.WHILE)
            self.state = 147
            self.match(gramatica_v4Parser.PARENTESISI)
            self.state = 148
            self.expresion(0)
            self.state = 149
            self.match(gramatica_v4Parser.PARENTESISD)
            self.state = 150
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(gramatica_v4Parser.FOR, 0)

        def PARENTESISI(self):
            return self.getToken(gramatica_v4Parser.PARENTESISI, 0)

        def asignacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.AsignacionContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.AsignacionContext,i)


        def expresion(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExpresionContext,0)


        def PARENTESISD(self):
            return self.getToken(gramatica_v4Parser.PARENTESISD, 0)

        def block(self):
            return self.getTypedRuleContext(gramatica_v4Parser.BlockContext,0)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_forStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = gramatica_v4Parser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(gramatica_v4Parser.FOR)
            self.state = 153
            self.match(gramatica_v4Parser.PARENTESISI)
            self.state = 154
            self.asignacion()
            self.state = 155
            self.match(gramatica_v4Parser.T__0)
            self.state = 156
            self.expresion(0)
            self.state = 157
            self.match(gramatica_v4Parser.T__0)
            self.state = 158
            self.asignacion()
            self.state = 159
            self.match(gramatica_v4Parser.PARENTESISD)
            self.state = 160
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BLOCKI(self):
            return self.getToken(gramatica_v4Parser.BLOCKI, 0)

        def BLOCKF(self):
            return self.getToken(gramatica_v4Parser.BLOCKF, 0)

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.InstruccionContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.InstruccionContext,i)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = gramatica_v4Parser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(gramatica_v4Parser.BLOCKI)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 193514103098056) != 0):
                self.state = 163
                self.instruccion()
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 169
            self.match(gramatica_v4Parser.BLOCKF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IFINICIO(self):
            return self.getToken(gramatica_v4Parser.IFINICIO, 0)

        def PARENTESISI(self):
            return self.getToken(gramatica_v4Parser.PARENTESISI, 0)

        def expresion(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExpresionContext,0)


        def PARENTESISD(self):
            return self.getToken(gramatica_v4Parser.PARENTESISD, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.BlockContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.BlockContext,i)


        def ELSE(self):
            return self.getToken(gramatica_v4Parser.ELSE, 0)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_ifStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = gramatica_v4Parser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(gramatica_v4Parser.IFINICIO)
            self.state = 172
            self.match(gramatica_v4Parser.PARENTESISI)
            self.state = 173
            self.expresion(0)
            self.state = 174
            self.match(gramatica_v4Parser.PARENTESISD)
            self.state = 175
            self.block()
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 176
                self.match(gramatica_v4Parser.ELSE)
                self.state = 177
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(gramatica_v4Parser.SWITCH, 0)

        def PARENTESISI(self):
            return self.getToken(gramatica_v4Parser.PARENTESISI, 0)

        def expresion(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExpresionContext,0)


        def PARENTESISD(self):
            return self.getToken(gramatica_v4Parser.PARENTESISD, 0)

        def BLOCKI(self):
            return self.getToken(gramatica_v4Parser.BLOCKI, 0)

        def BLOCKF(self):
            return self.getToken(gramatica_v4Parser.BLOCKF, 0)

        def caseClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.CaseClauseContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.CaseClauseContext,i)


        def defaultClause(self):
            return self.getTypedRuleContext(gramatica_v4Parser.DefaultClauseContext,0)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_switchStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchStatement" ):
                return visitor.visitSwitchStatement(self)
            else:
                return visitor.visitChildren(self)




    def switchStatement(self):

        localctx = gramatica_v4Parser.SwitchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_switchStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(gramatica_v4Parser.SWITCH)
            self.state = 181
            self.match(gramatica_v4Parser.PARENTESISI)
            self.state = 182
            self.expresion(0)
            self.state = 183
            self.match(gramatica_v4Parser.PARENTESISD)
            self.state = 184
            self.match(gramatica_v4Parser.BLOCKI)
            self.state = 186 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 185
                self.caseClause()
                self.state = 188 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==12):
                    break

            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 190
                self.defaultClause()


            self.state = 193
            self.match(gramatica_v4Parser.BLOCKF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(gramatica_v4Parser.CASE, 0)

        def expresion(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExpresionContext,0)


        def COLON(self):
            return self.getToken(gramatica_v4Parser.COLON, 0)

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.InstruccionContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.InstruccionContext,i)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_caseClause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseClause" ):
                return visitor.visitCaseClause(self)
            else:
                return visitor.visitChildren(self)




    def caseClause(self):

        localctx = gramatica_v4Parser.CaseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_caseClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(gramatica_v4Parser.CASE)
            self.state = 196
            self.expresion(0)
            self.state = 197
            self.match(gramatica_v4Parser.COLON)
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 193514103098056) != 0):
                self.state = 198
                self.instruccion()
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT(self):
            return self.getToken(gramatica_v4Parser.DEFAULT, 0)

        def COLON(self):
            return self.getToken(gramatica_v4Parser.COLON, 0)

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.InstruccionContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.InstruccionContext,i)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_defaultClause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefaultClause" ):
                return visitor.visitDefaultClause(self)
            else:
                return visitor.visitChildren(self)




    def defaultClause(self):

        localctx = gramatica_v4Parser.DefaultClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_defaultClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(gramatica_v4Parser.DEFAULT)
            self.state = 205
            self.match(gramatica_v4Parser.COLON)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 193514103098056) != 0):
                self.state = 206
                self.instruccion()
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v4Parser.ID)
            else:
                return self.getToken(gramatica_v4Parser.ID, i)

        def PUNTO(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v4Parser.PUNTO)
            else:
                return self.getToken(gramatica_v4Parser.PUNTO, i)

        def CORCHI(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v4Parser.CORCHI)
            else:
                return self.getToken(gramatica_v4Parser.CORCHI, i)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.ExpresionContext,i)


        def CORCHD(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v4Parser.CORCHD)
            else:
                return self.getToken(gramatica_v4Parser.CORCHD, i)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_lvalue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLvalue" ):
                return visitor.visitLvalue(self)
            else:
                return visitor.visitChildren(self)




    def lvalue(self):

        localctx = gramatica_v4Parser.LvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_lvalue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(gramatica_v4Parser.ID)
            self.state = 221
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 219
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [41]:
                        self.state = 213
                        self.match(gramatica_v4Parser.PUNTO)
                        self.state = 214
                        self.match(gramatica_v4Parser.ID)
                        pass
                    elif token in [22]:
                        self.state = 215
                        self.match(gramatica_v4Parser.CORCHI)
                        self.state = 216
                        self.expresion(0)
                        self.state = 217
                        self.match(gramatica_v4Parser.CORCHD)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 223
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_expresion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NumeroContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMERO(self):
            return self.getToken(gramatica_v4Parser.NUMERO, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)


    class CorchetesContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CORCHI(self):
            return self.getToken(gramatica_v4Parser.CORCHI, 0)
        def expresion(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExpresionContext,0)

        def CORCHD(self):
            return self.getToken(gramatica_v4Parser.CORCHD, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCorchetes" ):
                return visitor.visitCorchetes(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def lvalue(self):
            return self.getTypedRuleContext(gramatica_v4Parser.LvalueContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class CastExplicitoContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PARENTESISI(self):
            return self.getToken(gramatica_v4Parser.PARENTESISI, 0)
        def TIPO(self):
            return self.getToken(gramatica_v4Parser.TIPO, 0)
        def PARENTESISD(self):
            return self.getToken(gramatica_v4Parser.PARENTESISD, 0)
        def expresion(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExpresionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCastExplicito" ):
                return visitor.visitCastExplicito(self)
            else:
                return visitor.visitChildren(self)


    class ParentesisContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PARENTESISI(self):
            return self.getToken(gramatica_v4Parser.PARENTESISI, 0)
        def expresion(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExpresionContext,0)

        def PARENTESISD(self):
            return self.getToken(gramatica_v4Parser.PARENTESISD, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentesis" ):
                return visitor.visitParentesis(self)
            else:
                return visitor.visitChildren(self)


    class CadenaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(gramatica_v4Parser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCadena" ):
                return visitor.visitCadena(self)
            else:
                return visitor.visitChildren(self)


    class NotLogicoContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOTLOGICO(self):
            return self.getToken(gramatica_v4Parser.NOTLOGICO, 0)
        def expresion(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExpresionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotLogico" ):
                return visitor.visitNotLogico(self)
            else:
                return visitor.visitChildren(self)


    class MultiplicacionDivisisionModContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.ExpresionContext,i)

        def MULT(self):
            return self.getToken(gramatica_v4Parser.MULT, 0)
        def DIV(self):
            return self.getToken(gramatica_v4Parser.DIV, 0)
        def MOD(self):
            return self.getToken(gramatica_v4Parser.MOD, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicacionDivisisionMod" ):
                return visitor.visitMultiplicacionDivisisionMod(self)
            else:
                return visitor.visitChildren(self)


    class BooleanoContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOLEANO(self):
            return self.getToken(gramatica_v4Parser.BOOLEANO, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleano" ):
                return visitor.visitBooleano(self)
            else:
                return visitor.visitChildren(self)


    class SumaRestaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.ExpresionContext,i)

        def SUM(self):
            return self.getToken(gramatica_v4Parser.SUM, 0)
        def REST(self):
            return self.getToken(gramatica_v4Parser.REST, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumaResta" ):
                return visitor.visitSumaResta(self)
            else:
                return visitor.visitChildren(self)


    class AndOrLogicoContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.ExpresionContext,i)

        def AND(self):
            return self.getToken(gramatica_v4Parser.AND, 0)
        def OR(self):
            return self.getToken(gramatica_v4Parser.OR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndOrLogico" ):
                return visitor.visitAndOrLogico(self)
            else:
                return visitor.visitChildren(self)


    class RelacionalContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.ExpresionContext,i)

        def IGUALA(self):
            return self.getToken(gramatica_v4Parser.IGUALA, 0)
        def DIFERENTEA(self):
            return self.getToken(gramatica_v4Parser.DIFERENTEA, 0)
        def DIFERENTEA2(self):
            return self.getToken(gramatica_v4Parser.DIFERENTEA2, 0)
        def MENORQUE(self):
            return self.getToken(gramatica_v4Parser.MENORQUE, 0)
        def MAYORQUE(self):
            return self.getToken(gramatica_v4Parser.MAYORQUE, 0)
        def MENORIGUAL(self):
            return self.getToken(gramatica_v4Parser.MENORIGUAL, 0)
        def MAYORIGUAL(self):
            return self.getToken(gramatica_v4Parser.MAYORIGUAL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelacional" ):
                return visitor.visitRelacional(self)
            else:
                return visitor.visitChildren(self)


    class LlamadaFuncionContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(gramatica_v4Parser.ID, 0)
        def PARENTESISI(self):
            return self.getToken(gramatica_v4Parser.PARENTESISI, 0)
        def PARENTESISD(self):
            return self.getToken(gramatica_v4Parser.PARENTESISD, 0)
        def args(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ArgsContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamadaFuncion" ):
                return visitor.visitLlamadaFuncion(self)
            else:
                return visitor.visitChildren(self)


    class TernarioContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.ExpresionContext,i)

        def QUESTION(self):
            return self.getToken(gramatica_v4Parser.QUESTION, 0)
        def COLON(self):
            return self.getToken(gramatica_v4Parser.COLON, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTernario" ):
                return visitor.visitTernario(self)
            else:
                return visitor.visitChildren(self)


    class LlamadaModuloContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v4Parser.ID)
            else:
                return self.getToken(gramatica_v4Parser.ID, i)
        def PUNTO(self):
            return self.getToken(gramatica_v4Parser.PUNTO, 0)
        def PARENTESISI(self):
            return self.getToken(gramatica_v4Parser.PARENTESISI, 0)
        def PARENTESISD(self):
            return self.getToken(gramatica_v4Parser.PARENTESISD, 0)
        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.ExpresionContext,i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v4Parser.COMA)
            else:
                return self.getToken(gramatica_v4Parser.COMA, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamadaModulo" ):
                return visitor.visitLlamadaModulo(self)
            else:
                return visitor.visitChildren(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramatica_v4Parser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                localctx = gramatica_v4Parser.CastExplicitoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 225
                self.match(gramatica_v4Parser.PARENTESISI)
                self.state = 226
                self.match(gramatica_v4Parser.TIPO)
                self.state = 227
                self.match(gramatica_v4Parser.PARENTESISD)
                self.state = 228
                self.expresion(15)
                pass

            elif la_ == 2:
                localctx = gramatica_v4Parser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 229
                self.match(gramatica_v4Parser.PARENTESISI)
                self.state = 230
                self.expresion(0)
                self.state = 231
                self.match(gramatica_v4Parser.PARENTESISD)
                pass

            elif la_ == 3:
                localctx = gramatica_v4Parser.CorchetesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 233
                self.match(gramatica_v4Parser.CORCHI)
                self.state = 234
                self.expresion(0)
                self.state = 235
                self.match(gramatica_v4Parser.CORCHD)
                pass

            elif la_ == 4:
                localctx = gramatica_v4Parser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 237
                self.match(gramatica_v4Parser.NUMERO)
                pass

            elif la_ == 5:
                localctx = gramatica_v4Parser.CadenaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 238
                self.match(gramatica_v4Parser.STRING)
                pass

            elif la_ == 6:
                localctx = gramatica_v4Parser.BooleanoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 239
                self.match(gramatica_v4Parser.BOOLEANO)
                pass

            elif la_ == 7:
                localctx = gramatica_v4Parser.LlamadaFuncionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 240
                self.match(gramatica_v4Parser.ID)
                self.state = 241
                self.match(gramatica_v4Parser.PARENTESISI)
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 193514102063104) != 0):
                    self.state = 242
                    self.args()


                self.state = 245
                self.match(gramatica_v4Parser.PARENTESISD)
                pass

            elif la_ == 8:
                localctx = gramatica_v4Parser.LlamadaModuloContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 246
                self.match(gramatica_v4Parser.ID)
                self.state = 247
                self.match(gramatica_v4Parser.PUNTO)
                self.state = 248
                self.match(gramatica_v4Parser.ID)
                self.state = 249
                self.match(gramatica_v4Parser.PARENTESISI)
                self.state = 258
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 193514102063104) != 0):
                    self.state = 250
                    self.expresion(0)
                    self.state = 255
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==40:
                        self.state = 251
                        self.match(gramatica_v4Parser.COMA)
                        self.state = 252
                        self.expresion(0)
                        self.state = 257
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 260
                self.match(gramatica_v4Parser.PARENTESISD)
                pass

            elif la_ == 9:
                localctx = gramatica_v4Parser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 261
                self.lvalue()
                pass

            elif la_ == 10:
                localctx = gramatica_v4Parser.NotLogicoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 262
                self.match(gramatica_v4Parser.NOTLOGICO)
                self.state = 263
                self.expresion(6)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 286
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 284
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = gramatica_v4Parser.MultiplicacionDivisisionModContext(self, gramatica_v4Parser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 266
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 267
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 268
                        self.expresion(6)
                        pass

                    elif la_ == 2:
                        localctx = gramatica_v4Parser.SumaRestaContext(self, gramatica_v4Parser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 269
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 270
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==29 or _la==30):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 271
                        self.expresion(5)
                        pass

                    elif la_ == 3:
                        localctx = gramatica_v4Parser.RelacionalContext(self, gramatica_v4Parser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 272
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 273
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 272730423296) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 274
                        self.expresion(4)
                        pass

                    elif la_ == 4:
                        localctx = gramatica_v4Parser.AndOrLogicoContext(self, gramatica_v4Parser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 275
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 276
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==38 or _la==39):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 277
                        self.expresion(3)
                        pass

                    elif la_ == 5:
                        localctx = gramatica_v4Parser.TernarioContext(self, gramatica_v4Parser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 278
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 279
                        self.match(gramatica_v4Parser.QUESTION)
                        self.state = 280
                        self.expresion(0)
                        self.state = 281
                        self.match(gramatica_v4Parser.COLON)
                        self.state = 282
                        self.expresion(2)
                        pass

             
                self.state = 288
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.ExpresionContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v4Parser.COMA)
            else:
                return self.getToken(gramatica_v4Parser.COMA, i)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_args

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = gramatica_v4Parser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.expresion(0)
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 290
                self.match(gramatica_v4Parser.COMA)
                self.state = 291
                self.expresion(0)
                self.state = 296
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[18] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         




