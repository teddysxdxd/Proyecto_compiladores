# 🧮 Proyecto Compiladores — *Lenguaje Personalizado con ANTLR4*

> Intérprete / compilador híbrido de un lenguaje personalizado construido con **ANTLR4 + Python 3**.
> Soporta expresiones aritméticas, lógicas, variables tipadas, condicionales, ciclos, funciones, imports y bloques de código.

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square\&logo=python\&logoColor=white)](https://www.python.org/)
[![ANTLR4](https://img.shields.io/badge/ANTLR-4-EC1D24?style=flat-square)](https://www.antlr.org/)
[![Branch](https://img.shields.io/badge/branch-desarrollo-brightgreen?style=flat-square)](https://github.com/teddysxdxd/Proyecto_compiladores/tree/desarrollo)
[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)

---

## 📋 Tabla de Contenidos

<<<<<<< Updated upstream
- [¿Qué es este proyecto?](#-qué-es-este-proyecto)
- [Novedades del Proyecto 2](#-novedades-del-proyecto-2)
- [Características del lenguaje](#-características-del-lenguaje)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Requisitos previos](#-requisitos-previos)
- [Instalación y ejecución](#-instalación-y-ejecución)
- [Sintaxis del lenguaje](#-sintaxis-del-lenguaje)
- [Ejemplos de uso](#-ejemplos-de-uso)
- [Gramática (resumen)](#-gramática-resumen)
=======
* [¿Qué es este proyecto?](#-qué-es-este-proyecto)
* [Características del lenguaje](#-características-del-lenguaje)
* [Estructura del proyecto](#-estructura-del-proyecto)
* [Requisitos previos](#-requisitos-previos)
* [Instalación y ejecución](#-instalación-y-ejecución)
* [Sintaxis del lenguaje](#-sintaxis-del-lenguaje)
* [Ejemplos de uso](#-ejemplos-de-uso)
* [Gramática (resumen)](#-gramática-resumen)
* [Colaboradores](#-colaboradores)
>>>>>>> Stashed changes

---

## 🔍 ¿Qué es este proyecto?

Este proyecto implementa un **intérprete / compilador híbrido** para un lenguaje de programación personalizado usando el generador de parsers **ANTLR4** con runtime de Python.
El lenguaje soporta operaciones matemáticas, comparaciones, lógica booleana, variables tipadas, estructuras condicionales (`simon` / `sinel`), ciclos, funciones, imports y bloques de código.

---

## 🚀 Novedades del Proyecto 2

El proyecto evolucionó a un modelo más cercano a un compilador formal:

### 🔄 Pipeline de Ejecución
Se implementó un flujo obligatorio de validación:

```
Léxico → Sintáctico → Semántico → Intérprete
```

Esto garantiza que el código sea válido antes de ejecutarse.

### 🧠 Análisis Semántico
- Validación de tipos
- Verificación de variables declaradas
- Validación de funciones (parámetros y retorno)

### 🗂️ Manejo de Scopes (Ámbitos)
- Implementado con **pila de tablas hash (dicts en Python)**
- Soporta:
  - Scope global
  - Scopes locales (funciones y bloques)
- Acceso eficiente en tiempo **O(1)**

### 🔁 Funciones
- Declaración con parámetros tipados
- Retorno obligatorio
- Soporte para **recursividad**

### ❌ Manejo de Errores
- Errores léxicos, sintácticos y semánticos
- Reporte detallado con línea y columna
- Implementado en `custom_errors.py`

---

## ✨ Características del lenguaje

<<<<<<< Updated upstream
| Categoría | Operadores / Palabras clave |
|---|---|
| Aritméticos | `+` `-` `*` `/` |
| Relacionales | `==` `!=` `<>` `<` `>` `<=` `>=` |
| Lógicos | `&&` `\|\|` `!` |
| Asignación | `=` |
| Condicional | `simon ( condición ) { }` / `sinel { }` |
| I/O | `print( expresión )` |
| Delimitadores | `Program` … `End_Program` |
| Tipos | `int`, `float`, `string`, `bool` |
| Funciones | Declaración, parámetros y retorno |
=======
| Categoría        | Operadores / Palabras clave             |
| ---------------- | --------------------------------------- |
| Tipos            | `int` `float` `string` `bool` `void`    |
| Aritméticos      | `+` `-` `*` `/` `%`                     |
| Relacionales     | `==` `!=` `<>` `<` `>` `<=` `>=`        |
| Lógicos          | `&&` `\|\|` `!`                         |
| Asignación       | `=`                                     |
| Condicional      | `simon ( condición ) { }` / `sinel { }` |
| Ciclos           | `while (...) { }` / `for (...) { }`     |
| Funciones        | declaración, parámetros y `return`      |
| Control de flujo | `break` / `continue`                    |
| Imports          | `import modulo`                         |
| I/O              | `print( expresión )`                    |
| Delimitadores    | `Program` … `End_Program`               |
>>>>>>> Stashed changes

---

## 📁 Estructura del proyecto

```text
Proyecto_compiladores/
│
├── .antlr/                 # Archivos temporales de ANTLR
├── src/                    # Casos de prueba y programas fuente del lenguaje
│   ├── modulo.txt
│   ├── while.txt
│   ├── operaciones.txt
│   └── ...
├── venv/                   # Entorno virtual de Python
├── Calculadora.g4          # Gramática principal (Lexer + Parser)
├── compiler.py             # Script principal del compilador
├── interpreter_visitor.py  # Lógica del intérprete (Visitor)
├── semantic_visitor.py     # Verificación de reglas semánticas
├── symbol_table.py         # Gestión de tabla de símbolos (scopes)
├── custom_errors.py        # Manejo de errores personalizados
├── pipeline.py             # Flujo de ejecución del proyecto
├── arbol_ast.png           # Visualización del árbol generado
<<<<<<< Updated upstream
├── readme.md               # Documentación del proyecto
└── .gitignore
├── ir_generator.py			# traduce el modulo LLVM IR 
├── ui_compiler.py		    #  interfaz de compilación grafica
├── tac_generator.py      # Recorre el AST generado y emite codigo en tres direcciones
├── readme.md              # Documentación del proyecto
└── .gitignore                 # Archivos excluidos de Git

=======
├── ir_generator.py         # Traduce el módulo a LLVM IR
├── ui_compiler.py          # Interfaz gráfica de compilación
├── tac_generator.py        # Recorre el AST generado y emite código en tres direcciones
├── readme.md               # Documentación del proyecto
└── .gitignore              # Archivos excluidos de Git
>>>>>>> Stashed changes
```

> ⚙️ Al ejecutar `antlr4`, se generan automáticamente los siguientes archivos (no subir al repo):
> `CalculadoraLexer.py`, `CalculadoraParser.py`, `CalculadoraVisitor.py`, `CalculadoraListener.py`, `operaciones.ll`, `operaciones.tac`

---

## 🔧 Requisitos previos

Antes de correr el proyecto, asegúrate de tener instalado:

* **Python 3.8+** → [descargar](https://www.python.org/downloads/)
* **Java 11+** (necesario para ANTLR4) → [descargar](https://adoptium.net/)
* **ANTLR4 CLI** → [instrucciones de instalación](https://www.antlr.org/download.html)

Para verificar que tienes todo:

```bash
python3 --version   # Python 3.8+
java --version      # Java 11+
antlr4              # Debe mostrar la versión de ANTLR
```

---

## 🚀 Instalación y ejecución

### Paso 1 — Clonar el repositorio

```bash
git clone https://github.com/teddysxdxd/Proyecto_compiladores.git
cd Proyecto_compiladores
git checkout desarrollo
```

### Paso 2 — Crear y activar el entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### Paso 3 — Instalar dependencias

```bash
pip install antlr4-python3-runtime
pip install llvmlite
pip install textual
pip install rich
```

### Paso 4 — Generar el parser desde la gramática

```bash
antlr4 -Dlanguage=Python3 -visitor -no-listener Calculadora.g4
```

<<<<<<< Updated upstream
### Paso 5 — Instalar Graphviz
=======
Esto genera los archivos `CalculadoraLexer.py`, `CalculadoraParser.py`, etc.

## Paso 5 - Instalar dependencias de Graphviz
>>>>>>> Stashed changes

```bash
sudo apt install graphviz
```

<<<<<<< Updated upstream
### Paso 6 — Ejecutar el proyecto (pipeline recomendado)
## Paso 6 - Instalacion de Tkinter, llvmlite, textual & rich
=======
Esto generará dos archivos llamados `arbol.dot` y `arbol_ast.png`.

## Paso 6 - Instalación de Tkinter
>>>>>>> Stashed changes

```bash
sudo apt install python3-tk
```

### Paso 7 — Correr el intérprete

```bash
python3 pipeline.py
```

### Paso 8 — Vista de interfaz

```bash
1. Abrir interfaz gráfica
2. Seleccionar archivo fuente (.txt)
3. Presionar "Compilar"
4. Ejecutar pipeline de compilación
5. Mostrar resultados / errores
6. Cerrar aplicación

python3 ui_compiler.py

ui_compiler.py
└── Interfaz gráfica del compilador para carga de archivos,
    ejecución del pipeline y visualización de resultados
```

---

## 📝 Sintaxis del lenguaje

Todo programa debe comenzar con `Program` y terminar con `End_Program`.

### Estructura básica

```txt
Program
    # tu código aquí
End_Program
```

### Variables y expresiones

```txt
Program
    int x = 10
    float y = 3.5
<<<<<<< Updated upstream
    resultado = x + y * 2
=======
    float resultado = x + y * 2
>>>>>>> Stashed changes
    print(resultado)
End_Program
```

### Condicional — `simon` / `sinel`

<<<<<<< Updated upstream
```
=======
> La palabra clave `simon` equivale a `if`, y `sinel` equivale a `else`.

```txt
>>>>>>> Stashed changes
Program
    int x = 15
    simon (x > 10) {
        print("x es mayor que 10")
    } sinel {
        print("x es menor o igual a 10")
    }
End_Program
```

### Funciones y recursividad

```txt
Program
<<<<<<< Updated upstream
    int factorial(int n) {
        simon (n <= 1) {
            return 1
        } sinel {
            return n * factorial(n - 1)
        }
=======
    bool activo = true
    simon (activo && true) {
        print("condicion verdadera")
>>>>>>> Stashed changes
    }

    int res = factorial(5)
    print("Factorial: " + res)
End_Program
```

### Ciclo while

```txt
Program
    int i = 0

    while (i < 5) {
        print(i)
        i = i + 1
    }
End_Program
```

### Ciclo for

```txt
Program
    int i = 0

    for(i = 0; i < 10; i = i + 1) {
        print(i)
    }
End_Program
```

### Declaración de funciones

```txt
Program

int suma(int a, int b){
    return a + b
}

print(suma(4,6))

End_Program
```

### Imports

```txt
import math

Program
    print(math.sqrt(25))
End_Program
```

### Break / Continue

```txt
Program
    while (true) {
        break
    }
End_Program
```

### Sección Tipos

| Tipo   | Descripción | Ejemplo                    |
| ------ | ----------- | -------------------------- |
| int    | entero      | `int edad = 20`            |
| float  | decimal     | `float pi = 3.14`          |
| string | texto       | `string nombre = "Nombre"` |
| bool   | booleano    | `bool activo = true`       |

## 💡 Ejemplos de uso

<details>
<summary><strong>Ejemplo 1 — Operaciones aritméticas básicas</strong></summary>

```txt
Program
    print(5 + 3)
    print(10 / 2)
    print(7 * (2 + 1))
End_Program
```

<<<<<<< Updated upstream
=======
**Salida esperada:**

```txt
8
5.0
21
```

>>>>>>> Stashed changes
</details>

<details>
<summary><strong>Ejemplo 2 — Variables y comparaciones</strong></summary>

```txt
Program
    int edad = 20
    simon (edad >= 18) {
        print("Mayor de edad")
    } sinel {
        print("Menor de edad")
    }
End_Program
```

<<<<<<< Updated upstream
=======
**Salida esperada:**

```txt
Mayor de edad
```

</details>

<details>
<summary><strong>Ejemplo 3 — Operadores lógicos y negación</strong></summary>

```txt
Program
    bool activo = false
    simon (!activo) {
        print("inactivo")
    } sinel {
        print("activo")
    }
End_Program
```

>>>>>>> Stashed changes
</details>

---

> 📂 El directorio `src/` contiene todos los **casos de prueba** del compilador,
> incluyendo programas válidos, pruebas de operadores, estructuras condicionales,
> validaciones semánticas y escenarios de error utilizados para verificar
> el correcto funcionamiento del lenguaje.

```text
├── src/                    # Casos de prueba y programas fuente del lenguaje
│   ├── modulo.txt
│   ├── while.txt
│   ├── operaciones.txt
│   └── ...
```

## 📐 Gramática (resumen)

El lenguaje es definido en `Calculadora.g4`. Su estructura principal:

<<<<<<< Updated upstream
```
archivo → INICIOPROGRAMA instrucciones* FINPROGRAMA
instruccion → expresión | asignación | print | if | bloque | función
=======
```txt
archivo → importStatement* INICIOPROGRAMA instruccion* FINPROGRAMA
instruccion → declaracion | asignacion | print | if | while | for | return | funcion | break | continue | bloque | expresion
>>>>>>> Stashed changes
ifStatement → simon ( expresión ) bloque ( sinel bloque )?
whileStatement → while ( expresión ) bloque
forStatement → for ( asignacion ; expresión ; asignacion ) bloque
expresion → número | cadena | booleano | variable | llamadaFuncion | llamadaModulo | operación aritmética | operación lógica
```

<details>
<summary><strong>Ver gramática completa</strong></summary>

```antlr
```antlr
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
```

<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
</details>
