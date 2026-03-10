grammar Calculadora;

// El archivo puede contener instrucciones o líneas vacías
archivo : (instruccion | NEWLINE)* EOF ;

instruccion : expresion                    # InstruccionExpresion
            | ID '=' expresion             # Asignacion
            | PRINTI PARENTESISI expresion    PARENTESISD   # printStmt
            | ifStatement                  # InstruccionIf
            | block                        # InstruccionBloque
            ;

// Un bloque es una lista de instrucciones entre llaves
block : BLOCKI (instruccion | NEWLINE)* BLOCKF ;

// Tu estructura condicional personalizada
ifStatement : IFINICIO PARENTESISI expresion PARENTESISD block (ELSE block)? ;

// Jerarquía de expresiones (de mayor a menor precedencia)
expresion : PARENTESISI expresion PARENTESISD
          | '[' expresion ']'                 # Corchetes                 # Parentesis
          | NUMERO                            # Numero
          | STRING                            # Cadena
          | ID                                # Variable
          | NOTLOGICO expresion                     # NotLogico
          | expresion op=(MULT|DIV) expresion  # MultiplicacionDivisision
          | expresion op=(SUM|REST) expresion   # SumaResta
          | expresion op=(IGUALA|DIFERENTEA|DIFERENTEA2|MENORQUE|MAYORQUE|MENORIGUAL|MAYORIGUAL) expresion # Relacional
          | expresion op=(AND|OR) expresion # AndOrLogico
          ;

// Lexer Rules
PRINTI  : 'print';
BLOCKI  : '{';
BLOCKF  : '}';
IFINICIO: 'simon';
ELSE : 'sinel';
PARENTESISI :'(';
PARENTESISD : ')';
NOTLOGICO : '!';
MULT    : '*';
DIV     : '/';
SUM     : '+';
REST    : '-';
IGUALA  : '==';
DIFERENTEA : '!=';
DIFERENTEA2 : '<>';
MENORQUE: '<';
MAYORQUE: '>';
MENORIGUAL: '<=';
MAYORIGUAL:'>=';
AND : '&&';
OR  : '||' ;
NUMERO  : [0-9]+ ('.' [0-9]+)? ;
STRING  : '"' .*? '"' ;
NEWLINE : '\r'? '\n' ;
WS      : [ \t]+ -> skip ;
ID : [a-zA-Z_][a-zA-Z0-9_]* ;