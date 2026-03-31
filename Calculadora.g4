grammar Calculadora;

// El archivo puede contener instrucciones o líneas vacías
archivo : INICIOPROGRAMA instruccion* FINPROGRAMA EOF ;

instruccion : expresion                    # InstruccionExpresion
            | ID ASSIGN  expresion             # Asignacion
            | PRINTI PARENTESISI expresion    PARENTESISD   # printStmt
            | ifStatement                  # InstruccionIf
            | block                        # InstruccionBloque
            ;

// Un bloque es una lista de instrucciones entre llaves
block : BLOCKI instruccion* BLOCKF ;

// Tu estructura condicional personalizada
ifStatement : IFINICIO PARENTESISI expresion PARENTESISD block (ELSE block)? ;

// Jerarquía de expresiones (de mayor a menor precedencia)
expresion : PARENTESISI expresion PARENTESISD # Parentesis
          | CORCHI expresion CORCHD                 # Corchetes                
          | NUMERO                             # Numero
          | STRING                             # Cadena
          | ID                                 # Variable
          | NOTLOGICO expresion                     # NotLogico
          | expresion op=(MULT|DIV) expresion  # MultiplicacionDivisision
          | expresion op=(SUM|REST) expresion   # SumaResta
          | expresion op=(IGUALA|DIFERENTEA|DIFERENTEA2|MENORQUE|MAYORQUE|MENORIGUAL|MAYORIGUAL) expresion # Relacional
          | expresion op=(AND|OR) expresion # AndOrLogico
          ;

// Lexer Rules
INICIOPROGRAMA: 'Program';
FINPROGRAMA: 'End_Program';
PRINTI  : 'print';
BLOCKI  : '{';
BLOCKF  : '}';
IFINICIO: 'simon';
ELSE : 'sinel';
PARENTESISI :'(';
PARENTESISD : ')';
CORCHI : '[';
CORCHD : ']';
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

// Regla para omitir espacios, tabulaciones y saltos de línea
WS : [ \t\r\n]+ -> skip ;

// ID debe ir después de las palabras reservadas
ID : [a-zA-Z_][a-zA-Z0-9_]* ;
ASSIGN : '=';