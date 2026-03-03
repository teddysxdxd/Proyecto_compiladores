grammar Calculadora;

archivo : instruccion+ EOF ;
instruccion : expresion NEWLINE ;

expresion : '(' expresion ')'                 # Parentesis
          | NUMERO                            # Numero
          | '!' expresion                     # NotLogico
          | expresion op=('*'|'/') expresion  # MultiplicacionDivisision
          | expresion op=('+'|'-') expresion   # SumaResta
          | expresion op=('=='|'!='|'<>'|'<'|'>'|'<='|'>=') expresion # Relacional
          | expresion op=('&&'|'||') expresion # AndOrLogico
          ;

NUMERO  : [0-9]+ ('.' [0-9]+)? ;
NEWLINE : '\r'? '\n' ;
WS      : [ \t]+ -> skip ;