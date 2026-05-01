grammar Calculadora;

// El archivo ahora es un bloque Program/End_Program
archivo : importStatement* INICIOPROGRAMA instruccion* FINPROGRAMA EOF;

importStatement : IMPORT ID;

instruccion : declaracion           # InstruccionDeclaracion
            | asignacion            # EjecutarAsignacion
            | PRINTI PARENTESISI expresion PARENTESISD # EjecutarPrint
            | ifStatement           # InstruccionIf
            | whileStatement        # InstruccionWhile
            | forStatement          # InstruccionFor
            | returnStmt            # InstruccionReturn
            | funcionDecl           # InstruccionFuncion
            | expresion             # InstruccionExpresion
            | BREAK           # BreakStmt
            | CONTINUE        # ContinueStmt
            | block                 # InstruccionBloque
            ;

// Tipos explícitos y funciones
declaracion : TIPO ID (ASSIGN expresion)? ;
asignacion  : ID ASSIGN expresion ;
returnStmt  : RETURN (expresion)? ;

funcionDecl : TIPO ID PARENTESISI (params)? PARENTESISD block ;
params      : TIPO ID (',' TIPO ID)* ;

// Estructuras de control
whileStatement : WHILE PARENTESISI expresion PARENTESISD block ;
forStatement   : FOR PARENTESISI asignacion ';' expresion ';' asignacion PARENTESISD block ;
block          : BLOCKI instruccion* BLOCKF ;

ifStatement : IFINICIO PARENTESISI expresion PARENTESISD block (ELSE block)? ;

// Jerarquía de expresiones
expresion : PARENTESISI expresion PARENTESISD # Parentesis
          | CORCHI expresion CORCHD           # Corchetes
          | NUMERO                            # Numero
          | STRING                            # Cadena
          | BOOLEANO                          # Booleano
          | ID PARENTESISI (args)? PARENTESISD # LlamadaFuncion
          | ID PUNTO ID PARENTESISI (expresion (COMA expresion)*)? PARENTESISD # LlamadaModulo
          | ID                                # Variable
          | NOTLOGICO expresion               # NotLogico
          | expresion op=(MULT|DIV|MOD) expresion # MultiplicacionDivisisionMod
          | expresion op=(SUM|REST) expresion # SumaResta
          | expresion op=(IGUALA|DIFERENTEA|DIFERENTEA2|MENORQUE|MAYORQUE|MENORIGUAL|MAYORIGUAL) expresion # Relacional
          | expresion op=(AND|OR) expresion   # AndOrLogico
          ;

args : expresion (',' expresion)* ;

// Lexer Rules
IMPORT   : 'import';
TIPO    : 'int' | 'float' | 'string' | 'bool' | 'void' ;
INICIOPROGRAMA: 'Program';
FINPROGRAMA: 'End_Program';
PRINTI  : 'print';
BLOCKI  : '{';
BLOCKF  : '}';
IFINICIO: 'simon';
ELSE    : 'sinel';
WHILE   : 'while';
BREAK    : 'break';
CONTINUE : 'continue';
FOR     : 'for';
RETURN  : 'return';
PARENTESISI: '(';
PARENTESISD: ')';
CORCHI  : '[';
CORCHD  : ']';
BOOLEANO: 'true' | 'false';
NOTLOGICO : '!';
MULT    : '*';
MOD : '%';
DIV     : '/';
SUM     : '+';
REST    : '-';
IGUALA  : '==';
DIFERENTEA : '!=';
DIFERENTEA2 : '<>';
MENORQUE: '<';
MAYORQUE: '>';
MENORIGUAL: '<=';
MAYORIGUAL: '>=';
AND : '&&';
OR  : '||' ;
COMA : ',';
PUNTO: '.';

NUMERO  : '-'? [0-9]+ ('.' [0-9]+)? ;
STRING  : '"' .*? '"' ;
WS      : [ \t\r\n]+ -> skip ;
ID      : [a-zA-Z_][a-zA-Z0-9_]* ;
ASSIGN  : '=';