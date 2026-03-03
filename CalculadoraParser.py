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
        4,1,19,44,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,0,
        1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,25,8,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,39,8,2,10,2,12,2,42,
        9,2,1,2,0,1,4,3,0,2,4,0,4,1,0,4,5,1,0,6,7,1,0,8,14,1,0,15,16,47,
        0,7,1,0,0,0,2,13,1,0,0,0,4,24,1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,
        9,1,0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,11,1,0,0,0,11,12,5,0,0,1,12,
        1,1,0,0,0,13,14,3,4,2,0,14,15,5,18,0,0,15,3,1,0,0,0,16,17,6,2,-1,
        0,17,18,5,1,0,0,18,19,3,4,2,0,19,20,5,2,0,0,20,25,1,0,0,0,21,25,
        5,17,0,0,22,23,5,3,0,0,23,25,3,4,2,5,24,16,1,0,0,0,24,21,1,0,0,0,
        24,22,1,0,0,0,25,40,1,0,0,0,26,27,10,4,0,0,27,28,7,0,0,0,28,39,3,
        4,2,5,29,30,10,3,0,0,30,31,7,1,0,0,31,39,3,4,2,4,32,33,10,2,0,0,
        33,34,7,2,0,0,34,39,3,4,2,3,35,36,10,1,0,0,36,37,7,3,0,0,37,39,3,
        4,2,2,38,26,1,0,0,0,38,29,1,0,0,0,38,32,1,0,0,0,38,35,1,0,0,0,39,
        42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,5,1,0,0,0,42,40,1,0,0,
        0,4,9,24,38,40
    ]

class CalculadoraParser ( Parser ):

    grammarFileName = "Calculadora.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'!'", "'*'", "'/'", "'+'", 
                     "'-'", "'=='", "'!='", "'<>'", "'<'", "'>'", "'<='", 
                     "'>='", "'&&'", "'||'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUMERO", "NEWLINE", "WS" ]

    RULE_archivo = 0
    RULE_instruccion = 1
    RULE_expresion = 2

    ruleNames =  [ "archivo", "instruccion", "expresion" ]

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
    NUMERO=17
    NEWLINE=18
    WS=19

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


        def getRuleIndex(self):
            return CalculadoraParser.RULE_archivo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArchivo" ):
                listener.enterArchivo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArchivo" ):
                listener.exitArchivo(self)

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
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.instruccion()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 131082) != 0)):
                    break

            self.state = 11
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

        def expresion(self):
            return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,0)


        def NEWLINE(self):
            return self.getToken(CalculadoraParser.NEWLINE, 0)

        def getRuleIndex(self):
            return CalculadoraParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = CalculadoraParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruccion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.expresion(0)
            self.state = 14
            self.match(CalculadoraParser.NEWLINE)
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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndOrLogico" ):
                listener.enterAndOrLogico(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndOrLogico" ):
                listener.exitAndOrLogico(self)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumero" ):
                listener.enterNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumero" ):
                listener.exitNumero(self)

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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelacional" ):
                listener.enterRelacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelacional" ):
                listener.exitRelacional(self)

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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentesis" ):
                listener.enterParentesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentesis" ):
                listener.exitParentesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentesis" ):
                return visitor.visitParentesis(self)
            else:
                return visitor.visitChildren(self)


    class NotLogicoContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self):
            return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotLogico" ):
                listener.enterNotLogico(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotLogico" ):
                listener.exitNotLogico(self)

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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicacionDivisision" ):
                listener.enterMultiplicacionDivisision(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicacionDivisision" ):
                listener.exitMultiplicacionDivisision(self)

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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSumaResta" ):
                listener.enterSumaResta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSumaResta" ):
                listener.exitSumaResta(self)

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
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = CalculadoraParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 17
                self.match(CalculadoraParser.T__0)
                self.state = 18
                self.expresion(0)
                self.state = 19
                self.match(CalculadoraParser.T__1)
                pass
            elif token in [17]:
                localctx = CalculadoraParser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 21
                self.match(CalculadoraParser.NUMERO)
                pass
            elif token in [3]:
                localctx = CalculadoraParser.NotLogicoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 22
                self.match(CalculadoraParser.T__2)
                self.state = 23
                self.expresion(5)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 40
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 38
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = CalculadoraParser.MultiplicacionDivisisionContext(self, CalculadoraParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 26
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 27
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==4 or _la==5):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 28
                        self.expresion(5)
                        pass

                    elif la_ == 2:
                        localctx = CalculadoraParser.SumaRestaContext(self, CalculadoraParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 29
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 30
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==6 or _la==7):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 31
                        self.expresion(4)
                        pass

                    elif la_ == 3:
                        localctx = CalculadoraParser.RelacionalContext(self, CalculadoraParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 32
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 33
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32512) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 34
                        self.expresion(3)
                        pass

                    elif la_ == 4:
                        localctx = CalculadoraParser.AndOrLogicoContext(self, CalculadoraParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 35
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 36
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 37
                        self.expresion(2)
                        pass

             
                self.state = 42
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
        self._predicates[2] = self.expresion_sempred
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
         




