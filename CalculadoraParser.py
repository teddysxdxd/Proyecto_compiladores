# Generated from Calculadora.g4 by ANTLR 4.13.1
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
        4,1,25,77,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,5,0,13,
        8,0,10,0,12,0,16,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,
        28,8,1,1,2,1,2,1,2,5,2,33,8,2,10,2,12,2,36,9,2,1,2,1,2,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,3,3,47,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        3,4,58,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,72,
        8,4,10,4,12,4,75,9,4,1,4,0,1,8,5,0,2,4,6,8,0,4,1,0,9,10,1,0,11,12,
        1,0,13,19,1,0,20,21,86,0,14,1,0,0,0,2,27,1,0,0,0,4,29,1,0,0,0,6,
        39,1,0,0,0,8,57,1,0,0,0,10,13,3,2,1,0,11,13,5,24,0,0,12,10,1,0,0,
        0,12,11,1,0,0,0,13,16,1,0,0,0,14,12,1,0,0,0,14,15,1,0,0,0,15,17,
        1,0,0,0,16,14,1,0,0,0,17,18,5,0,0,1,18,1,1,0,0,0,19,28,3,8,4,0,20,
        21,5,1,0,0,21,22,5,2,0,0,22,23,3,8,4,0,23,24,5,3,0,0,24,28,1,0,0,
        0,25,28,3,6,3,0,26,28,3,4,2,0,27,19,1,0,0,0,27,20,1,0,0,0,27,25,
        1,0,0,0,27,26,1,0,0,0,28,3,1,0,0,0,29,34,5,4,0,0,30,33,3,2,1,0,31,
        33,5,24,0,0,32,30,1,0,0,0,32,31,1,0,0,0,33,36,1,0,0,0,34,32,1,0,
        0,0,34,35,1,0,0,0,35,37,1,0,0,0,36,34,1,0,0,0,37,38,5,5,0,0,38,5,
        1,0,0,0,39,40,5,6,0,0,40,41,5,2,0,0,41,42,3,8,4,0,42,43,5,3,0,0,
        43,46,3,4,2,0,44,45,5,7,0,0,45,47,3,4,2,0,46,44,1,0,0,0,46,47,1,
        0,0,0,47,7,1,0,0,0,48,49,6,4,-1,0,49,50,5,2,0,0,50,51,3,8,4,0,51,
        52,5,3,0,0,52,58,1,0,0,0,53,58,5,22,0,0,54,58,5,23,0,0,55,56,5,8,
        0,0,56,58,3,8,4,5,57,48,1,0,0,0,57,53,1,0,0,0,57,54,1,0,0,0,57,55,
        1,0,0,0,58,73,1,0,0,0,59,60,10,4,0,0,60,61,7,0,0,0,61,72,3,8,4,5,
        62,63,10,3,0,0,63,64,7,1,0,0,64,72,3,8,4,4,65,66,10,2,0,0,66,67,
        7,2,0,0,67,72,3,8,4,3,68,69,10,1,0,0,69,70,7,3,0,0,70,72,3,8,4,2,
        71,59,1,0,0,0,71,62,1,0,0,0,71,65,1,0,0,0,71,68,1,0,0,0,72,75,1,
        0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,9,1,0,0,0,75,73,1,0,0,0,9,12,
        14,27,32,34,46,57,71,73
    ]

class CalculadoraParser ( Parser ):

    grammarFileName = "Calculadora.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'('", "')'", "'{'", "'}'", 
                     "'simon'", "'sinel'", "'!'", "'*'", "'/'", "'+'", "'-'", 
                     "'=='", "'!='", "'<>'", "'<'", "'>'", "'<='", "'>='", 
                     "'&&'", "'||'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUMERO", "STRING", "NEWLINE", 
                      "WS" ]

    RULE_archivo = 0
    RULE_instruccion = 1
    RULE_block = 2
    RULE_ifStatement = 3
    RULE_expresion = 4

    ruleNames =  [ "archivo", "instruccion", "block", "ifStatement", "expresion" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    NUMERO=22
    STRING=23
    NEWLINE=24
    WS=25

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

        def EOF(self):
            return self.getToken(CalculadoraParser.EOF, 0)

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.InstruccionContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(CalculadoraParser.NEWLINE)
            else:
                return self.getToken(CalculadoraParser.NEWLINE, i)

        def getRuleIndex(self):
            return CalculadoraParser.RULE_archivo

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArchivo" ):
                return visitor.visitArchivo(self)
            else:
                return visitor.visitChildren(self)




    def archivo(self):

        localctx = CalculadoraParser.ArchivoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_archivo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 29360470) != 0):
                self.state = 12
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 2, 4, 6, 8, 22, 23]:
                    self.state = 10
                    self.instruccion()
                    pass
                elif token in [24]:
                    self.state = 11
                    self.match(CalculadoraParser.NEWLINE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 16
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 17
            self.match(CalculadoraParser.EOF)
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
            return CalculadoraParser.RULE_instruccion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class InstruccionIfContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ifStatement(self):
            return self.getTypedRuleContext(CalculadoraParser.IfStatementContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccionIf" ):
                return visitor.visitInstruccionIf(self)
            else:
                return visitor.visitChildren(self)


    class PrintStmtContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self):
            return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)


    class InstruccionExpresionContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self):
            return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccionExpresion" ):
                return visitor.visitInstruccionExpresion(self)
            else:
                return visitor.visitChildren(self)


    class InstruccionBloqueContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def block(self):
            return self.getTypedRuleContext(CalculadoraParser.BlockContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccionBloque" ):
                return visitor.visitInstruccionBloque(self)
            else:
                return visitor.visitChildren(self)



    def instruccion(self):

        localctx = CalculadoraParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruccion)
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 8, 22, 23]:
                localctx = CalculadoraParser.InstruccionExpresionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.expresion(0)
                pass
            elif token in [1]:
                localctx = CalculadoraParser.PrintStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.match(CalculadoraParser.T__0)
                self.state = 21
                self.match(CalculadoraParser.T__1)
                self.state = 22
                self.expresion(0)
                self.state = 23
                self.match(CalculadoraParser.T__2)
                pass
            elif token in [6]:
                localctx = CalculadoraParser.InstruccionIfContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.ifStatement()
                pass
            elif token in [4]:
                localctx = CalculadoraParser.InstruccionBloqueContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self.block()
                pass
            else:
                raise NoViableAltException(self)

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

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.InstruccionContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(CalculadoraParser.NEWLINE)
            else:
                return self.getToken(CalculadoraParser.NEWLINE, i)

        def getRuleIndex(self):
            return CalculadoraParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = CalculadoraParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(CalculadoraParser.T__3)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 29360470) != 0):
                self.state = 32
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 2, 4, 6, 8, 22, 23]:
                    self.state = 30
                    self.instruccion()
                    pass
                elif token in [24]:
                    self.state = 31
                    self.match(CalculadoraParser.NEWLINE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 37
            self.match(CalculadoraParser.T__4)
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

        def expresion(self):
            return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.BlockContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.BlockContext,i)


        def getRuleIndex(self):
            return CalculadoraParser.RULE_ifStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = CalculadoraParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(CalculadoraParser.T__5)
            self.state = 40
            self.match(CalculadoraParser.T__1)
            self.state = 41
            self.expresion(0)
            self.state = 42
            self.match(CalculadoraParser.T__2)
            self.state = 43
            self.block()
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 44
                self.match(CalculadoraParser.T__6)
                self.state = 45
                self.block()


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
            return CalculadoraParser.RULE_expresion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AndOrLogicoContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndOrLogico" ):
                return visitor.visitAndOrLogico(self)
            else:
                return visitor.visitChildren(self)


    class NumeroContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMERO(self):
            return self.getToken(CalculadoraParser.NUMERO, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)


    class RelacionalContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelacional" ):
                return visitor.visitRelacional(self)
            else:
                return visitor.visitChildren(self)


    class ParentesisContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self):
            return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentesis" ):
                return visitor.visitParentesis(self)
            else:
                return visitor.visitChildren(self)


    class CadenaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(CalculadoraParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCadena" ):
                return visitor.visitCadena(self)
            else:
                return visitor.visitChildren(self)


    class NotLogicoContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self):
            return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotLogico" ):
                return visitor.visitNotLogico(self)
            else:
                return visitor.visitChildren(self)


    class MultiplicacionDivisisionContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicacionDivisision" ):
                return visitor.visitMultiplicacionDivisision(self)
            else:
                return visitor.visitChildren(self)


    class SumaRestaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumaResta" ):
                return visitor.visitSumaResta(self)
            else:
                return visitor.visitChildren(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalculadoraParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = CalculadoraParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 49
                self.match(CalculadoraParser.T__1)
                self.state = 50
                self.expresion(0)
                self.state = 51
                self.match(CalculadoraParser.T__2)
                pass
            elif token in [22]:
                localctx = CalculadoraParser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 53
                self.match(CalculadoraParser.NUMERO)
                pass
            elif token in [23]:
                localctx = CalculadoraParser.CadenaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 54
                self.match(CalculadoraParser.STRING)
                pass
            elif token in [8]:
                localctx = CalculadoraParser.NotLogicoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 55
                self.match(CalculadoraParser.T__7)
                self.state = 56
                self.expresion(5)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 73
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 71
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = CalculadoraParser.MultiplicacionDivisisionContext(self, CalculadoraParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 59
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 60
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 61
                        self.expresion(5)
                        pass

                    elif la_ == 2:
                        localctx = CalculadoraParser.SumaRestaContext(self, CalculadoraParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 62
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 63
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 64
                        self.expresion(4)
                        pass

                    elif la_ == 3:
                        localctx = CalculadoraParser.RelacionalContext(self, CalculadoraParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 65
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 66
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1040384) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 67
                        self.expresion(3)
                        pass

                    elif la_ == 4:
                        localctx = CalculadoraParser.AndOrLogicoContext(self, CalculadoraParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 68
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 69
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==20 or _la==21):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 70
                        self.expresion(2)
                        pass

             
                self.state = 75
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




