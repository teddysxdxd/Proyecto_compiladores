# tac_generator.py
# Generador de Código de Tres Direcciones (TAC)

from CalculadoraParser import CalculadoraParser
from CalculadoraVisitor import CalculadoraVisitor


class TACGenerator(CalculadoraVisitor):
    def __init__(self):
        self.instructions = []
        self._temp_count = 0
        self._label_count = 0
        self.struct_defs = {}

    # ---------------- helpers ----------------
    def _new_temp(self) -> str:
        self._temp_count += 1
        return f"t{self._temp_count}"

    def _new_label(self) -> str:
        self._label_count += 1
        return f"L{self._label_count}"

    def _emit(self, line: str):
        self.instructions.append(line)

    def _iter_lvalue_ops(self, lvalue_ctx):
        children = list(lvalue_ctx.getChildren())
        expr_ctxs = lvalue_ctx.expresion()
        expr_i = 0
        i = 1
        while i < len(children):
            text = children[i].getText()
            if text == "." and i + 1 < len(children):
                yield ("field", children[i + 1].getText(), None)
                i += 2
            elif text == "[":
                expr_ctx = expr_ctxs[expr_i] if expr_i < len(expr_ctxs) else None
                yield ("index", None, expr_ctx)
                expr_i += 1
                i += 3
            else:
                i += 1

    def _lvalue_text(self, lvalue_ctx) -> str:
        ids = lvalue_ctx.ID()
        if not ids:
            return ""
        text = ids[0].getText()
        for op_kind, field, expr_ctx in self._iter_lvalue_ops(lvalue_ctx):
            if op_kind == "field":
                text += f".{field}"
            elif op_kind == "index":
                idx = self.visit(expr_ctx) if expr_ctx else "0"
                text += f"[{idx}]"
        return text

    def get_tac(self) -> str:
        return "\n".join(self.instructions)

    def save(self, path: str):
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.get_tac())
            f.write("\n")
        print(f"[TAC] Generado: {path}  ({len(self.instructions)} instrucciones)")

    # ---------------- raíz ----------------
    def visitArchivo(self, ctx: CalculadoraParser.ArchivoContext):
        self._emit("; ===== TAC  —  inicio de programa =====")
        self.visitChildren(ctx)
        self._emit("; ===== TAC  —  fin de programa   =====")

    # ---------------- dispatch de instrucciones ----------------
    def visitInstruccionDeclaracion(self, ctx):
        return self.visit(ctx.declaracion())

    def visitEjecutarAsignacion(self, ctx):
        return self.visit(ctx.asignacion())

    def visitEjecutarPrint(self, ctx):
        val = self.visit(ctx.expresion())
        self._emit(f"print {val}")

    def visitInstruccionIf(self, ctx):
        return self.visit(ctx.ifStatement())

    def visitInstruccionSwitch(self, ctx):
        return self.visit(ctx.switchStatement())

    def visitInstruccionWhile(self, ctx):
        return self.visit(ctx.whileStatement())

    def visitInstruccionFor(self, ctx):
        return self.visit(ctx.forStatement())

    def visitInstruccionReturn(self, ctx):
        return self.visit(ctx.returnStmt())

    def visitInstruccionFuncion(self, ctx):
        return self.visit(ctx.funcionDecl())

    def visitInstruccionStruct(self, ctx):
        return self.visit(ctx.structDecl())

    def visitInstruccionExpresion(self, ctx):
        self.visit(ctx.expresion())

    def visitInstruccionBloque(self, ctx):
        return self.visit(ctx.block())

    # ---------------- structs ----------------
    def visitStructDecl(self, ctx: CalculadoraParser.StructDeclContext):
        name = ctx.ID().getText()
        fields = []
        for fctx in ctx.structFieldDecl():
            fields.append((fctx.TIPO().getText(), fctx.ID().getText()))
        self.struct_defs[name] = fields

        self._emit(f"; --- struct {name} ---")
        for ftype, fname in fields:
            self._emit(f"; field {ftype} {fname}")
        self._emit(f"; --- end struct {name} ---")
        return None

    # ---------------- declaraciones ----------------
    def visitDeclaracion(self, ctx: CalculadoraParser.DeclaracionContext):
        # TIPO [] ID = [expr, ...]
        if ctx.TIPO() and len(ctx.CORCHI()) >= 2:
            tipo = ctx.TIPO().getText()
            name = ctx.ID(0).getText()
            vals = [self.visit(expr_ctx) for expr_ctx in ctx.expresion()]
            self._emit(f"{name} = array<{tipo}>[{len(vals)}]")
            for idx, val in enumerate(vals):
                self._emit(f"{name}[{idx}] = {val}")
            return None

        # TIPO ID (= expr)?
        if ctx.TIPO():
            name = ctx.ID(0).getText()
            exprs = ctx.expresion()
            expr_ctx = exprs[0] if exprs else None
            if expr_ctx:
                val = self.visit(expr_ctx)
                self._emit(f"{name} = {val}")
            else:
                defaults = {
                    "int": "0",
                    "float": "0.0",
                    "string": '""',
                    "bool": "false",
                    "void": "0",
                }
                tipo = ctx.TIPO().getText()
                self._emit(f"{name} = {defaults.get(tipo, '0')}")
            return None

        # ID ID  (variable struct)
        struct_name = ctx.ID(0).getText()
        var_name = ctx.ID(1).getText()
        self._emit(f"{var_name} = struct {struct_name}")

        for ftype, fname in self.struct_defs.get(struct_name, []):
            defaults = {
                "int": "0",
                "float": "0.0",
                "string": '""',
                "bool": "false",
            }
            self._emit(f"{var_name}.{fname} = {defaults.get(ftype, '0')}")
        return None

    # ---------------- asignación ----------------
    def visitAsignacion(self, ctx: CalculadoraParser.AsignacionContext):
        left = self._lvalue_text(ctx.lvalue())
        val = self.visit(ctx.expresion())
        self._emit(f"{left} = {val}")
        return left

    def visitReturnStmt(self, ctx: CalculadoraParser.ReturnStmtContext):
        if ctx.expresion():
            val = self.visit(ctx.expresion())
            self._emit(f"return {val}")
        else:
            self._emit("return")

    # ---------------- función ----------------
    def visitFuncionDecl(self, ctx: CalculadoraParser.FuncionDeclContext):
        name = ctx.ID().getText()
        ret_type = ctx.TIPO().getText()
        self._emit("")
        self._emit(f"; --- func {ret_type} {name} ---")
        self._emit(f"begin_func {name}")

        if ctx.params():
            p = ctx.params()
            tipos = [t.getText() for t in p.TIPO()]
            ids = [i.getText() for i in p.ID()]
            for t, pid in zip(tipos, ids):
                self._emit(f"param_decl {t} {pid}")

        self.visit(ctx.block())
        self._emit(f"end_func {name}")
        self._emit("")

    def visitBlock(self, ctx: CalculadoraParser.BlockContext):
        self.visitChildren(ctx)

    # ---------------- if / switch / while / for ----------------
    def visitIfStatement(self, ctx: CalculadoraParser.IfStatementContext):
        cond = self.visit(ctx.expresion())
        blocks = ctx.block()

        if len(blocks) == 1:
            l_end = self._new_label()
            self._emit(f"ifFalse {cond} goto {l_end}")
            self.visit(blocks[0])
            self._emit(f"{l_end}:")
        else:
            l_else = self._new_label()
            l_end = self._new_label()
            self._emit(f"ifFalse {cond} goto {l_else}")
            self.visit(blocks[0])
            self._emit(f"goto {l_end}")
            self._emit(f"{l_else}:")
            self.visit(blocks[1])
            self._emit(f"{l_end}:")

    def visitSwitchStatement(self, ctx: CalculadoraParser.SwitchStatementContext):
        ctrl = self.visit(ctx.expresion())
        l_end = self._new_label()
        next_case_label = self._new_label()

        case_clauses = ctx.caseClause()
        for idx, case_ctx in enumerate(case_clauses):
            if idx == 0:
                self._emit(f"{next_case_label}:")
            case_val = self.visit(case_ctx.expresion())
            cond = self._new_temp()
            following = self._new_label()
            self._emit(f"{cond} = {ctrl} == {case_val}")
            self._emit(f"ifFalse {cond} goto {following}")

            for inst in case_ctx.instruccion():
                self.visit(inst)
            self._emit(f"goto {l_end}")
            self._emit(f"{following}:")

        if ctx.defaultClause():
            for inst in ctx.defaultClause().instruccion():
                self.visit(inst)

        self._emit(f"{l_end}:")

    def visitWhileStatement(self, ctx: CalculadoraParser.WhileStatementContext):
        l_start = self._new_label()
        l_end = self._new_label()
        self._emit(f"{l_start}:")
        cond = self.visit(ctx.expresion())
        self._emit(f"ifFalse {cond} goto {l_end}")
        self.visit(ctx.block())
        self._emit(f"goto {l_start}")
        self._emit(f"{l_end}:")

    def visitForStatement(self, ctx: CalculadoraParser.ForStatementContext):
        asigs = ctx.asignacion()
        l_start = self._new_label()
        l_end = self._new_label()

        self.visit(asigs[0])
        self._emit(f"{l_start}:")
        cond = self.visit(ctx.expresion())
        self._emit(f"ifFalse {cond} goto {l_end}")
        self.visit(ctx.block())
        self.visit(asigs[1])
        self._emit(f"goto {l_start}")
        self._emit(f"{l_end}:")

    # ---------------- expresiones ----------------
    def visitNumero(self, ctx: CalculadoraParser.NumeroContext):
        return ctx.NUMERO().getText()

    def visitCadena(self, ctx: CalculadoraParser.CadenaContext):
        return ctx.STRING().getText()

    def visitBooleano(self, ctx: CalculadoraParser.BooleanoContext):
        return ctx.BOOLEANO().getText()

    def visitVariable(self, ctx: CalculadoraParser.VariableContext):
        return self._lvalue_text(ctx.lvalue())

    def visitParentesis(self, ctx: CalculadoraParser.ParentesisContext):
        return self.visit(ctx.expresion())

    def visitCorchetes(self, ctx: CalculadoraParser.CorchetesContext):
        return self.visit(ctx.expresion())

    def visitCastExplicito(self, ctx: CalculadoraParser.CastExplicitoContext):
        val = self.visit(ctx.expresion())
        dst = ctx.TIPO().getText()
        tmp = self._new_temp()
        self._emit(f"{tmp} = ({dst}) {val}")
        return tmp

    def visitNotLogico(self, ctx: CalculadoraParser.NotLogicoContext):
        operand = self.visit(ctx.expresion())
        tmp = self._new_temp()
        self._emit(f"{tmp} = !{operand}")
        return tmp

    def visitMultiplicacionDivisisionMod(self, ctx: CalculadoraParser.MultiplicacionDivisisionModContext):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        tmp = self._new_temp()
        self._emit(f"{tmp} = {left} {ctx.op.text} {right}")
        return tmp

    def visitSumaResta(self, ctx: CalculadoraParser.SumaRestaContext):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        tmp = self._new_temp()
        self._emit(f"{tmp} = {left} {ctx.op.text} {right}")
        return tmp

    def visitRelacional(self, ctx: CalculadoraParser.RelacionalContext):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        tmp = self._new_temp()
        self._emit(f"{tmp} = {left} {ctx.op.text} {right}")
        return tmp

    def visitAndOrLogico(self, ctx: CalculadoraParser.AndOrLogicoContext):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        tmp = self._new_temp()
        self._emit(f"{tmp} = {left} {ctx.op.text} {right}")
        return tmp

    def visitTernario(self, ctx: CalculadoraParser.TernarioContext):
        cond = self.visit(ctx.expresion(0))
        l_false = self._new_label()
        l_end = self._new_label()
        tmp = self._new_temp()

        self._emit(f"ifFalse {cond} goto {l_false}")
        true_val = self.visit(ctx.expresion(1))
        self._emit(f"{tmp} = {true_val}")
        self._emit(f"goto {l_end}")
        self._emit(f"{l_false}:")
        false_val = self.visit(ctx.expresion(2))
        self._emit(f"{tmp} = {false_val}")
        self._emit(f"{l_end}:")
        return tmp

    # ---------------- llamadas ----------------
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

    def visitLlamadaModulo(self, ctx):
        modulo = ctx.ID(0).getText()
        funcion = ctx.ID(1).getText()
        nombre = f"{modulo}.{funcion}"

        args = []
        for expr in ctx.expresion():
            args.append(self.visit(expr))

        for arg in args:
            self._emit(f"param {arg}")

        tmp = self._new_temp()
        self._emit(f"{tmp} = call {nombre}, {len(args)}")
        return tmp
