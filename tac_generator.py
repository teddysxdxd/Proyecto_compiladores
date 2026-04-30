# tac_generator.py
# Generador de Código de Tres Direcciones (TAC)
# Rama: desarrollo — compatible con Calculadora.g4 de esa rama
#
# Instrucciones TAC emitidas:
#   t1 = a OP b          aritmética / relacional / lógica binaria
#   t1 = !a              negación lógica
#   VAR = t1             asignación
#   print t1             salida estándar
#   ifFalse t1 goto Ln   salto condicional (falso)
#   goto Ln              salto incondicional
#   Ln:                  etiqueta de destino
#   param t1             argumento real (antes de call)
#   t1 = call f, N       llamada con retorno
#   call f, N            llamada sin captura de retorno
#   begin_func f         apertura de función
#   param_decl TIPO id   parámetro formal
#   end_func f           cierre de función
#   return t1            retorno con valor
#   return               retorno vacío

from CalculadoraParser import CalculadoraParser
from CalculadoraVisitor import CalculadoraVisitor


class TACGenerator(CalculadoraVisitor):

    def __init__(self):
        self.instructions = []
        self._temp_count = 0
        self._label_count = 0

    # ── helpers ────────────────────────────────────────────────────
    def _new_temp(self) -> str:
        self._temp_count += 1
        return f"t{self._temp_count}"

    def _new_label(self) -> str:
        self._label_count += 1
        return f"L{self._label_count}"

    def _emit(self, line: str):
        self.instructions.append(line)

    def get_tac(self) -> str:
        return "\n".join(self.instructions)

    def save(self, path: str):
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.get_tac())
            f.write("\n")
        print(f"[TAC] Generado: {path}  ({len(self.instructions)} instrucciones)")

    # ── programa raíz ──────────────────────────────────────────────
    def visitArchivo(self, ctx: CalculadoraParser.ArchivoContext):
        self._emit("; ===== TAC  —  inicio de programa =====")
        self.visitChildren(ctx)
        self._emit("; ===== TAC  —  fin de programa   =====")

    # ── instrucciones (dispatch por label ANTLR) ───────────────────
    def visitInstruccionDeclaracion(self, ctx):
        return self.visit(ctx.declaracion())

    def visitEjecutarAsignacion(self, ctx):
        return self.visit(ctx.asignacion())

    def visitEjecutarPrint(self, ctx):
        val = self.visit(ctx.expresion())
        self._emit(f"print {val}")

    def visitInstruccionIf(self, ctx):
        return self.visit(ctx.ifStatement())

    def visitInstruccionWhile(self, ctx):
        return self.visit(ctx.whileStatement())

    def visitInstruccionFor(self, ctx):
        return self.visit(ctx.forStatement())

    def visitInstruccionReturn(self, ctx):
        return self.visit(ctx.returnStmt())

    def visitInstruccionFuncion(self, ctx):
        return self.visit(ctx.funcionDecl())

    def visitInstruccionExpresion(self, ctx):
        # Expresión usada como instrucción standalone: suma(10, 20)
        # El TAC de la llamada ya se emite dentro de visitLlamadaFuncion.
        self.visit(ctx.expresion())

    def visitInstruccionBloque(self, ctx):
        return self.visit(ctx.block())

    # ── declaración: TIPO ID (= expr)? ────────────────────────────
    def visitDeclaracion(self, ctx: CalculadoraParser.DeclaracionContext):
        name = ctx.ID().getText()
        if ctx.expresion():
            val = self.visit(ctx.expresion())
            self._emit(f"{name} = {val}")
        else:
            defaults = {
                "int": "0", "float": "0.0",
                "string": '""', "bool": "false", "void": "0"
            }
            tipo = ctx.TIPO().getText()
            self._emit(f"{name} = {defaults.get(tipo, '0')}")

    # ── asignación: ID = expr ──────────────────────────────────────
    def visitAsignacion(self, ctx: CalculadoraParser.AsignacionContext):
        name = ctx.ID().getText()
        val = self.visit(ctx.expresion())
        self._emit(f"{name} = {val}")

    # ── return (expr)? ────────────────────────────────────────────
    def visitReturnStmt(self, ctx: CalculadoraParser.ReturnStmtContext):
        if ctx.expresion():
            val = self.visit(ctx.expresion())
            self._emit(f"return {val}")
        else:
            self._emit("return")

    # ── función: TIPO ID(params?) block ───────────────────────────
    def visitFuncionDecl(self, ctx: CalculadoraParser.FuncionDeclContext):
        name     = ctx.ID().getText()
        ret_type = ctx.TIPO().getText()
        self._emit("")
        self._emit(f"; --- func {ret_type} {name} ---")
        self._emit(f"begin_func {name}")

        if ctx.params():
            p = ctx.params()
            tipos = [t.getText() for t in p.TIPO()]
            ids   = [i.getText() for i in p.ID()]
            for t, pid in zip(tipos, ids):
                self._emit(f"param_decl {t} {pid}")

        self.visit(ctx.block())
        self._emit(f"end_func {name}")
        self._emit("")

    # ── bloque: { instruccion* } ───────────────────────────────────
    def visitBlock(self, ctx: CalculadoraParser.BlockContext):
        self.visitChildren(ctx)

    # ── if / if-else  (simon / sinel) ─────────────────────────────
    def visitIfStatement(self, ctx: CalculadoraParser.IfStatementContext):
        cond   = self.visit(ctx.expresion())
        blocks = ctx.block()

        if len(blocks) == 1:
            l_end = self._new_label()
            self._emit(f"ifFalse {cond} goto {l_end}")
            self.visit(blocks[0])
            self._emit(f"{l_end}:")
        else:
            l_else = self._new_label()
            l_end  = self._new_label()
            self._emit(f"ifFalse {cond} goto {l_else}")
            self.visit(blocks[0])
            self._emit(f"goto {l_end}")
            self._emit(f"{l_else}:")
            self.visit(blocks[1])
            self._emit(f"{l_end}:")

    # ── while ─────────────────────────────────────────────────────
    def visitWhileStatement(self, ctx: CalculadoraParser.WhileStatementContext):
        l_start = self._new_label()
        l_end   = self._new_label()
        self._emit(f"{l_start}:")
        cond = self.visit(ctx.expresion())
        self._emit(f"ifFalse {cond} goto {l_end}")
        self.visit(ctx.block())
        self._emit(f"goto {l_start}")
        self._emit(f"{l_end}:")

    # ── for ───────────────────────────────────────────────────────
    def visitForStatement(self, ctx: CalculadoraParser.ForStatementContext):
        asigs   = ctx.asignacion()  # [init, update]
        l_start = self._new_label()
        l_end   = self._new_label()

        self.visit(asigs[0])        # init
        self._emit(f"{l_start}:")
        cond = self.visit(ctx.expresion())
        self._emit(f"ifFalse {cond} goto {l_end}")
        self.visit(ctx.block())
        self.visit(asigs[1])        # update
        self._emit(f"goto {l_start}")
        self._emit(f"{l_end}:")

    # ── expresiones ── cada una retorna el nombre del temp o literal
    def visitNumero(self, ctx: CalculadoraParser.NumeroContext):
        return ctx.NUMERO().getText()

    def visitCadena(self, ctx: CalculadoraParser.CadenaContext):
        return ctx.STRING().getText()

    def visitBooleano(self, ctx: CalculadoraParser.BooleanoContext):
        return ctx.BOOLEANO().getText()

    def visitVariable(self, ctx: CalculadoraParser.VariableContext):
        return ctx.ID().getText()

    def visitParentesis(self, ctx: CalculadoraParser.ParentesisContext):
        # ( expr )  — transparente
        return self.visit(ctx.expresion())

    def visitCorchetes(self, ctx: CalculadoraParser.CorchetesContext):
        # [ expr ]  — agrupación (ej. [x + 1]), transparente en TAC
        return self.visit(ctx.expresion())

    def visitNotLogico(self, ctx: CalculadoraParser.NotLogicoContext):
        operand = self.visit(ctx.expresion())
        tmp = self._new_temp()
        self._emit(f"{tmp} = !{operand}")
        return tmp

    def visitMultiplicacionDivisisionMod(self, ctx: CalculadoraParser.MultiplicacionDivisisionModContext):
        left  = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        tmp   = self._new_temp()
        self._emit(f"{tmp} = {left} {ctx.op.text} {right}")
        return tmp

    def visitSumaResta(self, ctx: CalculadoraParser.SumaRestaContext):
        left  = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        tmp   = self._new_temp()
        self._emit(f"{tmp} = {left} {ctx.op.text} {right}")
        return tmp

    def visitRelacional(self, ctx: CalculadoraParser.RelacionalContext):
        left  = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        tmp   = self._new_temp()
        self._emit(f"{tmp} = {left} {ctx.op.text} {right}")
        return tmp

    def visitAndOrLogico(self, ctx: CalculadoraParser.AndOrLogicoContext):
        left  = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        tmp   = self._new_temp()
        self._emit(f"{tmp} = {left} {ctx.op.text} {right}")
        return tmp

    # ── llamada a función: ID(args?) ──────────────────────────────
    # Cubre tanto el caso con asignación (visitado desde otro visitor)
    # como el caso standalone (visitado desde visitInstruccionExpresion).
    def visitLlamadaFuncion(self, ctx: CalculadoraParser.LlamadaFuncionContext):
        name = ctx.ID().getText()
        args = []
        if ctx.args():
            for expr in ctx.args().expresion():
                args.append(self.visit(expr))

        for arg in args:
            self._emit(f"param {arg}")

        tmp = self._new_temp()
        self._emit(f"{tmp} = call {name}, {len(args)}")
        return tmp
