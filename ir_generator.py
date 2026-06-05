# ir_generator.py
# Generador de LLVM IR usando llvmlite 0.47+
# Compatible con gramatica_v4.g4 rama desarrollo
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
from gramatica_v4Parser import gramatica_v4Parser
from gramatica_v4Visitor import gramatica_v4Visitor


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
class IRGenerator(gramatica_v4Visitor):

    def __init__(self):
        self.module   = ir.Module(name="programa")
        self.module.triple = "x86_64-pc-linux-gnu"

        self.builder: ir.IRBuilder = None
        self.scope    = None
        self.functions = {}          # name -> (ir.Function, ret_tipo_str)
        self.current_ret_tipo = None # tipo_str de la función actual
        self.struct_types = {}       # nombre -> IdentifiedStructType
        self.struct_fields = {}      # nombre -> [(field_name, field_tipo_str)]
        self.struct_index = {}       # nombre -> {field_name: idx}
        self.break_targets = []      # stack de bloques destino para break
        self.continue_targets = []   # stack de bloques destino para continue
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

    def _is_struct_instance_type(self, tipo_str: str) -> bool:
        return isinstance(tipo_str, str) and tipo_str.startswith("struct:")

    def _is_array_instance_type(self, tipo_str: str) -> bool:
        return isinstance(tipo_str, str) and tipo_str.startswith("array:")

    def _array_meta_from_type(self, tipo_str: str):
        if not self._is_array_instance_type(tipo_str):
            return None, None
        parts = tipo_str.split(":")
        elem_tipo = parts[1] if len(parts) > 1 else None
        arr_len = None
        if len(parts) > 2:
            try:
                arr_len = int(parts[2])
            except Exception:
                arr_len = None
        return elem_tipo, arr_len

    def _struct_name_from_instance_type(self, tipo_str: str):
        if not self._is_struct_instance_type(tipo_str):
            return None
        return tipo_str.split(":", 1)[1]

    def _llvm_type_for_name(self, tipo_str: str) -> ir.Type:
        if self._is_struct_instance_type(tipo_str):
            sname = self._struct_name_from_instance_type(tipo_str)
            return self.struct_types.get(sname, INT)
        if self._is_array_instance_type(tipo_str):
            elem_tipo, _ = self._array_meta_from_type(tipo_str)
            return self._llvm_type_for_name(elem_tipo or "int")
        if tipo_str in self.struct_types:
            return self.struct_types[tipo_str]
        return llvm_type(tipo_str)

    def _default_val_for_type(self, tipo_str: str):
        if self._is_struct_instance_type(tipo_str):
            st = self._llvm_type_for_name(tipo_str)
            return ir.Constant(st, None)
        return default_val(tipo_str)

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
                yield (("index", None, expr_ctx))
                expr_i += 1
                i += 3
            else:
                i += 1

    def _resolve_lvalue_ptr_and_type(self, lvalue_ctx):
        if not lvalue_ctx.ID():
            return None, None

        base_name = lvalue_ctx.ID(0).getText()
        ptr, tipo_str = self.scope.lookup(base_name)
        if ptr is None:
            return None, None

        current_ptr = ptr
        current_tipo = tipo_str

        for op_kind, field, expr_ctx in self._iter_lvalue_ops(lvalue_ctx):
            if op_kind == "field":
                if not self._is_struct_instance_type(current_tipo):
                    return None, None

                sname = self._struct_name_from_instance_type(current_tipo)
                fmap = self.struct_index.get(sname, {})
                fmeta = self.struct_fields.get(sname, [])
                if field not in fmap:
                    return None, None

                idx = fmap[field]
                field_name, field_tipo = fmeta[idx]
                _ = field_name

                current_ptr = self.builder.gep(
                    current_ptr,
                    [ir.Constant(INT, 0), ir.Constant(INT, idx)],
                    inbounds=True,
                )
                if field_tipo in self.struct_types:
                    current_tipo = f"struct:{field_tipo}"
                else:
                    current_tipo = field_tipo

            elif op_kind == "index":
                if not self._is_array_instance_type(current_tipo):
                    return None, None
                elem_tipo, _ = self._array_meta_from_type(current_tipo)
                index_val = self.visit(expr_ctx) if expr_ctx else ir.Constant(INT, 0)
                if index_val is None:
                    index_val = ir.Constant(INT, 0)
                index_val = self._coerce(index_val, INT)
                current_ptr = self.builder.gep(
                    current_ptr,
                    [ir.Constant(INT, 0), index_val],
                    inbounds=True,
                )
                current_tipo = elem_tipo or "int"
            else:
                return None, None

        return current_ptr, current_tipo

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

    def visitArchivo(self, ctx: gramatica_v4Parser.ArchivoContext):
        # Registrar tipos struct antes de generar cuerpos que los usen
        for inst in ctx.instruccion():
            if hasattr(inst, "structDecl") and inst.structDecl():
                self.visit(inst.structDecl())

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

    def visitInstruccionSwitch(self, ctx):
        self.visit(ctx.switchStatement())

    def visitInstruccionWhile(self, ctx):
        self.visit(ctx.whileStatement())

    def visitInstruccionFor(self, ctx):
        self.visit(ctx.forStatement())

    def visitInstruccionReturn(self, ctx):
        self.visit(ctx.returnStmt())

    def visitInstruccionFuncion(self, ctx):
        self.visit(ctx.funcionDecl())

    def visitInstruccionStruct(self, ctx):
        self.visit(ctx.structDecl())

    def visitInstruccionExpresion(self, ctx):
        self.visit(ctx.expresion())   # llamada standalone; resultado descartado

    def visitInstruccionBloque(self, ctx):
        self.visit(ctx.block())

    def visitStructDecl(self, ctx: gramatica_v4Parser.StructDeclContext):
        sname = ctx.ID().getText()
        if sname in self.struct_types:
            return

        field_meta = []
        field_ir_types = []
        for fctx in ctx.structFieldDecl():
            ftype = fctx.TIPO().getText()
            fname = fctx.ID().getText()
            field_meta.append((fname, ftype))
            field_ir_types.append(self._llvm_type_for_name(ftype))

        st = self.module.context.get_identified_type(f"fstruct.{sname}")
        st.set_body(*field_ir_types)
        self.struct_types[sname] = st
        self.struct_fields[sname] = field_meta
        self.struct_index[sname] = {name: idx for idx, (name, _) in enumerate(field_meta)}

    # ── declaración ───────────────────────────────────────────────

    def visitDeclaracion(self, ctx: gramatica_v4Parser.DeclaracionContext):
        # TIPO [] ID = [expr, ...]
        if ctx.TIPO() and len(ctx.CORCHI()) >= 2:
            tipo_elem = ctx.TIPO().getText()
            name = ctx.ID(0).getText()
            exprs = ctx.expresion()
            if not exprs:
                return

            elem_ty = self._llvm_type_for_name(tipo_elem)
            arr_len = len(exprs)
            arr_ty = ir.ArrayType(elem_ty, arr_len)
            alloca = self._alloca(name, arr_ty)
            self.scope.define(name, alloca, f"array:{tipo_elem}:{arr_len}")

            for idx, expr_ctx in enumerate(exprs):
                elem_ptr = self.builder.gep(
                    alloca,
                    [ir.Constant(INT, 0), ir.Constant(INT, idx)],
                    inbounds=True,
                )
                val = self.visit(expr_ctx)
                if val is None:
                    val = self._default_val_for_type(tipo_elem)
                val = self._coerce(val, elem_ty)
                self.builder.store(val, elem_ptr)
            return

        # TIPO ID (= expr)?
        if ctx.TIPO():
            tipo_str = ctx.TIPO().getText()
            name     = ctx.ID(0).getText()
            ltype    = self._llvm_type_for_name(tipo_str)

            alloca = self._alloca(name, ltype)
            self.scope.define(name, alloca, tipo_str)

            exprs = ctx.expresion()
            expr_ctx = exprs[0] if exprs else None
            if expr_ctx:
                val = self._coerce(self.visit(expr_ctx), ltype)
            else:
                val = self._default_val_for_type(tipo_str)

            self.builder.store(val, alloca)
            return

        # ID ID  (declaración de variable struct)
        struct_name = ctx.ID(0).getText()
        var_name = ctx.ID(1).getText()
        st = self.struct_types.get(struct_name)
        if st is None:
            return

        alloca = self._alloca(var_name, st)
        self.scope.define(var_name, alloca, f"struct:{struct_name}")
        self.builder.store(ir.Constant(st, None), alloca)

    # ── asignación ────────────────────────────────────────────────

    def visitAsignacion(self, ctx: gramatica_v4Parser.AsignacionContext):
        lvalue_ctx = ctx.lvalue()
        ops = list(self._iter_lvalue_ops(lvalue_ctx))
        rval = self.visit(ctx.expresion())

        if not lvalue_ctx.ID():
            return

        # Asignación simple con autodeclaración para compatibilidad histórica
        if not ops:
            name = lvalue_ctx.ID(0).getText()
            alloca, tipo_str = self.scope.lookup(name)
            if alloca is None:
                tipo_str = tipo_str_from_llvm(rval.type)
                alloca = self._alloca(name, rval.type)
                self.scope.define(name, alloca, tipo_str)

            target_ty = self._llvm_type_for_name(tipo_str)
            rval = self._coerce(rval, target_ty)
            self.builder.store(rval, alloca)
            return

        # Asignación compuesta (obj.campo = expr, arr[i] = expr)
        ptr, tipo_str = self._resolve_lvalue_ptr_and_type(lvalue_ctx)
        if ptr is None or tipo_str is None:
            return
        target_ty = self._llvm_type_for_name(tipo_str)
        rval = self._coerce(rval, target_ty)
        self.builder.store(rval, ptr)

    # ── return ────────────────────────────────────────────────────

    def visitReturnStmt(self, ctx: gramatica_v4Parser.ReturnStmtContext):
        if self.builder.block.is_terminated:
            return

        ret_ltype = self._llvm_type_for_name(self.current_ret_tipo or "int")

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

    def visitFuncionDecl(self, ctx: gramatica_v4Parser.FuncionDeclContext):
        ret_tipo = ctx.TIPO().getText()
        name     = ctx.ID().getText()

        param_tipos = []
        param_names = []
        if ctx.params():
            p = ctx.params()
            param_tipos = [t.getText() for t in p.TIPO()]
            param_names = [i.getText() for i in p.ID()]

        fn_ty = ir.FunctionType(
            self._llvm_type_for_name(ret_tipo),
            [self._llvm_type_for_name(t) for t in param_tipos],
        )
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
            alloca = self._alloca(pname, self._llvm_type_for_name(ptyp))
            self.builder.store(arg, alloca)
            self.scope.define(pname, alloca, ptyp)

        # Cuerpo
        self.visit(ctx.block())

        # Ret implícito si el bloque no terminó
        if not self.builder.block.is_terminated:
            if self._llvm_type_for_name(ret_tipo) == VOID:
                self.builder.ret_void()
            else:
                self.builder.ret(ir.Constant(self._llvm_type_for_name(ret_tipo), 0))

        # Restaurar contexto
        self.builder          = prev_builder
        self.scope            = prev_scope
        self.current_ret_tipo = prev_ret_tipo

    # ── bloque ────────────────────────────────────────────────────

    def visitBlock(self, ctx: gramatica_v4Parser.BlockContext):
        self.scope = Scope(parent=self.scope)
        for inst in ctx.instruccion():
            if self.builder.block.is_terminated:
                break
            self.visit(inst)
        self.scope = self.scope.parent

    # ── if / if-else ──────────────────────────────────────────────

    def visitIfStatement(self, ctx: gramatica_v4Parser.IfStatementContext):
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

    def visitSwitchStatement(self, ctx: gramatica_v4Parser.SwitchStatementContext):
        fn = self.builder.function
        control = self.visit(ctx.expresion())

        end_bb = fn.append_basic_block("switch_end")
        default_bb = fn.append_basic_block("switch_default")
        current_test_bb = self.builder.block

        case_blocks = []
        for _ in ctx.caseClause():
            case_blocks.append(fn.append_basic_block("switch_case"))

        # Crear cadena de tests
        for idx, case_ctx in enumerate(ctx.caseClause()):
            is_last = idx == (len(ctx.caseClause()) - 1)
            next_test_bb = None if is_last else fn.append_basic_block(f"switch_test_{idx + 1}")
            self.builder.position_at_end(current_test_bb)

            case_val = self.visit(case_ctx.expresion())
            case_val = self._coerce(case_val, control.type)
            cond = self._cmp(control, case_val, "==")

            target_if_false = next_test_bb if next_test_bb is not None else default_bb
            self.builder.cbranch(cond, case_blocks[idx], target_if_false)

            if next_test_bb is not None:
                current_test_bb = next_test_bb

        self.break_targets.append(end_bb)
        try:
            # Bloques case
            for idx, case_ctx in enumerate(ctx.caseClause()):
                self.builder.position_at_end(case_blocks[idx])
                for inst in case_ctx.instruccion():
                    if self.builder.block.is_terminated:
                        break
                    self.visit(inst)
                if not self.builder.block.is_terminated:
                    self.builder.branch(end_bb)

            # default
            self.builder.position_at_end(default_bb)
            if ctx.defaultClause():
                for inst in ctx.defaultClause().instruccion():
                    if self.builder.block.is_terminated:
                        break
                    self.visit(inst)
            if not self.builder.block.is_terminated:
                self.builder.branch(end_bb)
        finally:
            self.break_targets.pop()

        self.builder.position_at_end(end_bb)

    # ── while ─────────────────────────────────────────────────────

    def visitWhileStatement(self, ctx: gramatica_v4Parser.WhileStatementContext):
        fn = self.builder.function
        cond_bb = fn.append_basic_block("while_cond")
        body_bb = fn.append_basic_block("while_body")
        end_bb  = fn.append_basic_block("while_end")

        self.builder.branch(cond_bb)

        self.builder.position_at_end(cond_bb)
        cond = self._coerce(self.visit(ctx.expresion()), BOOL)
        self.builder.cbranch(cond, body_bb, end_bb)

        self.builder.position_at_end(body_bb)
        self.break_targets.append(end_bb)
        self.continue_targets.append(cond_bb)
        try:
            self.visit(ctx.block())
        finally:
            self.continue_targets.pop()
            self.break_targets.pop()
        if not self.builder.block.is_terminated:
            self.builder.branch(cond_bb)

        self.builder.position_at_end(end_bb)

    # ── for ───────────────────────────────────────────────────────

    def visitForStatement(self, ctx: gramatica_v4Parser.ForStatementContext):
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
        self.break_targets.append(end_bb)
        self.continue_targets.append(incr_bb)
        try:
            self.visit(ctx.block())
        finally:
            self.continue_targets.pop()
            self.break_targets.pop()
        if not self.builder.block.is_terminated:
            self.builder.branch(incr_bb)

        self.builder.position_at_end(incr_bb)
        self.visit(asigs[1])
        self.builder.branch(cond_bb)

        self.builder.position_at_end(end_bb)

    # ── other methods continue, unchanged

    def visitBreakStmt(self, ctx):
        if not self.break_targets:
            return
        if not self.builder.block.is_terminated:
            self.builder.branch(self.break_targets[-1])

    def visitContinueStmt(self, ctx):
        if not self.continue_targets:
            return
        if not self.builder.block.is_terminated:
            self.builder.branch(self.continue_targets[-1])

    # ── expresiones ───────────────────────────────────────────────

    def visitNumero(self, ctx: gramatica_v4Parser.NumeroContext):
        txt = ctx.NUMERO().getText()
        if "." in txt:
            return ir.Constant(FLOAT, float(txt))
        return ir.Constant(INT, int(txt))

    def visitCadena(self, ctx: gramatica_v4Parser.CadenaContext):
        raw  = ctx.STRING().getText()[1:-1]       # quitar comillas
        gvar = self._global_str(raw)
        return self._str_ptr(gvar)

    def visitBooleano(self, ctx: gramatica_v4Parser.BooleanoContext):
        return ir.Constant(BOOL, 1 if ctx.BOOLEANO().getText() == "true" else 0)

    def visitVariable(self, ctx: gramatica_v4Parser.VariableContext):
        ptr, tipo_str = self._resolve_lvalue_ptr_and_type(ctx.lvalue())
        if ptr is None:
            return ir.Constant(INT, 0)
        if tipo_str is None:
            return ir.Constant(INT, 0)
        return self.builder.load(ptr)

    def visitParentesis(self, ctx: gramatica_v4Parser.ParentesisContext):
        return self.visit(ctx.expresion())

    def visitCorchetes(self, ctx: gramatica_v4Parser.CorchetesContext):
        return self.visit(ctx.expresion())

    def visitCastExplicito(self, ctx: gramatica_v4Parser.CastExplicitoContext):
        val = self.visit(ctx.expresion())
        target = self._llvm_type_for_name(ctx.TIPO().getText())
        return self._coerce(val, target)

    def visitNotLogico(self, ctx: gramatica_v4Parser.NotLogicoContext):
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

    def visitMultiplicacionDivisisionMod(self, ctx: gramatica_v4Parser.MultiplicacionDivisisionModContext):
        return self._arith(self.visit(ctx.expresion(0)),
                           self.visit(ctx.expresion(1)), ctx.op.text)

    def visitSumaResta(self, ctx: gramatica_v4Parser.SumaRestaContext):
        return self._arith(self.visit(ctx.expresion(0)),
                           self.visit(ctx.expresion(1)), ctx.op.text)

    def visitRelacional(self, ctx: gramatica_v4Parser.RelacionalContext):
        return self._cmp(self.visit(ctx.expresion(0)),
                         self.visit(ctx.expresion(1)), ctx.op.text)

    def visitAndOrLogico(self, ctx: gramatica_v4Parser.AndOrLogicoContext):
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

    def visitTernario(self, ctx: gramatica_v4Parser.TernarioContext):
        cond = self._coerce(self.visit(ctx.expresion(0)), BOOL)
        true_val = self.visit(ctx.expresion(1))
        false_val = self.visit(ctx.expresion(2))

        result_ty = true_val.type
        if false_val.type != result_ty:
            if true_val.type == FLOAT or false_val.type == FLOAT:
                result_ty = FLOAT
            elif true_val.type in (INT, BOOL) and false_val.type in (INT, BOOL):
                result_ty = INT

        true_val = self._coerce(true_val, result_ty)
        false_val = self._coerce(false_val, result_ty)

        fn = self.builder.function
        then_bb = fn.append_basic_block("ternary_then")
        else_bb = fn.append_basic_block("ternary_else")
        merge_bb = fn.append_basic_block("ternary_merge")

        self.builder.cbranch(cond, then_bb, else_bb)

        self.builder.position_at_end(then_bb)
        self.builder.branch(merge_bb)
        then_bb = self.builder.block

        self.builder.position_at_end(else_bb)
        self.builder.branch(merge_bb)
        else_bb = self.builder.block

        self.builder.position_at_end(merge_bb)
        phi = self.builder.phi(result_ty)
        phi.add_incoming(true_val, then_bb)
        phi.add_incoming(false_val, else_bb)
        return phi

    def visitLlamadaFuncion(self, ctx: gramatica_v4Parser.LlamadaFuncionContext):
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

    def visitLlamadaModulo(self, ctx: gramatica_v4Parser.LlamadaModuloContext):
        modulo = ctx.ID(0).getText()
        funcion = ctx.ID(1).getText()
        
        # Soportar módulo math con funciones básicas
        if modulo == "math":
            if funcion in ["sqrt", "pow", "sin", "cos"]:
                if funcion == "sqrt":
                    fn_ty = ir.FunctionType(FLOAT, [FLOAT])
                    fn = self.module.globals.get("sqrt")
                    if not isinstance(fn, ir.Function):
                        fn = ir.Function(self.module, fn_ty, name="sqrt")
                    args = [self.visit(e) for e in ctx.expresion()]
                    if args and args[0] is not None:
                        args[0] = self._coerce(args[0], FLOAT)
                        return self.builder.call(fn, [args[0]])
                elif funcion == "pow":
                    fn_ty = ir.FunctionType(FLOAT, [FLOAT, FLOAT])
                    fn = self.module.globals.get("pow")
                    if not isinstance(fn, ir.Function):
                        fn = ir.Function(self.module, fn_ty, name="pow")
                    args = [self.visit(e) for e in ctx.expresion()]
                    if len(args) >= 2 and args[0] is not None and args[1] is not None:
                        args[0] = self._coerce(args[0], FLOAT)
                        args[1] = self._coerce(args[1], FLOAT)
                        return self.builder.call(fn, args[:2])
                elif funcion in ["sin", "cos"]:
                    fn_ty = ir.FunctionType(FLOAT, [FLOAT])
                    fn = self.module.globals.get(funcion)
                    if not isinstance(fn, ir.Function):
                        fn = ir.Function(self.module, fn_ty, name=funcion)
                    args = [self.visit(e) for e in ctx.expresion()]
                    if args and args[0] is not None:
                        args[0] = self._coerce(args[0], FLOAT)
                        return self.builder.call(fn, [args[0]])

        return ir.Constant(FLOAT, 0.0)

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
