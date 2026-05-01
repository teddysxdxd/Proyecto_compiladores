# ir_generator.py
# Generador de LLVM IR usando llvmlite 0.47+
# Compatible con Calculadora.g4 rama desarrollo
#
# Tipos:
#   int    -> i32
#   float  -> double
#   bool   -> i1
#   string -> i8*   (puntero a constante global)
#   void   -> void
#
# El .ll producido es:
#   verificable con:  llvm-as archivo.ll
#   ejecutable con:   lli archivo.ll

from llvmlite import ir, binding
from CalculadoraParser import CalculadoraParser
from CalculadoraVisitor import CalculadoraVisitor


# ── Tipos base ─────────────────────────────────────────────────────
INT   = ir.IntType(32)
FLOAT = ir.DoubleType()
BOOL  = ir.IntType(1)
VOID  = ir.VoidType()
I8    = ir.IntType(8)
I8PTR = ir.PointerType(I8)
I64   = ir.IntType(64)


def llvm_type(tipo_str: str) -> ir.Type:
    return {"int": INT, "float": FLOAT, "bool": BOOL,
            "void": VOID, "string": I8PTR}.get(tipo_str, INT)


def default_val(tipo_str: str) -> ir.Constant:
    return {"int":    ir.Constant(INT, 0),
            "float":  ir.Constant(FLOAT, 0.0),
            "bool":   ir.Constant(BOOL, 0),
            "string": ir.Constant(I8PTR, None)}.get(tipo_str, ir.Constant(INT, 0))


def tipo_str_from_llvm(ltype: ir.Type) -> str:
    if ltype == INT:   return "int"
    if ltype == FLOAT: return "float"
    if ltype == BOOL:  return "bool"
    if ltype == I8PTR: return "string"
    return "int"


# ── Scope de variables ─────────────────────────────────────────────
class Scope:
    def __init__(self, parent=None):
        self.parent   = parent
        self.vars     = {}   # name -> ir.AllocaInstr
        self.tipos    = {}   # name -> tipo_str

    def define(self, name: str, alloca: ir.AllocaInstr, tipo_str: str):
        self.vars[name]  = alloca
        self.tipos[name] = tipo_str

    def lookup(self, name: str):
        if name in self.vars:
            return self.vars[name], self.tipos[name]
        if self.parent:
            return self.parent.lookup(name)
        return None, None


# ── Generador ─────────────────────────────────────────────────────
class IRGenerator(CalculadoraVisitor):

    def __init__(self):
        self.module   = ir.Module(name="programa")
        self.module.triple = "x86_64-pc-linux-gnu"

        self.builder: ir.IRBuilder = None
        self.scope    = None
        self.functions = {}          # name -> (ir.Function, ret_tipo_str)
        self.current_ret_tipo = None # tipo_str de la función actual
        self._str_n  = 0
        self._fmt_cache = {}         # texto -> ir.GlobalVariable

        # Declarar printf
        printf_ty   = ir.FunctionType(INT, [I8PTR], var_arg=True)
        self.printf = ir.Function(self.module, printf_ty, name="printf")

    # ── helpers globales ───────────────────────────────────────────

    def _global_str(self, text: str) -> ir.GlobalVariable:
        if text in self._fmt_cache:
            return self._fmt_cache[text]
        encoded = (text + "\0").encode("utf-8")
        arr_ty  = ir.ArrayType(I8, len(encoded))
        gvar    = ir.GlobalVariable(self.module, arr_ty,
                                    name=f".str.{self._str_n}")
        self._str_n += 1
        gvar.linkage         = "private"
        gvar.global_constant = True
        gvar.initializer     = ir.Constant(arr_ty, bytearray(encoded))
        self._fmt_cache[text] = gvar
        return gvar

    def _str_ptr(self, gvar: ir.GlobalVariable) -> ir.Value:
        z = ir.Constant(I64, 0)
        return self.builder.gep(gvar, [z, z], inbounds=True)

    def _printf(self, fmt: str, val: ir.Value):
        ptr = self._str_ptr(self._global_str(fmt))
        self.builder.call(self.printf, [ptr, val])

    # ── coerciones de tipo ─────────────────────────────────────────

    def _coerce(self, val: ir.Value, target: ir.Type) -> ir.Value:
        if val is None:
            return ir.Constant(target if target != VOID else INT, 0)
        if val.type == target:
            return val
        # int -> float
        if val.type == INT and target == FLOAT:
            return self.builder.sitofp(val, FLOAT)
        # float -> int
        if val.type == FLOAT and target == INT:
            return self.builder.fptosi(val, INT)
        # bool -> int
        if val.type == BOOL and target == INT:
            return self.builder.zext(val, INT)
        # bool -> float
        if val.type == BOOL and target == FLOAT:
            return self.builder.sitofp(self.builder.zext(val, INT), FLOAT)
        # int -> bool
        if val.type == INT and target == BOOL:
            return self.builder.icmp_signed("!=", val, ir.Constant(INT, 0))
        # float -> bool
        if val.type == FLOAT and target == BOOL:
            return self.builder.fcmp_ordered("one", val,
                                             ir.Constant(FLOAT, 0.0))
        return val

    # ── alloca al inicio del bloque entry de la función actual ─────
    # En llvmlite 0.47 el builder inserta en la posición actual,
    # así que guardamos el punto de inserción, volvemos al inicio
    # del entry block, hacemos alloca, y restauramos.

    def _alloca(self, name: str, ltype: ir.Type) -> ir.AllocaInstr:
        fn    = self.builder.function
        entry = fn.entry_basic_block

        # Guardar posición actual
        saved_block = self.builder.block
        saved_pos   = self.builder._anchor   # posición interna llvmlite

        # Posicionarse al inicio del entry block
        self.builder.position_at_start(entry)
        alloca = self.builder.alloca(ltype, name=name)

        # Restaurar posición original
        if saved_block is entry:
            # Estábamos en entry: volver después de la alloca recién creada
            # pero antes de donde estábamos → posicionar al final del bloque
            # (las instrucciones previas ya estaban bien)
            self.builder.position_at_end(saved_block)
        else:
            self.builder.position_at_end(saved_block)

        return alloca

    # ── print polimórfico ──────────────────────────────────────────

    def _print_val(self, val: ir.Value):
        if val is None:
            return
        t = val.type
        if t == INT:
            self._printf("%d\n", val)
        elif t == FLOAT:
            self._printf("%f\n", val)
        elif t == BOOL:
            self._printf("%d\n", self.builder.zext(val, INT))
        elif t == I8PTR:
            self._printf("%s\n", val)
        else:
            try:
                self._printf("%d\n", self._coerce(val, INT))
            except Exception:
                pass

    # ── programa raíz ──────────────────────────────────────────────

    def visitArchivo(self, ctx: CalculadoraParser.ArchivoContext):
        # Construir main() i32 como punto de entrada
        main_ty = ir.FunctionType(INT, [])
        main_fn = ir.Function(self.module, main_ty, name="main")
        self.functions["main"] = (main_fn, "int")
        self.current_ret_tipo  = "int"

        entry = main_fn.append_basic_block("entry")
        self.builder = ir.IRBuilder(entry)
        self.scope   = Scope()

        self.visitChildren(ctx)

        if not self.builder.block.is_terminated:
            self.builder.ret(ir.Constant(INT, 0))

        self.current_ret_tipo = None

    # ── instrucciones ──────────────────────────────────────────────

    def visitInstruccionDeclaracion(self, ctx):
        self.visit(ctx.declaracion())

    def visitEjecutarAsignacion(self, ctx):
        self.visit(ctx.asignacion())

    def visitEjecutarPrint(self, ctx):
        val = self.visit(ctx.expresion())
        self._print_val(val)

    def visitInstruccionIf(self, ctx):
        self.visit(ctx.ifStatement())

    def visitInstruccionWhile(self, ctx):
        self.visit(ctx.whileStatement())

    def visitInstruccionFor(self, ctx):
        self.visit(ctx.forStatement())

    def visitInstruccionReturn(self, ctx):
        self.visit(ctx.returnStmt())

    def visitInstruccionFuncion(self, ctx):
        self.visit(ctx.funcionDecl())

    def visitInstruccionExpresion(self, ctx):
        self.visit(ctx.expresion())   # llamada standalone; resultado descartado

    def visitInstruccionBloque(self, ctx):
        self.visit(ctx.block())

    # ── declaración ───────────────────────────────────────────────

    def visitDeclaracion(self, ctx: CalculadoraParser.DeclaracionContext):
        tipo_str = ctx.TIPO().getText()
        name     = ctx.ID().getText()
        ltype    = llvm_type(tipo_str)

        alloca = self._alloca(name, ltype)
        self.scope.define(name, alloca, tipo_str)

        if ctx.expresion():
            val = self._coerce(self.visit(ctx.expresion()), ltype)
        else:
            val = default_val(tipo_str)

        self.builder.store(val, alloca)

    # ── asignación ────────────────────────────────────────────────

    def visitAsignacion(self, ctx: CalculadoraParser.AsignacionContext):
        name             = ctx.ID().getText()
        alloca, tipo_str = self.scope.lookup(name)
        rval             = self.visit(ctx.expresion())

        if alloca is None:
            # Variable no declarada explícitamente (for loop sin tipo)
            tipo_str = tipo_str_from_llvm(rval.type)
            alloca   = self._alloca(name, rval.type)
            self.scope.define(name, alloca, tipo_str)

        rval = self._coerce(rval, llvm_type(tipo_str))
        self.builder.store(rval, alloca)

    # ── return ────────────────────────────────────────────────────

    def visitReturnStmt(self, ctx: CalculadoraParser.ReturnStmtContext):
        if self.builder.block.is_terminated:
            return

        ret_ltype = llvm_type(self.current_ret_tipo or "int")

        if ctx.expresion():
            val = self.visit(ctx.expresion())
            if ret_ltype == VOID:
                self.builder.ret_void()
            else:
                self.builder.ret(self._coerce(val, ret_ltype))
        else:
            if ret_ltype == VOID:
                self.builder.ret_void()
            else:
                self.builder.ret(ir.Constant(ret_ltype, 0))

    # ── declaración de función ────────────────────────────────────

    def visitFuncionDecl(self, ctx: CalculadoraParser.FuncionDeclContext):
        ret_tipo = ctx.TIPO().getText()
        name     = ctx.ID().getText()

        param_tipos = []
        param_names = []
        if ctx.params():
            p = ctx.params()
            param_tipos = [t.getText() for t in p.TIPO()]
            param_names = [i.getText() for i in p.ID()]

        fn_ty = ir.FunctionType(llvm_type(ret_tipo),
                                [llvm_type(t) for t in param_tipos])
        fn    = ir.Function(self.module, fn_ty, name=name)
        self.functions[name] = (fn, ret_tipo)

        for arg, pname in zip(fn.args, param_names):
            arg.name = pname

        # Guardar contexto del llamador
        prev_builder  = self.builder
        prev_scope    = self.scope
        prev_ret_tipo = self.current_ret_tipo

        # Nuevo contexto
        entry = fn.append_basic_block("entry")
        self.builder          = ir.IRBuilder(entry)
        self.scope            = Scope(parent=prev_scope)
        self.current_ret_tipo = ret_tipo

        # Alocar parámetros en stack y hacer store del argumento
        for arg, pname, ptyp in zip(fn.args, param_names, param_tipos):
            alloca = self._alloca(pname, llvm_type(ptyp))
            self.builder.store(arg, alloca)
            self.scope.define(pname, alloca, ptyp)

        # Cuerpo
        self.visit(ctx.block())

        # Ret implícito si el bloque no terminó
        if not self.builder.block.is_terminated:
            if llvm_type(ret_tipo) == VOID:
                self.builder.ret_void()
            else:
                self.builder.ret(ir.Constant(llvm_type(ret_tipo), 0))

        # Restaurar contexto
        self.builder          = prev_builder
        self.scope            = prev_scope
        self.current_ret_tipo = prev_ret_tipo

    # ── bloque ────────────────────────────────────────────────────

    def visitBlock(self, ctx: CalculadoraParser.BlockContext):
        self.scope = Scope(parent=self.scope)
        self.visitChildren(ctx)
        self.scope = self.scope.parent

    # ── if / if-else ──────────────────────────────────────────────

    def visitIfStatement(self, ctx: CalculadoraParser.IfStatementContext):
        cond   = self._coerce(self.visit(ctx.expresion()), BOOL)
        fn     = self.builder.function
        blocks = ctx.block()

        then_bb  = fn.append_basic_block("then")
        else_bb  = fn.append_basic_block("else") if len(blocks) > 1 else None
        merge_bb = fn.append_basic_block("if_end")

        self.builder.cbranch(cond, then_bb, else_bb or merge_bb)

        self.builder.position_at_end(then_bb)
        self.visit(blocks[0])
        if not self.builder.block.is_terminated:
            self.builder.branch(merge_bb)

        if else_bb:
            self.builder.position_at_end(else_bb)
            self.visit(blocks[1])
            if not self.builder.block.is_terminated:
                self.builder.branch(merge_bb)

        self.builder.position_at_end(merge_bb)

    # ── while ─────────────────────────────────────────────────────

    def visitWhileStatement(self, ctx: CalculadoraParser.WhileStatementContext):
        fn = self.builder.function
        cond_bb = fn.append_basic_block("while_cond")
        body_bb = fn.append_basic_block("while_body")
        end_bb  = fn.append_basic_block("while_end")

        self.builder.branch(cond_bb)

        self.builder.position_at_end(cond_bb)
        cond = self._coerce(self.visit(ctx.expresion()), BOOL)
        self.builder.cbranch(cond, body_bb, end_bb)

        self.builder.position_at_end(body_bb)
        self.visit(ctx.block())
        if not self.builder.block.is_terminated:
            self.builder.branch(cond_bb)

        self.builder.position_at_end(end_bb)

    # ── for ───────────────────────────────────────────────────────

    def visitForStatement(self, ctx: CalculadoraParser.ForStatementContext):
        asigs = ctx.asignacion()
        fn    = self.builder.function

        cond_bb = fn.append_basic_block("for_cond")
        body_bb = fn.append_basic_block("for_body")
        incr_bb = fn.append_basic_block("for_incr")
        end_bb  = fn.append_basic_block("for_end")

        self.visit(asigs[0])
        self.builder.branch(cond_bb)

        self.builder.position_at_end(cond_bb)
        cond = self._coerce(self.visit(ctx.expresion()), BOOL)
        self.builder.cbranch(cond, body_bb, end_bb)

        self.builder.position_at_end(body_bb)
        self.visit(ctx.block())
        if not self.builder.block.is_terminated:
            self.builder.branch(incr_bb)

        self.builder.position_at_end(incr_bb)
        self.visit(asigs[1])
        self.builder.branch(cond_bb)

        self.builder.position_at_end(end_bb)

    # ── expresiones ───────────────────────────────────────────────

    def visitNumero(self, ctx: CalculadoraParser.NumeroContext):
        txt = ctx.NUMERO().getText()
        if "." in txt:
            return ir.Constant(FLOAT, float(txt))
        return ir.Constant(INT, int(txt))

    def visitCadena(self, ctx: CalculadoraParser.CadenaContext):
        raw  = ctx.STRING().getText()[1:-1]       # quitar comillas
        gvar = self._global_str(raw)
        return self._str_ptr(gvar)

    def visitBooleano(self, ctx: CalculadoraParser.BooleanoContext):
        return ir.Constant(BOOL, 1 if ctx.BOOLEANO().getText() == "true" else 0)

    def visitVariable(self, ctx: CalculadoraParser.VariableContext):
        name             = ctx.ID().getText()
        alloca, tipo_str = self.scope.lookup(name)
        if alloca is None:
            return ir.Constant(INT, 0)
        return self.builder.load(alloca, name=name)

    def visitParentesis(self, ctx: CalculadoraParser.ParentesisContext):
        return self.visit(ctx.expresion())

    def visitCorchetes(self, ctx: CalculadoraParser.CorchetesContext):
        return self.visit(ctx.expresion())

    def visitNotLogico(self, ctx: CalculadoraParser.NotLogicoContext):
        val = self._coerce(self.visit(ctx.expresion()), BOOL)
        return self.builder.not_(val)

    def _arith(self, left: ir.Value, right: ir.Value, op: str) -> ir.Value:
        # Promoción a float si alguno lo es
        if left.type == FLOAT or right.type == FLOAT:
            left  = self._coerce(left, FLOAT)
            right = self._coerce(right, FLOAT)

            ops = {
                "+": self.builder.fadd,
                "-": self.builder.fsub,
                "*": self.builder.fmul,
                "/": self.builder.fdiv,
                "%": self.builder.frem
            }

            return ops[op](left, right)

        # Enteros
        left  = self._coerce(left, INT)
        right = self._coerce(right, INT)

        ops = {
            "+": self.builder.add,
            "-": self.builder.sub,
            "*": self.builder.mul,
            "/": self.builder.sdiv,
            "%": self.builder.srem
        }

        return ops[op](left, right)

        
    def _cmp(self, left: ir.Value, right: ir.Value, op: str) -> ir.Value:
        norm = {"<>": "!="}
        op = norm.get(op, op)

        if left.type == FLOAT or right.type == FLOAT:
            left  = self._coerce(left,  FLOAT)
            right = self._coerce(right, FLOAT)
            fmap  = {"==": "oeq", "!=": "one", "<":  "olt",
                     ">":  "ogt", "<=": "ole", ">=": "oge"}
            return self.builder.fcmp_ordered(fmap[op], left, right)

        left  = self._coerce(left,  INT)
        right = self._coerce(right, INT)
        return self.builder.icmp_signed(op, left, right)

    def visitMultiplicacionDivisisionMod(self, ctx: CalculadoraParser.MultiplicacionDivisisionModContext):
        return self._arith(self.visit(ctx.expresion(0)),
                           self.visit(ctx.expresion(1)), ctx.op.text)

    def visitSumaResta(self, ctx: CalculadoraParser.SumaRestaContext):
        return self._arith(self.visit(ctx.expresion(0)),
                           self.visit(ctx.expresion(1)), ctx.op.text)

    def visitRelacional(self, ctx: CalculadoraParser.RelacionalContext):
        return self._cmp(self.visit(ctx.expresion(0)),
                         self.visit(ctx.expresion(1)), ctx.op.text)

    def visitAndOrLogico(self, ctx: CalculadoraParser.AndOrLogicoContext):
        left  = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        if left is None:
            left = ir.Constant(BOOL, 0)
        if right is None:
            right = ir.Constant(BOOL, 0)
        left  = self._coerce(left, BOOL)
        right = self._coerce(right, BOOL)
        if ctx.op.text == "&&":
            return self.builder.and_(left, right)
        return self.builder.or_(left, right)

    def visitLlamadaModulo(self, ctx: CalculadoraParser.LlamadaModuloContext):
        modulo = ctx.ID(0).getText()
        funcion = ctx.ID(1).getText()
        
        # Soportar módulo math con funciones básicas
        if modulo == "math":
            if funcion in ["sqrt", "pow", "sin", "cos"]:
                if funcion == "sqrt":
                    fn_ty = ir.FunctionType(FLOAT, [FLOAT])
                    fn = ir.Function(self.module, fn_ty, name="sqrt")
                    args = [self.visit(e) for e in ctx.expresion()]
                    if args and args[0] is not None:
                        args[0] = self._coerce(args[0], FLOAT)
                        return self.builder.call(fn, [args[0]])
                elif funcion == "pow":
                    fn_ty = ir.FunctionType(FLOAT, [FLOAT, FLOAT])
                    fn = ir.Function(self.module, fn_ty, name="pow")
                    args = [self.visit(e) for e in ctx.expresion()]
                    if len(args) >= 2 and args[0] is not None and args[1] is not None:
                        args[0] = self._coerce(args[0], FLOAT)
                        args[1] = self._coerce(args[1], FLOAT)
                        return self.builder.call(fn, args[:2])
                elif funcion in ["sin", "cos"]:
                    fn_ty = ir.FunctionType(FLOAT, [FLOAT])
                    fn = ir.Function(self.module, fn_ty, name=funcion)
                    args = [self.visit(e) for e in ctx.expresion()]
                    if args and args[0] is not None:
                        args[0] = self._coerce(args[0], FLOAT)
                        return self.builder.call(fn, [args[0]])
        
        return ir.Constant(FLOAT, 0.0)
        name = ctx.ID().getText()
        if name not in self.functions:
            return ir.Constant(INT, 0)

        fn, ret_tipo = self.functions[name]

        args = []
        if ctx.args():
            for i, expr in enumerate(ctx.args().expresion()):
                val = self.visit(expr)
                if val is None:
                    val = ir.Constant(INT, 0)
                if i < len(fn.args):
                    val = self._coerce(val, fn.args[i].type)
                args.append(val)

        result = self.builder.call(fn, args)
        if ret_tipo == "void":
            return ir.Constant(INT, 0)
        return result if result is not None else ir.Constant(INT, 0)

    # ── API pública ───────────────────────────────────────────────

    def get_ir(self) -> str:
        return str(self.module)

    def save(self, path: str):
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.get_ir())
        print(f"[IR] Generado: {path}")

    def verify(self) -> bool:
        try:
            mod = binding.parse_assembly(self.get_ir())
            mod.verify()
            print("[IR] Verificación LLVM: OK")
            return True
        except Exception as e:
            print(f"[IR] Error de verificación: {e}")
            return False
