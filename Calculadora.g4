grammar Calculadora;

// Reglas del Parser
archivo : instruccion+ EOF ;
instruccion : expresion NEWLINE ;

expresion : expresion op=('*'|'/') expresion   # MultiplicacionDivisision
          | expresion op=('+'|'-') expresion   # SumaResta
          | NUMERO                             # Numero
          | '(' expresion ')'                  # Parentesis
          ;

// Reglas del Lexer
NUMERO  : [0-9]+ ('.' [0-9]+)? ;
NEWLINE : '\r'? '\n' ;
WS      : [ \t]+ -> skip ;