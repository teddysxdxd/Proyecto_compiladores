from CalculadoraVisitor import CalculadoraVisitor
from symbol_table import SymbolTable


PRIMITIVE_TYPES = {"int", "float", "string", "bool", "void"}


class SemanticVisitor(CalculadoraVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.errors = []
        self.struct_types = {}

    # ---------------- helpers ----------------
    def _is_numeric(self, tipo):
        return tipo in {"int", "float"}

    def _is_struct_instance(self, tipo):
        return isinstance(tipo, str) and tipo.startswith("struct:")

    def _is_array_type(self, tipo):
        return isinstance(tipo, str) and tipo.startswith("array:")

    def _array_elem_type(self, tipo):
        if not self._is_array_type(tipo):
            return None
        return tipo.split(":", 1)[1]

    def _struct_name(self, tipo):
        if not self._is_struct_instance(tipo):
            return None
        return tipo.split(":", 1)[1]

    def _add_error(self, ctx, mensaje):
        self.errors.append(f"[Error Semántico] Línea {ctx.start.line}: {mensaje}")

    def _is_assignable(self, destino, fuente):
        if destino == "unknown" or fuente == "unknown":
            return True
        if destino == fuente:
            return True
        # Permitir promoción implícita int -> float
        if destino == "float" and fuente == "int":
            return True
        return False

    def _merge_types(self, t1, t2):
        if t1 == "unknown" or t2 == "unknown":
            return "unknown"
        if t1 == t2:
            return t1
        if self._is_numeric(t1) and self._is_numeric(t2):
            return "float" if "float" in (t1, t2) else "int"
        return "unknown"

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

    def _resolve_lvalue_type(self, lvalue_ctx):
        base_id = lvalue_ctx.ID(0).getText() if lvalue_ctx.ID() else None
        if not base_id:
            return "unknown"

        simbolo = self.symbol_table.lookup(base_id)
        if not simbolo:
            self._add_error(lvalue_ctx, f"Variable '{base_id}' no declarada.")
            return "unknown"

        tipo_actual = simbolo["type"]

        for op_kind, campo, expr_ctx in self._iter_lvalue_ops(lvalue_ctx):
            if op_kind == "field":
                if not self._is_struct_instance(tipo_actual):
                    self._add_error(
                        lvalue_ctx,
                        f"'{base_id}' no es struct; acceso a campo '{campo}' inválido.",
                    )
                    return "unknown"

                struct_name = self._struct_name(tipo_actual)
                campos = self.struct_types.get(struct_name)
                if campos is None:
                    self._add_error(lvalue_ctx, f"Tipo struct '{struct_name}' no definido.")
                    return "unknown"
                if campo not in campos:
                    self._add_error(
                        lvalue_ctx, f"El struct '{struct_name}' no tiene el campo '{campo}'."
                    )
                    return "unknown"

                tipo_campo = campos[campo]
                if tipo_campo in PRIMITIVE_TYPES:
                    tipo_actual = tipo_campo
                else:
                    tipo_actual = f"struct:{tipo_campo}"
            elif op_kind == "index":
                if not self._is_array_type(tipo_actual):
                    self._add_error(lvalue_ctx, "Indexación solo válida sobre arreglos.")
                    return "unknown"
                tipo_indice = self.visit(expr_ctx) if expr_ctx else "unknown"
                if tipo_indice not in {"int", "float", "bool", "unknown"}:
                    self._add_error(lvalue_ctx, "El índice del arreglo debe ser numérico.")
                tipo_actual = self._array_elem_type(tipo_actual) or "unknown"
            else:
                self._add_error(lvalue_ctx, "Operación de lvalue no soportada.")
                return "unknown"

        return tipo_actual

    # ---------------- programa ----------------
    def visitArchivo(self, ctx):
        # Primero registrar structs para permitir uso posterior
        for inst in ctx.instruccion():
            if hasattr(inst, "structDecl") and inst.structDecl():
                self.visit(inst)

        # Luego el resto de instrucciones
        for inst in ctx.instruccion():
            if hasattr(inst, "structDecl") and inst.structDecl():
                continue
            self.visit(inst)
        return None

    # ---------------- structs ----------------
    def visitInstruccionStruct(self, ctx):
        self.visit(ctx.structDecl())
        return None

    def visitStructDecl(self, ctx):
        nombre = ctx.ID().getText()
        if nombre in PRIMITIVE_TYPES:
            self._add_error(ctx, f"'{nombre}' no puede usarse como nombre de struct.")
            return None
        if nombre in self.struct_types:
            self._add_error(ctx, f"El struct '{nombre}' ya fue declarado.")
            return None

        campos = {}
        for field_ctx in ctx.structFieldDecl():
            tipo = field_ctx.TIPO().getText()
            campo = field_ctx.ID().getText()
            if campo in campos:
                self._add_error(
                    field_ctx, f"Campo '{campo}' duplicado en struct '{nombre}'."
                )
                continue
            campos[campo] = tipo

        self.struct_types[nombre] = campos
        return None

    # ---------------- funciones ----------------
    def visitInstruccionFuncion(self, ctx):
        nombre = ctx.funcionDecl().ID().getText()
        tipo_retorno = ctx.funcionDecl().TIPO().getText()

        try:
            self.symbol_table.declare(nombre, tipo_retorno)
        except Exception as e:
            self.errors.append(str(e))

        self.symbol_table.push_scope()

        params_ctx = ctx.funcionDecl().params()
        if params_ctx:
            for i in range(len(params_ctx.ID())):
                p_nombre = params_ctx.ID(i).getText()
                p_tipo = params_ctx.TIPO(i).getText()
                try:
                    self.symbol_table.declare(p_nombre, p_tipo)
                except Exception as e:
                    self.errors.append(str(e))

        self.visit(ctx.funcionDecl().block())
        self.symbol_table.pop_scope()
        return None

    def visitLlamadaFuncion(self, ctx):
        nombre = ctx.ID().getText()
        func = self.symbol_table.lookup(nombre)
        if not func:
            self._add_error(ctx, f"La función '{nombre}' no ha sido definida.")
            return "unknown"

        if ctx.args():
            for arg in ctx.args().expresion():
                self.visit(arg)

        return func["type"]

    # ---------------- declaraciones / asignaciones ----------------
    def visitInstruccionDeclaracion(self, ctx):
        self.visit(ctx.declaracion())
        return None

    def visitDeclaracion(self, ctx):
        # Alternativa 2: TIPO [] ID = [expr, ...] (arreglo)
        if ctx.TIPO() and len(ctx.CORCHI()) >= 2:
            tipo_elem = ctx.TIPO().getText()
            nombre = ctx.ID(0).getText()
            exprs = ctx.expresion()
            if not exprs:
                self._add_error(ctx, "Un arreglo debe inicializarse con al menos un valor.")
                return None

            for expr_ctx in exprs:
                tipo_exp = self.visit(expr_ctx)
                if not self._is_assignable(tipo_elem, tipo_exp):
                    self._add_error(
                        ctx,
                        f"No se puede asignar {tipo_exp} a elemento de arreglo {tipo_elem}.",
                    )

            try:
                self.symbol_table.declare(nombre, f"array:{tipo_elem}")
            except Exception as e:
                self.errors.append(str(e))
            return None

        # Alternativa 1: TIPO ID (= expr)?
        if ctx.TIPO():
            tipo = ctx.TIPO().getText()
            nombre = ctx.ID(0).getText()
            exprs = ctx.expresion()
            expr_ctx = exprs[0] if exprs else None

            if expr_ctx:
                tipo_exp = self.visit(expr_ctx)
                if not self._is_assignable(tipo, tipo_exp):
                    self._add_error(
                        ctx, f"No se puede asignar {tipo_exp} a variable de tipo {tipo}."
                    )

            try:
                self.symbol_table.declare(nombre, tipo)
            except Exception as e:
                self.errors.append(str(e))
            return None

        # Alternativa 2: ID ID  (declaración de variable struct)
        tipo_struct = ctx.ID(0).getText()
        nombre_var = ctx.ID(1).getText()

        if tipo_struct not in self.struct_types:
            self._add_error(ctx, f"El tipo struct '{tipo_struct}' no está declarado.")
            return None

        try:
            self.symbol_table.declare(nombre_var, f"struct:{tipo_struct}")
        except Exception as e:
            self.errors.append(str(e))
        return None

    def visitEjecutarAsignacion(self, ctx):
        tipo_destino = self._resolve_lvalue_type(ctx.asignacion().lvalue())
        tipo_fuente = self.visit(ctx.asignacion().expresion())
        if not self._is_assignable(tipo_destino, tipo_fuente):
            self._add_error(
                ctx,
                f"Incompatibilidad de tipos en asignación ({tipo_fuente} -> {tipo_destino}).",
            )
        return None

    # ---------------- control de flujo ----------------
    def visitInstruccionIf(self, ctx):
        tipo_cond = self.visit(ctx.ifStatement().expresion())
        if tipo_cond not in {"bool", "int", "float"}:
            self._add_error(ctx, "La condición de if debe ser booleana o numérica.")
        self.visit(ctx.ifStatement().block(0))
        if ctx.ifStatement().block(1):
            self.visit(ctx.ifStatement().block(1))
        return None

    def visitInstruccionSwitch(self, ctx):
        self.visit(ctx.switchStatement())
        return None

    def visitSwitchStatement(self, ctx):
        tipo_control = self.visit(ctx.expresion())
        if tipo_control not in {"int", "float", "bool", "string"}:
            self._add_error(ctx, "switch solo acepta tipos primitivos.")

        for case_ctx in ctx.caseClause():
            tipo_case = self.visit(case_ctx.expresion())
            combinacion = self._merge_types(tipo_control, tipo_case)
            if combinacion == "unknown" and not (
                tipo_control == "string" and tipo_case == "string"
            ):
                self._add_error(
                    case_ctx,
                    f"Tipo de case ({tipo_case}) incompatible con switch ({tipo_control}).",
                )
            for inst in case_ctx.instruccion():
                self.visit(inst)

        if ctx.defaultClause():
            for inst in ctx.defaultClause().instruccion():
                self.visit(inst)
        return None

    def visitInstruccionWhile(self, ctx):
        tipo_cond = self.visit(ctx.whileStatement().expresion())
        if tipo_cond not in {"bool", "int", "float"}:
            self._add_error(ctx, "La condición de while debe ser booleana o numérica.")
        self.visit(ctx.whileStatement().block())
        return None

    def visitInstruccionFor(self, ctx):
        self.visit(ctx.forStatement())
        return None

    def visitForStatement(self, ctx):
        self.symbol_table.push_scope()
        self.visit(ctx.asignacion(0))
        tipo_cond = self.visit(ctx.expresion())
        if tipo_cond not in {"bool", "int", "float"}:
            self._add_error(ctx, "La condición del for debe ser booleana o numérica.")
        self.visit(ctx.block())
        self.visit(ctx.asignacion(1))
        self.symbol_table.pop_scope()
        return None

    def visitBlock(self, ctx):
        self.symbol_table.push_scope()
        for inst in ctx.instruccion():
            self.visit(inst)
        self.symbol_table.pop_scope()
        return None

    # ---------------- expresiones ----------------
    def visitVariable(self, ctx):
        return self._resolve_lvalue_type(ctx.lvalue())

    def visitLvalue(self, ctx):
        return self._resolve_lvalue_type(ctx)

    def visitNumero(self, ctx):
        return "float" if "." in ctx.NUMERO().getText() else "int"

    def visitCadena(self, ctx):
        return "string"

    def visitBooleano(self, ctx):
        return "bool"

    def visitCastExplicito(self, ctx):
        destino = ctx.TIPO().getText()
        origen = self.visit(ctx.expresion())

        if destino == "void":
            self._add_error(ctx, "No se permite casting explícito a void.")
            return "unknown"
        if origen == "unknown":
            return "unknown"
        if origen.startswith("struct:"):
            self._add_error(ctx, "No se permite casting de structs a tipos primitivos.")
            return "unknown"
        return destino

    def visitTernario(self, ctx):
        tipo_cond = self.visit(ctx.expresion(0))
        if tipo_cond not in {"bool", "int", "float"}:
            self._add_error(ctx, "La condición del ternario debe ser booleana o numérica.")

        tipo_true = self.visit(ctx.expresion(1))
        tipo_false = self.visit(ctx.expresion(2))
        merged = self._merge_types(tipo_true, tipo_false)

        if merged == "unknown":
            self._add_error(
                ctx,
                f"Las ramas del ternario son incompatibles: {tipo_true} y {tipo_false}.",
            )
        return merged

    def visitSumaResta(self, ctx):
        t1 = self.visit(ctx.expresion(0))
        t2 = self.visit(ctx.expresion(1))

        if ctx.op.text == "+":
            if t1 == "string" or t2 == "string":
                return "string"
            if self._is_numeric(t1) and self._is_numeric(t2):
                return "float" if "float" in (t1, t2) else "int"
            self._add_error(ctx, "No se puede sumar esos tipos.")
            return "unknown"

        # resta
        if self._is_numeric(t1) and self._is_numeric(t2):
            return "float" if "float" in (t1, t2) else "int"
        self._add_error(ctx, "La resta solo aplica a tipos numéricos.")
        return "unknown"

    def visitRelacional(self, ctx):
        self.visit(ctx.expresion(0))
        self.visit(ctx.expresion(1))
        return "bool"

    def visitMultiplicacionDivisisionMod(self, ctx):
        t1 = self.visit(ctx.expresion(0))
        t2 = self.visit(ctx.expresion(1))
        if not self._is_numeric(t1) or not self._is_numeric(t2):
            self._add_error(ctx, "Operación aritmética inválida para tipos no numéricos.")
            return "unknown"
        return "float" if "float" in (t1, t2) else "int"

    def visitAndOrLogico(self, ctx):
        self.visit(ctx.expresion(0))
        self.visit(ctx.expresion(1))
        return "bool"

    def visitNotLogico(self, ctx):
        self.visit(ctx.expresion())
        return "bool"

    # ---------------- otras instrucciones ----------------
    def visitInstruccionBloque(self, ctx):
        self.visit(ctx.block())
        return None

    def visitBreakStmt(self, ctx):
        return None

    def visitContinueStmt(self, ctx):
        return None

    def visitInstruccionExpresion(self, ctx):
        self.visit(ctx.expresion())
        return None

    def visitEjecutarPrint(self, ctx):
        self.visit(ctx.expresion())
        return None

    def visitInstruccionReturn(self, ctx):
        expr = ctx.returnStmt().expresion()
        if expr:
            return self.visit(expr)
        return None

    def visitLlamadaModulo(self, ctx):
        modulo = ctx.ID(0).getText()
        funcion = ctx.ID(1).getText()

        if modulo == "math":
            if funcion in ["sqrt", "pow", "sin", "cos"]:
                return "float"
            self._add_error(
                ctx, f"Función '{funcion}' no existe en módulo '{modulo}'."
            )
            return "unknown"

        self._add_error(ctx, f"Módulo '{modulo}' no reconocido.")
        return "unknown"
