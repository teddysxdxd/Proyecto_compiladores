# symbol_table.py [cite: 64]
class SymbolTable:
    def __init__(self):
        # Una lista que actúa como pila de diccionarios (Tablas Hash) [cite: 41, 42]
        self.scopes = [{}] 

    def push_scope(self):
        # Al entrar a un bloque o función [cite: 42]
        self.scopes.append({})

    def pop_scope(self):
        # Al salir de un bloque [cite: 43]
        if len(self.scopes) > 1:
            self.scopes.pop()

    def declare(self, name, symbol_type, value=None):
        # Shadowing: Error si ya existe en el ámbito LOCAL actual [cite: 44, 50]
        if name in self.scopes[-1]:
            raise Exception(f"Error Semántico: Variable '{name}' ya declarada en este ámbito.")
        self.scopes[-1][name] = {'type': symbol_type, 'value': value}

    def assign(self, name, value):
        # Busca desde el scope más interno al más externo [cite: 41]
        for scope in reversed(self.scopes):
            if name in scope:
                scope[name]['value'] = value
                return
        raise Exception(f"Error Semántico: Variable '{name}' no declarada.")

    def lookup(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None