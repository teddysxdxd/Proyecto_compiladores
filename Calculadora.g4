grammar Calculadora;

// El archivo puede contener instrucciones o líneas vacías
archivo : (instruccion | NEWLINE)* EOF ;

instruccion : expresion                    # InstruccionExpresion
            | 'print' '(' expresion ')'    # printStmt
            | ifStatement                  # InstruccionIf
            | block                        # InstruccionBloque
            ;

// Un bloque es una lista de instrucciones entre llaves
block : '{' (instruccion | NEWLINE)* '}' ;

// Tu estructura condicional personalizada
ifStatement : 'simon' '(' expresion ')' block ('sinel' block)? ;

// Jerarquía de expresiones (de mayor a menor precedencia)
expresion : '(' expresion ')'                 # Parentesis
          | NUMERO                            # Numero
          | STRING                            # Cadena
          | '!' expresion                     # NotLogico
          | expresion op=('*'|'/') expresion  # MultiplicacionDivisision
          | expresion op=('+'|'-') expresion   # SumaResta
          | expresion op=('=='|'!='|'<>'|'<'|'>'|'<='|'>=') expresion # Relacional
          | expresion op=('&&'|'||') expresion # AndOrLogico
          ;

// Lexer Rules
NUMERO  : [0-9]+ ('.' [0-9]+)? ;
STRING  : '"' .*? '"' ;
NEWLINE : '\r'? '\n' ;
WS      : [ \t]+ -> skip ;