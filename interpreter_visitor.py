from CalculadoraVisitor import CalculadoraVisitor
from symbol_table import SymbolTable


PRIMITIVE_TYPES = {"int", "float", "string", "bool", "void"}


class BreakSignal(Exception):
    pass


class ContinueSignal(Exception):
    pass


class ReturnSignal(Exception):
    def __init__(self, value):
        self.value = value


class InterpreterVisitor(CalculadoraVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.funciones = {}
        self.struct_types = {}

    # ---------------- helpers ----------------
    def _default_value(self, tipo):
        defaults = {
            "int": 0,
            "float": 0.0,
            "string": "",
            "bool": False,
            "void": None,
        }
        return defaults.get(tipo, None)

    def _is_struct_instance_type(self, tipo):
        return isinstance(tipo, str) and tipo.startswith("struct:")

    def _struct_name(self, tipo):
        if not self._is_struct_instance_type(tipo):
            return None
        return tipo.split(":", 1)[1]

    def _build_struct_instance(self, struct_name):
        campos = self.struct_types.get(struct_name, {})
        return {campo: self._default_value(tipo) for campo, tipo in campos.items()}

    def _truthy(self, val):
        if isinstance(val, bool):
            return val
        if isinstance(val, (int, float)):
            return val != 0
        if isinstance(val, str):
            return len(val) > 0
        return bool(val)

    def _coerce_to_type(self, value, tipo_destino):
        if tipo_destino == "int":
            if isinstance(value, bool):
                return 1 if value else 0
            if isinstance(value, (int, float)):
                return int(value)
            if isinstance(value, str):
                return int(float(value))
        elif tipo_destino == "float":
            if isinstance(value, bool):
                return 1.0 if value else 0.0
            if isinstance(value, (int, float)):
                return float(value)
            if isinstance(value, str):
                return float(value)
        elif tipo_destino == "bool":
            return self._truthy(value)
        elif tipo_destino == "string":
            return str(value)
        return value

    def _lvalue_parts(self, lvalue_ctx):
        return [tok.getText() for tok in lvalue_ctx.ID()]

    def _lookup_var(self, name):
        var = self.symbol_table.lookup(name)
        if not var:
            raise RuntimeError(f"Variable '{name}' no declarada.")
        return var

    def _read_lvalue(self, lvalue_ctx):
        parts = self._lvalue_parts(lvalue_ctx)
        if not parts:
            raise RuntimeError("LValue inválido.")

        base = self._lookup_var(parts[0])
        current = base["value"]

        for field in parts[1:]:
            if not isinstance(current, dict):
                raise RuntimeError(f"'{parts[0]}' no es un struct.")
            if field not in current:
                raise RuntimeError(f"Campo '{field}' no existe en struct.")
            current = current[field]

        return current

    def _write_lvalue(self, lvalue_ctx, value):
        parts = self._lvalue_parts(lvalue_ctx)
        if not parts:
            raise RuntimeError("LValue inválido.")

        if len(parts) == 1:
            self.symbol_table.assign(parts[0], value)
            return value

        base = self._lookup_var(parts[0])
        current = base["value"]
        if not isinstance(current, dict):
            raise RuntimeError(f"'{parts[0]}' no es un struct.")

        for field in parts[1:-1]:
            if field not in current or not isinstance(current[field], dict):
                raise RuntimeError(f"Campo anidado '{field}' no válido.")
            current = current[field]

        last = parts[-1]
        if last not in current:
            raise RuntimeError(f"Campo '{last}' no existe en struct.")
        current[last] = value
        return value

    # ---------------- programa ----------------
    def visitArchivo(self, ctx):
        for inst in ctx.instruccion():
            self.visit(inst)
        return None

    # ---------------- instrucciones ----------------
    def visitInstruccionDeclaracion(self, ctx):
        return self.visit(ctx.declaracion())

    def visitDeclaracion(self, ctx):
        # Alternativa 1: TIPO ID (= expr)?
        if ctx.TIPO():
            tipo = ctx.TIPO().getText()
            nombre = ctx.ID(0).getText()
            valor = self.visit(ctx.expresion()) if ctx.expresion() else self._default_value(tipo)
            self.symbol_table.declare(nombre, tipo, valor)
            return valor

        # Alternativa 2: ID ID (variable struct)
        struct_name = ctx.ID(0).getText()
        var_name = ctx.ID(1).getText()
        if struct_name not in self.struct_types:
            raise RuntimeError(f"Struct '{struct_name}' no declarado.")
        valor = self._build_struct_instance(struct_name)
        self.symbol_table.declare(var_name, f"struct:{struct_name}", valor)
        return valor

    def visitEjecutarAsignacion(self, ctx):
        lval = ctx.asignacion().lvalue()
        valor = self.visit(ctx.asignacion().expresion())
        return self._write_lvalue(lval, valor)

    def visitEjecutarPrint(self, ctx):
        resultado = self.visit(ctx.expresion())
        print(resultado)
        return None

    def visitInstruccionIf(self, ctx):
        condicion = self.visit(ctx.ifStatement().expresion())
        if self._truthy(condicion):
            self.visit(ctx.ifStatement().block(0))
        elif ctx.ifStatement().block(1):
            self.visit(ctx.ifStatement().block(1))
        return None

    def visitInstruccionSwitch(self, ctx):
        self.visit(ctx.switchStatement())
        return None

    def visitSwitchStatement(self, ctx):
        control = self.visit(ctx.expresion())
        try:
            for case_ctx in ctx.caseClause():
                case_val = self.visit(case_ctx.expresion())
                if control == case_val:
                    for inst in case_ctx.instruccion():
                        self.visit(inst)
                    return None

            if ctx.defaultClause():
                for inst in ctx.defaultClause().instruccion():
                    self.visit(inst)
        except BreakSignal:
            return None
        return None

    def visitInstruccionWhile(self, ctx):
        while self._truthy(self.visit(ctx.whileStatement().expresion())):
            try:
                self.visit(ctx.whileStatement().block())
            except ContinueSignal:
                continue
            except BreakSignal:
                break
        return None

    def visitInstruccionFor(self, ctx):
        self.visit(ctx.forStatement())
        return None

    def visitForStatement(self, ctx):
        self.visit(ctx.asignacion(0))
        while self._truthy(self.visit(ctx.expresion())):
            try:
                self.visit(ctx.block())
            except ContinueSignal:
                self.visit(ctx.asignacion(1))
                continue
            except BreakSignal:
                break
            self.visit(ctx.asignacion(1))
        return None

    def visitInstruccionReturn(self, ctx):
        valor = self.visit(ctx.returnStmt().expresion()) if ctx.returnStmt().expresion() else None
        raise ReturnSignal(valor)

    def visitInstruccionFuncion(self, ctx):
        nombre = ctx.funcionDecl().ID().getText()
        self.funciones[nombre] = ctx.funcionDecl()
        return None

    def visitInstruccionStruct(self, ctx):
        self.visit(ctx.structDecl())
        return None

    def visitStructDecl(self, ctx):
        nombre = ctx.ID().getText()
        campos = {}
        for field_ctx in ctx.structFieldDecl():
            campos[field_ctx.ID().getText()] = field_ctx.TIPO().getText()
        self.struct_types[nombre] = campos
        return None

    def visitBreakStmt(self, ctx):
        raise BreakSignal()

    def visitContinueStmt(self, ctx):
        raise ContinueSignal()

    def visitInstruccionBloque(self, ctx):
        self.visit(ctx.block())
        return None

    def visitInstruccionExpresion(self, ctx):
        resultado = self.visit(ctx.expresion())
        if resultado is not None:
            print(f"Resultado: {resultado}")
        return resultado

    def visitBlock(self, ctx):
        self.symbol_table.push_scope()
        try:
            for inst in ctx.instruccion():
                self.visit(inst)
        finally:
            self.symbol_table.pop_scope()
        return None

    # ---------------- funciones ----------------
    def visitLlamadaFuncion(self, ctx):
        nombre = ctx.ID().getText()
        func_ctx = self.funciones.get(nombre)
        if not func_ctx:
            raise RuntimeError(f"Función '{nombre}' no definida.")

        args_valores = [self.visit(arg) for arg in ctx.args().expresion()] if ctx.args() else []
        params_ctx = func_ctx.params()

        self.symbol_table.push_scope()
        try:
            if params_ctx:
                for i in range(len(params_ctx.ID())):
                    p_name = params_ctx.ID(i).getText()
                    p_tipo = params_ctx.TIPO(i).getText()
                    p_val = args_valores[i] if i < len(args_valores) else self._default_value(p_tipo)
                    self.symbol_table.declare(p_name, p_tipo, p_val)

            try:
                self.visit(func_ctx.block())
            except ReturnSignal as ret:
                return ret.value
            return None
        finally:
            self.symbol_table.pop_scope()

    def visitLlamadaModulo(self, ctx):
        import math

        modulo = ctx.ID(0).getText()
        funcion = ctx.ID(1).getText()
        args = [self.visit(expr) for expr in ctx.expresion()]

        modulos_permitidos = {"math": math}
        if modulo not in modulos_permitidos:
            raise RuntimeError(f"Módulo '{modulo}' no reconocido")
        mod = modulos_permitidos[modulo]
        if not hasattr(mod, funcion):
            raise RuntimeError(f"Función '{funcion}' no existe en módulo '{modulo}'")
        return getattr(mod, funcion)(*args)

    # ---------------- expresiones ----------------
    def visitVariable(self, ctx):
        return self._read_lvalue(ctx.lvalue())

    def visitNumero(self, ctx):
        num = ctx.NUMERO().getText()
        return float(num) if "." in num else int(num)

    def visitCadena(self, ctx):
        return ctx.STRING().getText().strip('"')

    def visitBooleano(self, ctx):
        return ctx.BOOLEANO().getText() == "true"

    def visitParentesis(self, ctx):
        return self.visit(ctx.expresion())

    def visitCorchetes(self, ctx):
        return self.visit(ctx.expresion())

    def visitCastExplicito(self, ctx):
        tipo_destino = ctx.TIPO().getText()
        valor = self.visit(ctx.expresion())
        return self._coerce_to_type(valor, tipo_destino)

    def visitNotLogico(self, ctx):
        return not self._truthy(self.visit(ctx.expresion()))

    def visitMultiplicacionDivisisionMod(self, ctx):
        izq = self.visit(ctx.expresion(0))
        der = self.visit(ctx.expresion(1))
        op = ctx.op.text
        if op == "*":
            return izq * der
        if op == "/":
            return izq / der
        return izq % der

    def visitSumaResta(self, ctx):
        izq = self.visit(ctx.expresion(0))
        der = self.visit(ctx.expresion(1))
        if ctx.op.text == "+":
            return izq + der
        return izq - der

    def visitRelacional(self, ctx):
        izq = self.visit(ctx.expresion(0))
        der = self.visit(ctx.expresion(1))
        op = ctx.op.text
        if op == "==":
            return izq == der
        if op in ("!=", "<>"):
            return izq != der
        if op == "<":
            return izq < der
        if op == ">":
            return izq > der
        if op == "<=":
            return izq <= der
        if op == ">=":
            return izq >= der
        return False

    def visitAndOrLogico(self, ctx):
        izq = self._truthy(self.visit(ctx.expresion(0)))
        der = self._truthy(self.visit(ctx.expresion(1)))
        if ctx.op.text == "&&":
            return izq and der
        return izq or der

    def visitTernario(self, ctx):
        cond = self._truthy(self.visit(ctx.expresion(0)))
        if cond:
            return self.visit(ctx.expresion(1))
        return self.visit(ctx.expresion(2))
