from CalculadoraVisitor import CalculadoraVisitor
from symbol_table import SymbolTable

class InterpreterVisitor(CalculadoraVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.funciones = {} 

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
        # IMPORTANTE: assign debe actualizar el valor en la Tabla Hash
        self.symbol_table.assign(nombre, valor)
        return valor

    # --- Estructuras de Control ---
    def visitWhileStatement(self, ctx):
        # El while debe re-evaluar la condición en cada vuelta
        while self.visit(ctx.expresion()):
            # IMPORTANTE: No usamos visitBlock aquí para que el ciclo 
            # trabaje sobre el mismo scope y pueda modificar las variables.
            for inst in ctx.block().instruccion():
                res = self.visit(inst)
                if res is not None: return res # Por si hay un return dentro
        return None

    def visitInstruccionIf(self, ctx):
        condicion = self.visit(ctx.ifStatement().expresion())
        if condicion:
            return self.visit(ctx.ifStatement().block(0))
        elif ctx.ifStatement().block(1):
            return self.visit(ctx.ifStatement().block(1))
        return None

    def visitBlock(self, ctx):
        self.symbol_table.push_scope() 
        for inst in ctx.instruccion():
            res = self.visit(inst)
            if res is not None: # Si hay un return, lo propagamos
                self.symbol_table.pop_scope()
                return res
        self.symbol_table.pop_scope() 
        return None

    # --- Funciones ---
    def visitInstruccionFuncion(self, ctx):
        nombre = ctx.funcionDecl().ID().getText()
        self.funciones[nombre] = ctx.funcionDecl()
        return None

    def visitLlamadaFuncion(self, ctx):
        nombre = ctx.ID().getText()
        func_ctx = self.funciones.get(nombre)
        if not func_ctx: return None
        
        args_valores = [self.visit(arg) for arg in ctx.args().expresion()] if ctx.args() else []
        self.symbol_table.push_scope()
        
        params_ctx = func_ctx.params()
        if params_ctx:
            for i in range(len(args_valores)):
                self.symbol_table.declare(params_ctx.ID(i).getText(), params_ctx.TIPO(i).getText(), args_valores[i])
        
        resultado = self.visit(func_ctx.block())
        self.symbol_table.pop_scope()
        return resultado

    def visitInstruccionReturn(self, ctx):
        return self.visit(ctx.returnStmt().expresion()) if ctx.returnStmt().expresion() else None

    # --- Impresión ---
    def visitPrintStmt(self, ctx):
        res = self.visit(ctx.expresion())
        if isinstance(res, bool):
            print("verdadero" if res else "falso")
        elif isinstance(res, str):
            print(res.strip('"')) # Limpiamos las comillas al imprimir
        else:
            print(res)
        return None

    # --- Expresiones ---
    def visitVariable(self, ctx):
        var = self.symbol_table.lookup(ctx.ID().getText())
        return var['value'] if var else 0

    def visitNumero(self, ctx):
        num = ctx.NUMERO().getText()
        return float(num) if "." in num else int(num)

    def visitCadena(self, ctx):
        return ctx.STRING().getText()

    def visitRelacional(self, ctx):
        izq = self.visit(ctx.expresion(0))
        der = self.visit(ctx.expresion(1))
        op = ctx.op.text
        if op == '==': return izq == der
        if op == '>': return izq > der
        if op == '<': return izq < der
        if op == '>=': return izq >= der
        if op == '<=': return izq <= der
        if op == '!=' or op == '<>': return izq != der
        return False

    def visitSumaResta(self, ctx):
        izq = self.visit(ctx.expresion(0))
        der = self.visit(ctx.expresion(1))
        
        if isinstance(izq, str) or isinstance(der, str):
            if ctx.op.text == '+':
                # Limpiamos comillas antes de concatenar para que se vea bien
                return str(izq).strip('"') + str(der).strip('"')
            else:
                raise RuntimeError(f"Error: Operación '{ctx.op.text}' no válida con strings")
        
        return (izq + der) if ctx.op.text == '+' else (izq - der)