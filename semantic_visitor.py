from CalculadoraVisitor import CalculadoraVisitor
from symbol_table import SymbolTable

class SemanticVisitor(CalculadoraVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.errors = []

    def visitArchivo(self, ctx):
        for inst in ctx.instruccion():
            self.visit(inst)
        return None

    # --- Manejo de Funciones (Nuevo) ---
    def visitInstruccionFuncion(self, ctx):
        nombre = ctx.funcionDecl().ID().getText()
        tipo_retorno = ctx.funcionDecl().TIPO().getText()
        
        # 1. Registrar la función en el ámbito global para permitir recursividad
        try:
            self.symbol_table.declare(nombre, tipo_retorno)
        except Exception as e:
            self.errors.append(str(e))

        # 2. Nuevo Scope para los parámetros y el cuerpo de la función
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
        
        # 3. Visitar el bloque de la función
        self.visit(ctx.funcionDecl().block())
        
        # 4. Salir del Scope de la función
        self.symbol_table.pop_scope()
        return None

    def visitLlamadaFuncion(self, ctx):
        nombre = ctx.ID().getText()
        func = self.symbol_table.lookup(nombre)
        if not func:
            self.errors.append(f"[Error Semántico] Línea {ctx.start.line}: La función '{nombre}' no ha sido definida.")
            return "unknown"
        
        # Validar argumentos (opcional: podrías validar que la cantidad coincida)
        if ctx.args():
            for arg in ctx.args().expresion():
                self.visit(arg)
                
        return func['type']

    # --- Declaraciones y Asignaciones ---
    def visitInstruccionDeclaracion(self, ctx):
        tipo = ctx.declaracion().TIPO().getText()
        nombre = ctx.declaracion().ID().getText()
        
        if ctx.declaracion().expresion():
            tipo_exp = self.visit(ctx.declaracion().expresion())
            if tipo_exp != tipo and not (tipo == "float" and tipo_exp == "int"):
                self.errors.append(f"[Error Semántico] Línea {ctx.start.line}: No se puede asignar {tipo_exp} a {tipo}.")
        
        try:
            self.symbol_table.declare(nombre, tipo)
        except Exception as e:
            self.errors.append(str(e))
        return None

    def visitEjecutarAsignacion(self, ctx):
        nombre = ctx.asignacion().ID().getText()
        tipo_exp = self.visit(ctx.asignacion().expresion())
        
        var = self.symbol_table.lookup(nombre)
        if not var:
            self.errors.append(f"[Error Semántico] Línea {ctx.start.line}: Variable '{nombre}' no declarada.")
        elif var['type'] != tipo_exp and not (var['type'] == "float" and tipo_exp == "int"):
            self.errors.append(f"[Error Semántico] Línea {ctx.start.line}: Incompatibilidad de tipos en asignación a '{nombre}'.")
        return None

    # --- Estructuras de Control ---
    def visitInstruccionIf(self, ctx):
        self.visit(ctx.ifStatement().expresion())
        self.visit(ctx.ifStatement().block(0))
        if ctx.ifStatement().block(1):
            self.visit(ctx.ifStatement().block(1))
        return None

    def visitInstruccionWhile(self, ctx):
        self.visit(ctx.whileStatement().expresion())
        self.visit(ctx.whileStatement().block())
        return None

    def visitBlock(self, ctx):
        self.symbol_table.push_scope() # Manejo de Scopes para { } [cite: 42]
        for inst in ctx.instruccion():
            self.visit(inst)
        self.symbol_table.pop_scope() # Pop al salir [cite: 43]
        return None

    # --- Expresiones y Tipos Primitivos ---
    def visitVariable(self, ctx):
        nombre = ctx.ID().getText()
        var = self.symbol_table.lookup(nombre)
        if not var:
            self.errors.append(f"[Error Semántico] Línea {ctx.start.line}: Variable '{nombre}' no declarada.")
            return "unknown"
        return var['type']

    def visitNumero(self, ctx):
        return "float" if "." in ctx.NUMERO().getText() else "int"

    def visitCadena(self, ctx):
        return "string"

    def visitBooleano(self, ctx):
        return "bool"

    def visitSumaResta(self, ctx):
        t1 = self.visit(ctx.expresion(0))
        t2 = self.visit(ctx.expresion(1))
        if t1 == "string" or t2 == "string":
            self.errors.append(f"[Error Semántico] Línea {ctx.start.line}: Operación no válida con strings.")
            return "unknown"
        return "float" if t1 == "float" or t2 == "float" else "int"

    def visitRelacional(self, ctx):
        self.visit(ctx.expresion(0))
        self.visit(ctx.expresion(1))
        return "bool"

    def visitEjecutarPrint(self, ctx):
        self.visit(ctx.expresion())
        return None

    def visitInstruccionReturn(self, ctx):
        return self.visit(ctx.returnStmt().expresion())