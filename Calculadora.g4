grammar Calculadora;

// El archivo ahora es un bloque Program/End_Program
archivo : importStatement* INICIOPROGRAMA instruccion* FINPROGRAMA EOF;

importStatement : IMPORT ID;

instruccion : declaracion           # InstruccionDeclaracion
            | asignacion            # EjecutarAsignacion
            | PRINTI PARENTESISI expresion PARENTESISD # EjecutarPrint
            | switchStatement       # InstruccionSwitch
            | ifStatement           # InstruccionIf
            | whileStatement        # InstruccionWhile
            | forStatement          # InstruccionFor
            | returnStmt            # InstruccionReturn
            | funcionDecl           # InstruccionFuncion
            | structDecl            # InstruccionStruct
            | expresion             # InstruccionExpresion
            | BREAK           # BreakStmt
            | CONTINUE        # ContinueStmt
            | block                 # InstruccionBloque
            ;

// Tipos explícitos y funciones
declaracion : TIPO ID (ASSIGN expresion)?
            | TIPO CORCHI CORCHD ID ASSIGN CORCHI expresion (COMA expresion)* CORCHD
            | ID ID
            ;
asignacion  : lvalue ASSIGN expresion ;
returnStmt  : RETURN (expresion)? ;

funcionDecl : TIPO ID PARENTESISI (params)? PARENTESISD block ;
params      : TIPO ID (',' TIPO ID)* ;

// Structs
structDecl      : STRUCT ID BLOCKI structFieldDecl* BLOCKF ;
structFieldDecl : TIPO ID ;

// Estructuras de control
whileStatement : WHILE PARENTESISI expresion PARENTESISD block ;
forStatement   : FOR PARENTESISI asignacion ';' expresion ';' asignacion PARENTESISD block ;
block          : BLOCKI instruccion* BLOCKF ;

ifStatement : IFINICIO PARENTESISI expresion PARENTESISD block (ELSE block)? ;
switchStatement : SWITCH PARENTESISI expresion PARENTESISD BLOCKI caseClause+ defaultClause? BLOCKF ;
caseClause      : CASE expresion COLON instruccion* ;
defaultClause   : DEFAULT COLON instruccion* ;

lvalue : ID ((PUNTO ID) | (CORCHI expresion CORCHD))* ;

// Jerarquía de expresiones
expresion : PARENTESISI TIPO PARENTESISD expresion # CastExplicito
          | PARENTESISI expresion PARENTESISD # Parentesis
          | CORCHI expresion CORCHD           # Corchetes
          | NUMERO                            # Numero
          | STRING                            # Cadena
          | BOOLEANO                          # Booleano
          | ID PARENTESISI (args)? PARENTESISD # LlamadaFuncion
          | ID PUNTO ID PARENTESISI (expresion (COMA expresion)*)? PARENTESISD # LlamadaModulo
          | lvalue                            # Variable
          | NOTLOGICO expresion               # NotLogico
          | expresion op=(MULT|DIV|MOD) expresion # MultiplicacionDivisisionMod
          | expresion op=(SUM|REST) expresion # SumaResta
          | expresion op=(IGUALA|DIFERENTEA|DIFERENTEA2|MENORQUE|MAYORQUE|MENORIGUAL|MAYORIGUAL) expresion # Relacional
          | expresion op=(AND|OR) expresion   # AndOrLogico
          | expresion QUESTION expresion COLON expresion # Ternario
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
SWITCH  : 'switch';
CASE    : 'case';
DEFAULT : 'default';
STRUCT  : 'struct';
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
COLON: ':';
QUESTION: '?';

NUMERO  : '-'? [0-9]+ ('.' [0-9]+)? ;
STRING  : '"' .*? '"' ;
WS      : [ \t\r\n]+ -> skip ;
ID      : [a-zA-Z_][a-zA-Z0-9_]* ;
ASSIGN  : '=';
