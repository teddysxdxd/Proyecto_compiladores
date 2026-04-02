from CalculadoraVisitor import CalculadoraVisitor
from symbol_table import SymbolTable

class InterpreterVisitor(CalculadoraVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.funciones = {} # Diccionario para guardar el cuerpo de las funciones

    def visitArchivo(self, ctx):
        for inst in ctx.instruccion():
            self.visit(inst)
        return None

    # --- Declaración y Asignación ---
    def visitInstruccionDeclaracion(self, ctx):
        tipo = ctx.declaracion().TIPO().getText()
        nombre = ctx.declaracion().ID().getText()
        valor = self.visit(ctx.declaracion().expresion()) if ctx.declaracion().expresion() else None
        self.symbol_table.declare(nombre, tipo, valor)
        return valor

    def visitInstruccionAsignacion(self, ctx):
        nombre = ctx.asignacion().ID().getText()
        valor = self.visit(ctx.asignacion().expresion())
        self.symbol_table.assign(nombre, valor)
        return valor

    # --- Estructuras de Control ---
    def visitWhileStatement(self, ctx):
        while self.visit(ctx.expresion()):
            self.visit(ctx.block())
        return None

    def visitInstruccionIf(self, ctx):
        condicion = self.visit(ctx.ifStatement().expresion())
        if condicion:
            return self.visit(ctx.ifStatement().block(0))
        elif ctx.ifStatement().block(1):
            return self.visit(ctx.ifStatement().block(1))
        return None

    def visitBlock(self, ctx):
        self.symbol_table.push_scope() # Manejo de Scopes [cite: 42]
        for inst in ctx.instruccion():
            self.visit(inst)
        self.symbol_table.pop_scope() # Limpieza al salir [cite: 43]
        return None

    # --- Funciones (Recursividad) ---
    def visitInstruccionFuncion(self, ctx):
        nombre = ctx.funcionDecl().ID().getText()
        # Guardamos el contexto de la función para llamarla luego
        self.funciones[nombre] = ctx.funcionDecl()
        return None

    def visitLlamadaFuncion(self, ctx):
        nombre = ctx.ID().getText()
        func_ctx = self.funciones.get(nombre)
        
        # Evaluar argumentos
        args_valores = []
        if ctx.args():
            args_valores = [self.visit(arg) for arg in ctx.args().expresion()]
        
        # Crear nuevo ámbito para la ejecución de la función
        self.symbol_table.push_scope()
        
        # Mapear parámetros a los valores de los argumentos
        params_ctx = func_ctx.params()
        if params_ctx:
            for i in range(len(args_valores)):
                p_nombre = params_ctx.ID(i).getText()
                p_tipo = params_ctx.TIPO(i).getText()
                self.symbol_table.declare(p_nombre, p_tipo, args_valores[i])
        
        # Ejecutar el bloque y capturar el return (si existe)
        resultado = self.visit(func_ctx.block())
        
        self.symbol_table.pop_scope()
        return resultado

    def visitInstruccionReturn(self, ctx):
        return self.visit(ctx.returnStmt().expresion())

    # --- Impresión ---
    def visitPrintStmt(self, ctx):
        res = self.visit(ctx.expresion())
        if isinstance(res, bool):
            print("verdadero" if res else "falso")
        else:
            print(res)
        return None

    # --- Expresiones ---
    def visitVariable(self, ctx):
        var = self.symbol_table.lookup(ctx.ID().getText())
        return var['value'] if var else None

    def visitNumero(self, ctx):
        num = ctx.NUMERO().getText()
        return float(num) if "." in num else int(num)

    def visitRelacional(self, ctx):
        izq = self.visit(ctx.expresion(0))
        der = self.visit(ctx.expresion(1))
        op = ctx.op.text
        if op == '==': return izq == der
        if op == '>': return izq > der
        if op == '<=': return izq <= der
        # Agrega aquí los demás: !=, <, >= [cite: 19]
        return False

def visitSumaResta(self, ctx):
    izq = self.visit(ctx.expresion(0))
    der = self.visit(ctx.expresion(1))
    
    # Concatenación si alguno es string
    if isinstance(izq, str) or isinstance(der, str):
        if ctx.op.text == '+':
            # Convierte ambos a string y concatena
            return str(izq) + str(der)
        else:
            raise RuntimeError(f"No se puede restar con strings: {izq} - {der}")
    
    # Suma/resta numérica normal
    if ctx.op.text == '+':
        return izq + der
    else:
        return izq - der
