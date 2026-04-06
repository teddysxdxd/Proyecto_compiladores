# 🧮 Proyecto Compiladores — *Calculadora Avanzada con ANTLR4*

> Intérprete y Analizador Semántico robusto construido con **ANTLR4 + Python 3**.  
> Evolución de una calculadora básica hacia un **lenguaje formal con tipado, funciones, scopes y validación completa**.

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![ANTLR4](https://img.shields.io/badge/ANTLR-4-EC1D24?style=flat-square)](https://www.antlr.org/)
[![Branch](https://img.shields.io/badge/branch-desarrollo-brightgreen?style=flat-square)](https://github.com/teddysxdxd/Proyecto_compiladores/tree/desarrollo)
[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)

---

## 📋 Tabla de Contenidos

- [¿Qué es este proyecto?](#-qué-es-este-proyecto)
- [Novedades del Proyecto 2](#-novedades-del-proyecto-2)
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

Este proyecto implementa un **intérprete para un lenguaje de programación personalizado** usando **ANTLR4** con runtime en Python.

Inicialmente era una calculadora básica, pero ahora evolucionó a un sistema más completo que incluye:

- Validación semántica
- Tipado estricto
- Funciones con recursividad
- Manejo de ámbitos (scopes)
- Pipeline formal de compilación

---

## 🚀 Novedades del Proyecto 2

El sistema ahora sigue un flujo formal tipo compilador:

### 🔄 Pipeline de Ejecución
Flujo obligatorio:
```
Análisis Léxico → Análisis Sintáctico → Análisis Semántico → Ejecución
```

### 🧠 Análisis Semántico
- Validación de tipos
- Verificación de variables declaradas
- Validación de funciones (firma, parámetros, retorno)

### 🗂️ Tabla de Símbolos (Scopes)
- Implementada como **pila de tablas hash (dicts en Python)**
- Manejo de:
  - Ámbito global
  - Ámbitos locales (funciones, bloques)
- Acceso eficiente: **O(1)**

### 🔁 Funciones
- Parámetros tipados
- Retorno obligatorio
- Soporte para **recursividad**

### ❌ Manejo de Errores
- Errores léxicos, sintácticos y semánticos
- Reporte con:
  - Línea
  - Columna
- Implementado en `custom_errors.py`

---

## ✨ Características del Lenguaje

| Categoría | Operadores / Palabras clave |
|---|---|
| **Tipos de Datos** | `int`, `float`, `string`, `bool` |
| **Aritméticos** | `+` `-` `*` `/` |
| **Relacionales** | `==` `!=` `<>` `<` `>` `<=` `>=` |
| **Lógicos** | `&&` `||` `!` |
| **Asignación** | `=` |
| **Condicional** | `simon ( condición ) { }` / `sinel { }` |
| **Ciclos** | `while (...) {}` / `for (...) {}` |
| **Funciones** | Declaración y llamadas con parámetros |
| **I/O** | `print( expresión )` |
| **Delimitadores** | `Program` … `End_Program` |

---

## 📁 Estructura del Proyecto

```
Proyecto_compiladores/
│
├── .antlr/                 # Archivos generados por ANTLR
├── venv/                   # Entorno virtual
├── Calculadora.g4          # Gramática (Lexer + Parser + Labels)
├── pipeline.py             # Orquestador del flujo (pipeline)
├── interpreter_visitor.py  # Motor de ejecución
├── semantic_visitor.py     # Validación semántica
├── symbol_table.py         # Manejo de scopes
├── custom_errors.py        # Manejo de errores
├── operaciones.txt         # Código fuente de entrada
├── arbol_ast.png           # Árbol AST generado
├── readme.md               # Documentación
└── .gitignore
```

> ⚙️ Archivos generados automáticamente por ANTLR (no subir):
> `CalculadoraLexer.py`, `CalculadoraParser.py`, etc.

---

## 🔧 Requisitos previos

- Python 3.8+
- Java 11+
- ANTLR4 CLI
- Graphviz

Verificación:

```bash
python3 --version
java --version
antlr4
```

---

## 🚀 Instalación y ejecución

### 1. Clonar repositorio

```bash
git clone https://github.com/teddysxdxd/Proyecto_compiladores.git
cd Proyecto_compiladores
git checkout desarrollo
```

### 2. Crear entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install antlr4-python3-runtime
```

### 4. Generar parser

```bash
antlr4 -Dlanguage=Python3 -visitor -no-listener Calculadora.g4
```

### 5. Instalar Graphviz

```bash
sudo apt install graphviz
```

### 6. Ejecutar pipeline

```bash
python3 pipeline.py
```

---

## 📝 Sintaxis del lenguaje

### Estructura básica

```
Program
    # código
End_Program
```

---

## 💡 Ejemplos de uso

### 🔁 Recursividad (Factorial)

```
Program
    int x = 5

    int factorial(int n) {
        simon (n <= 1) {
            return 1
        } sinel {
            return n * factorial(n - 1)
        }
    }

    int res = factorial(x)
    print("El factorial es: " + res)
End_Program
```

---

### ➗ Operaciones básicas

```
Program
    print(5 + 3)
    print(10 / 2)
    print(7 * (2 + 1))
End_Program
```

---

### 🔀 Condicionales

```
Program
    int x = 15
    simon (x > 10) {
        print("Mayor")
    } sinel {
        print("Menor")
    }
End_Program
```

---

## 📐 Gramática (resumen)

```
instruccion : expresion
            | declaracion
            | asignacion
            | funcionDecl
            | returnStmt
            | printStmt
            | ifStatement
            | whileStatement
            | forStatement
            ;
```

---
