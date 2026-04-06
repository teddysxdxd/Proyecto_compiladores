# 🧮 Proyecto Compiladores — *Calculadora con ANTLR4*

> Intérprete de un lenguaje personalizado construido con **ANTLR4 + Python 3**.  
> Soporta expresiones aritméticas, lógicas, variables, condicionales y bloques de código.

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![ANTLR4](https://img.shields.io/badge/ANTLR-4-EC1D24?style=flat-square)](https://www.antlr.org/)
[![Branch](https://img.shields.io/badge/branch-desarrollo-brightgreen?style=flat-square)](https://github.com/teddysxdxd/Proyecto_compiladores/tree/desarrollo)
[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)

---

## 📋 Tabla de Contenidos

- [¿Qué es este proyecto?](#-qué-es-este-proyecto)
- [Características del lenguaje](#-características-del-lenguaje)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Requisitos previos](#-requisitos-previos)
- [Instalación y ejecución](#-instalación-y-ejecución)
- [Sintaxis del lenguaje](#-sintaxis-del-lenguaje)
- [Ejemplos de uso](#-ejemplos-de-uso)
- [Gramática (resumen)](#-gramática-resumen)
- [Colaboradores](#-colaboradores)

---

## 🔍 ¿Qué es este proyecto?

Este proyecto implementa un **intérprete** para un lenguaje de programación personalizado usando el generador de parsers **ANTLR4** con runtime de Python.  
El lenguaje soporta operaciones matemáticas, comparaciones, lógica booleana, variables, estructuras condicionales (`simon` / `sinel`) y bloques de código.

---

## ✨ Características del lenguaje

| Categoría | Operadores / Palabras clave |
|---|---|
| Aritméticos | `+` `-` `*` `/` |
| Relacionales | `==` `!=` `<>` `<` `>` `<=` `>=` |
| Lógicos | `&&` `\|\|` `!` |
| Asignación | `=` |
| Condicional | `simon ( condición ) { }` / `sinel { }` |
| I/O | `print( expresión )` |
| Delimitadores | `Program` … `End_Program` |
| Tipos | Números enteros y decimales, cadenas de texto `"..."` |

---

## 📁 Estructura del proyecto

```
Proyecto_compiladores/
│
├── .antlr/                 # Archivos temporales de ANTLR
├── venv/                   # Entorno virtual de Python
├── Calculadora.g4          # Gramática principal (Lexer + Parser)
├── compiler.py             # Script principal del compilador
├── interpreter_visitor.py  # Lógica del intérprete (Visitor)
├── semantic_visitor.py     # Verificación de reglas semánticas
├── symbol_table.py         # Gestión de tabla de símbolos
├── custom_errors.py        # Manejo de errores personalizados
├── pipeline.py             # Flujo de ejecución del proyecto
├── operaciones.txt         # Archivo de entrada con código fuente
├── arbol_ast.png           # Visualización del árbol generado
├── readme.md               # Documentación del proyecto
└── .gitignore              # Archivos excluidos de Git
└── .gitignore
```

> ⚙️ Al ejecutar `antlr4`, se generan automáticamente los siguientes archivos (no subir al repo):
> `CalculadoraLexer.py`, `CalculadoraParser.py`, `CalculadoraVisitor.py`, `CalculadoraListener.py`

---

## 🔧 Requisitos previos

Antes de correr el proyecto, asegúrate de tener instalado:

- **Python 3.8+** → [descargar](https://www.python.org/downloads/)
- **Java 11+** (necesario para ANTLR4) → [descargar](https://adoptium.net/)
- **ANTLR4 CLI** → [instrucciones de instalación](https://www.antlr.org/download.html)

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
# Crear entorno virtual
python3 -m venv venv

# Activar (Linux / macOS)
source venv/bin/activate

```

> 💡 Sabrás que está activo cuando el prompt muestre `(venv)` al inicio.

### Paso 3 — Instalar dependencias

```bash
pip install antlr4-python3-runtime
```

### Paso 4 — Generar el parser desde la gramática

```bash
antlr4 -Dlanguage=Python3 -visitor -no-listener Calculadora.g4
```

Esto genera los archivos `CalculadoraLexer.py`, `CalculadoraParser.py`, etc.

## Paso 5 - Instalar dependencias de graphviz

```bash
sudo apt install graphviz
```
Esto generará dos archivos los cuales tienen de nombre `arbol.dot` y `arbol_ast.png`

### Paso 6 — Correr el intérprete

```bash
python3 main.py
```

---

## 📝 Sintaxis del lenguaje

Todo programa debe comenzar con `Program` y terminar con `End_Program`.

### Estructura básica

```
Program
    # tu código aquí
End_Program
```

### Variables y expresiones

```
Program
    x = 10
    y = 3.5
    resultado = x + y * 2
    print(resultado)
End_Program
```

### Condicional — `simon` / `sinel`

> La palabra clave `simon` equivale a `if`, y `sinel` equivale a `else`.

```
Program
    x = 15
    simon (x > 10) {
        print("x es mayor que 10")
    } sinel {
        print("x es menor o igual a 10")
    }
End_Program
```

### Operadores lógicos

```
Program
    a = 1
    b = 0
    simon (a == 1 && b == 0) {
        print("condicion verdadera")
    }
End_Program
```

---

## 💡 Ejemplos de uso

<details>
<summary><strong>Ejemplo 1 — Operaciones aritméticas básicas</strong></summary>

```
Program
    print(5 + 3)
    print(10 / 2)
    print(7 * (2 + 1))
End_Program
```

**Salida esperada:**
```
8
5.0
21
```

</details>

<details>
<summary><strong>Ejemplo 2 — Variables y comparaciones</strong></summary>

```
Program
    edad = 20
    simon (edad >= 18) {
        print("Mayor de edad")
    } sinel {
        print("Menor de edad")
    }
End_Program
```

**Salida esperada:**
```
Mayor de edad
```

</details>

<details>
<summary><strong>Ejemplo 3 — Operadores lógicos y negación</strong></summary>

```
Program
    activo = 1
    simon (!activo == 1) {
        print("inactivo")
    } sinel {
        print("activo")
    }
End_Program
```

</details>

---

## 📐 Gramática (resumen)

El lenguaje es definido en `Calculadora.g4`. Su estructura principal:

```
archivo → INICIOPROGRAMA instrucciones* FINPROGRAMA
instruccion → expresión | asignación | print | if | bloque
ifStatement → simon ( expresión ) bloque ( sinel bloque )?
expresion → número | cadena | variable | operación aritmética | operación lógica
```

<details>
<summary><strong>Ver gramática completa</strong></summary>

```antlr
grammar Calculadora;

archivo : INICIOPROGRAMA (instruccion | NEWLINE)* FINPROGRAMA EOF ;

instruccion : expresion                                                          # InstruccionExpresion
            | ID ASSIGN expresion                                                # Asignacion
            | PRINTI PARENTESISI expresion PARENTESISD                          # printStmt
            | ifStatement                                                        # InstruccionIf
            | block                                                              # InstruccionBloque
            ;

block : BLOCKI (instruccion | NEWLINE)* BLOCKF ;

ifStatement : IFINICIO PARENTESISI expresion PARENTESISD block (ELSE block)? ;

expresion : PARENTESISI expresion PARENTESISD                                   # Parentesis
          | CORCHI expresion CORCHD                                              # Corchetes
          | NUMERO                                                               # Numero
          | STRING                                                               # Cadena
          | ID                                                                   # Variable
          | NOTLOGICO expresion                                                  # NotLogico
          | expresion op=(MULT|DIV) expresion                                   # MultiplicacionDivisision
          | expresion op=(SUM|REST) expresion                                   # SumaResta
          | expresion op=(IGUALA|DIFERENTEA|DIFERENTEA2|MENORQUE|
                          MAYORQUE|MENORIGUAL|MAYORIGUAL) expresion             # Relacional
          | expresion op=(AND|OR) expresion                                     # AndOrLogico
          ;

// Palabras clave
INICIOPROGRAMA : 'Program';
FINPROGRAMA    : 'End_Program';
PRINTI         : 'print';
IFINICIO       : 'simon';
ELSE           : 'sinel';

// Operadores
MULT : '*';  DIV : '/';  SUM : '+';  REST : '-';
IGUALA : '==';  DIFERENTEA : '!=';  DIFERENTEA2 : '<>';
MENORQUE : '<';  MAYORQUE : '>';  MENORIGUAL : '<=';  MAYORIGUAL : '>=';
AND : '&&';  OR : '||';  NOTLOGICO : '!';  ASSIGN : '=';

// Delimitadores
BLOCKI : '{';  BLOCKF : '}';
PARENTESISI : '(';  PARENTESISD : ')';
CORCHI : '[';  CORCHD : ']';

// Literales e identificadores
NUMERO  : [0-9]+ ('.' [0-9]+)? ;
STRING  : '"' .*? '"' ;
ID      : [a-zA-Z_][a-zA-Z0-9_]* ;
NEWLINE : '\r'? '\n' ;
WS      : [ \t]+ -> skip ;
```

</details>



