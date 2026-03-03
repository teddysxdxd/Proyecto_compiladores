grammar Calculadora;

// Reglas del Parser
archivo : instruccion+ EOF ;
instruccion : expresion NEWLINE ;

expresion : '(' expresion ')'                 # Parentesis
          | NUMERO                            # Numero
          | expresion op=('*'|'/') expresion  # MultiplicacionDivisision
          | expresion op=('+'|'-') expresion   # SumaResta
          | expresion op=('=='|'!='|'<>'|'<'|'>'|'<='|'>=') expresion # Relacional
          | expresion op=('&&'|'||'|'!') expresion # operadores logicos xd
          ;

// Reglas del Lexer
NUMERO  : [0-9]+ ('.' [0-9]+)? ;
NEWLINE : '\r'? '\n' ;
WS      : [ \t]+ -> skip ;