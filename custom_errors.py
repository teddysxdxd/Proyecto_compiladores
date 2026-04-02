from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener(ErrorListener):
    def __init__(self):
        super(MyErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Formato exigido: [Error Sintáctico] Línea X, Columna Y...
        error_msg = f"[Error Sintáctico] Línea {line}, Columna {column}: {msg}"
        self.errors.append(error_msg)
        print(error_msg)

class LexerErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_msg = f"[Error Léxico] Línea {line}, Columna {column}: Símbolo no reconocido."
        print(error_msg)
        # Detener el pipeline si hay error léxico
        raise Exception("Fallo en Fase Léxica")