[//]: # (Miércoles 2 de abril)

# Clase 1: Conceptos del pensamiento lógico y la programación de flujos

## Sección 1
* Bienvenido al curso
* Acerca del curso
* Plan de Estudios
* evaluación

## Sección 2
* ¿Qué es la programación?
* ¿Por qué aprender a programar?
* Programar en la era de la IA
  - MCP: Model Control Protocol
  - Asistente de programación
  - Agentes autónomos para programar
* Pensamiento lógico
  - Problema - idea - solución
* Programación como un herramienta creativa (Un problema múltiples soluciones)
* Diagrama de flujo y Pseudocódigo
* Diferencia entre un programa y un modelo de ml

### Ejercicios: 
* Diseño de diagrama de flujos para resolver 3 problemas


# Clase 2: intro a la programación en python

## Sección 1 - Introducción a la programación

* ¿Cómo funciona un programa de computadora?
* Lenguajes naturales y lenguajes de programación
* Lenguaje máquina vs. lenguaje de alto nivel
* Compilación vs. interpretación
* ¿Qué hace el intérprete?
* Compilación vs. Interpretación – Ventajas y Desventajas

## Sección 2 – Introducción a Python
* Python - un lenguaje de programación
* ¿Qué hace que Python sea tan especial?
* ¿Rivales de Python?
* ¿Dónde podemos ver a Python en acción?
* ¿Por qué no Python?
* Existe más de un Python
*  
* Reglas para escribir código python (sintaxis)

## Sección 3 - Descarga e instalación de Python
* Conda para la gestión de python 
* Versiones de python y la importancia de la que usaremos
* Python interactivo desde la terminal 
* Tu primer script/programa
* IDEs: como usarlos y las ventajas y desventajas de VSCode vs Colab
  - terminal
  - VSCode
  - jupyter notebook (Colab, KAggle, DeepNote, MyBinder)

* Cómo estropear y arreglar tu código

### Ejercicios: 
* interactuar con la terminal usando print

[//]: # (Sábado 5 de abril)

# Clase 3: Tipos de Datos, variables y Operaciones Básicas

## Sección 1: Tipos de datos elementales de Python
* Enteros
* Flotantes
* Cadenas
* Valores Booleanos
* función type()

## Sección 3 – Variables
* ¿Qué es una variable? 
* ¿Cómo crear una variable?
* ¿Qué nombres usar?
* ¿Qué nombres no usar?
* Cómo asignar un nuevo valor a una variable ya existente
* python es no tipeado
* como castear una variable a otro tipo de dato

## Sección 2 – Operadores - herramientas de manipulación de datos
* Operadores Básicos 
  * +,-,/,\*,//,%, **
* Otros operadores
  * round(), abs()
* Extensión para string y otros tipos de datos
  * +
* Orden de las operaciones
* Operadores Abreviados
  * +=, -=, *=, /=
* Convertir tipo de variable
  * str(), int(), float()

## Personalizar strings
* ¿Cómo juntar 2 strings?
* ¿Cómo crea un string con otro tipo de datos?
* ¿Cómo generar string dinámicos?
* ¿Cómo crear un bloque de texto?
* Caracteres especiales \n \t \”
* Doble comilla o comilla simple?

## Sección 5 – Comentarios
* 2.5.1 Comentarios – ¿por qué, cuándo, y dónde?
* 2.5.2 Marcar fragmentos de código

## Sección 6 – Entrada y salida de texto
* La función print()
* La función input()

### Buenas prácticas 


# Clase 4: Estructuras de Control - Condicionales

## Sección 1 – Introducción a las Condiciones
* ¿Qué es una estructura de control?
* ¿Por qué son necesarias las condiciones en programación?

## Sección 2 – La estructura if-elif-else
* Sintaxis y funcionamiento
* Uso de operadores de comparación (==, !=, <, >, <=, >=)
* Uso de operadores lógicos (and, or, not)
* Anidamiento de condicionales

## Sección 3 – Expresiones Condicionales y Evaluación Cortocircuitada
* Expresiones condicionales en una línea
* Evaluación perezosa

### Ejercicios:
* Crear un programa que determine si un número es positivo, negativo o cero
* Validar si un usuario puede acceder a una plataforma según su edad
* Escribir una calculadora de descuentos basada en la cantidad de productos comprados


# Clase 5: Estructuras de Control - Bucles

## Sección 1 – Introducción a los Bucles
* ¿Qué es un bucle y por qué es importante?

## Sección 2 – El bucle while
* Sintaxis y funcionamiento
* Ejemplo con contadores y acumuladores
* Evitando bucles infinitos

## Sección 3 – El bucle for
* Sintaxis y funcionamiento
* Iteración sobre listas, cadenas y rangos (range())
* Usando enumerate() y zip()

## Sección 4 – Controlando el Flujo del Bucle
* break y continue
* else en bucles

### Ejercicios:
* Imprimir los números del 1 al 10 usando for y while
* Sumar los primeros 100 números naturales
* Crear un programa que pida al usuario adivinar un número secreto usando un bucle



[//]: # (Lunes 7 de abril)

# Clase 6: Listas y Tuplas
## Sección 1 – Introducción a las Colecciones
* ¿Qué es una colección de datos?
* ¿Por qué necesitamos estructuras como listas y tuplas?

## Sección 2 – Listas en Python
* Definición y sintaxis
* Indexación y slicing
* Métodos comunes (append(), remove(), pop(), sort(), reverse())

## Sección 3 – Tuplas en Python
* Definición y diferencias con listas
* Inmutabilidad y cuándo usar tuplas
* Desempaquetado de tuplas

## Sección 4 – Iteración sobre Listas y Tuplas
* Recorrer listas con for
* List comprehension

### Ejercicios:
* Crear una lista con nombres y ordenarla alfabéticamente
* Convertir una lista en una tupla y viceversa
* Crear una lista de números y filtrar los pares usando list comprehension


# Clase 7: Diccionarios y Conjuntos

## Sección 1 – Diccionarios en Python
* ¿Qué es un diccionario y cuándo usarlo?
* Sintaxis y acceso a elementos
* Métodos (keys(), values(), items(), get())
* Modificación y eliminación de elementos

## Sección 2 – Conjuntos en Python
* Definición y diferencias con listas
* Métodos (add(), remove(), union(), intersection(), difference())
* Eliminación de duplicados con conjuntos

## Sección 3 – Iteración sobre Diccionarios y Conjuntos
* Recorrer diccionarios con for
* Uso de conjuntos para operaciones de filtrado

### Ejercicios:
* Crear un diccionario con información de un estudiante y actualizar su edad
* Contar la frecuencia de palabras en un texto usando diccionarios
* Encontrar elementos comunes entre dos listas usando conjuntos

[//]: # (Miércoles 9 de abril)

# Clase 8: Funciones, programación modular, clases y objetos

## Sección 1 – Funciones en Python
* ¿Qué es una función y por qué es útil?
* Sintaxis de una función (def)
* Parámetros y argumentos

## Sección 2 – Programación Modular
* Importar funciones desde otros archivos (import)
* Crear y usar módulos

## Sección 3 – Clases y Objetos
* Conceptos básicos de Programación Orientada a Objetos
* Creación de una clase (class)
* Métodos y atributos

### Ejercicios:
* Crear una función que calcule el área de un rectángulo
* Escribir una clase Persona con atributos como nombre y edad
* Crear un módulo que contenga funciones matemáticas básicas


# Clase 9: Manejo de String, Archivos, Manejo de Errores y Excepciones

## Sección 1 – Manejo de Archivos
* Apertura y lectura de archivos (open(), read())
* Escritura en archivos (write(), append())
* Uso de with para manejar archivos

## Sección 2 – Manejo de Errores y Excepciones
* ¿Qué es una excepción?
* try-except para manejar errores
* Excepciones comunes en Python (ZeroDivisionError, FileNotFoundError)
* Personalizar excepciones

### Ejercicios:
* Leer un archivo de texto y contar sus líneas
* Manejar un error al dividir entre cero
* Escribir en un archivo sin sobrescribir contenido anterior

[//]: # (Sábado 12 de abril)

# Clase 10: Introducción a Bibliotecas en Python

## Sección 1 – ¿Qué es una biblioteca?
* Definición y beneficios
* Librerías estándar vs. externas

## Sección 2 – Instalación y Uso de Librerías
* pip y conda para instalar librerías
* Importación y uso básico de bibliotecas comunes (math, random, datetime)

### Ejercicios:
* Generar un número aleatorio con random
* Obtener la fecha y hora actual con datetime
* Calcular la raíz cuadrada de un número usando math

## Sección 3 - Proyecto final


# Clase 11: Introducción a NumPy
## Sección 1 – ¿Qué es NumPy?
* Importancia de NumPy en ciencia de datos
* Diferencias entre listas y arreglos

## Sección 2 – Creación y Manipulación de Arreglos
* np.array()
* Indexación y slicing en arreglos
* Operaciones básicas con arreglos

### Ejercicios:
* Crear un arreglo NumPy con 10 elementos y acceder a ellos
* Realizar operaciones matemáticas en un arreglo


# Clase 12: Operaciones y Funciones en NumPy
## Sección 1 – Funciones de NumPy
* np.mean(), np.median(), np.std()
* Funciones matemáticas (sin, cos, log)

## Sección 2 – Manipulación Avanzada de Arreglos
* reshape(), concatenate(), split()

### Ejercicios:
* Calcular la media y la desviación estándar de un conjunto de datos

[//]: # (Lunes 14 de abril)

# Clase 13: Introducción a Pandas - Series y DataFrames

## Sección 1 – Introducción a Pandas
* ¿Qué es Pandas?
* Instalación de Pandas
* Concepto de Series y DataFrames
* Creación de Series y DataFrames
* Lectura y escritura de archivos (CSV, Excel, JSON)

## Sección 2 – Manipulación de Datos en Pandas
* Selección y filtrado de datos
* Modificación de datos
* Manejo de valores nulos
* Operaciones con columnas y filas
* Aplicación de funciones a columnas y filas

### Ejercicios:

* Lectura y análisis de un archivo CSV
* Filtrado y transformación de datos en un DataFrame


# Clase 14: Manipulación de Datos con Pandas

## Sección 1 – Análisis y Transformación de Datos
* Agrupamiento y agregación de datos
* Combinación y fusión de DataFrames
* Pivot tables y manejo de datos categóricos
* Aplicación de estadísticas descriptivas

## Sección 2 – Visualización con Pandas

* Introducción a la visualización con Pandas
* Creación de gráficos básicos (line, bar, hist, box)
* Personalización de gráficos
* Introducción a matplotlib y seaborn

### Ejercicios:
* Análisis exploratorio de datos con Pandas
* Visualización de tendencias en datos

[//]: # (Miércoles 16 de abril)

# Clase 15: Extras

* Maximiza la programación
* plugins (autocomplete, formato, detección de errores estático)
* asistentes de AI
* control de versiones y github
* cómo estructurar un proyecto con miras a producción
* importancia del control estricto de versiones para que sea reproducible

# Clase 16: Consultas


# Tareas
## Tarea 1
Se publica el sábado 5 y hay plazo hasta el lunes 7 para entregarlos
* Temática: Variables, condicionales y bucles
* Objetivo: 

## Tarea 2
Se publica el Lunes 7 y hay plazo hasta el Miércoles 9 para entregarlos
* Temática: Listas, tuplas, diccionarios, conjuntos
* Objetivo: 

## Tarea 3
Se publica el Miércoles 9 y hay plazo hasta el Sábado 12 para entregarlos
* Temática: funciones, clases y archivos
* Objetivo: 

## Tarea 4
Se publica el sábado 12 y hay plazo hasta el lunes 14 para entregarlos
* Temática: Numpy
* Objetivo: 

## Tarea 5
Se publica el Lunes 14 y hay plazo hasta el Miércoles 16 para entregarlos
* Temática: Pandas
* Objetivo: Trabajar con el dataset de datos del registro civil 



# Bibliografía:
- [Python for Everybody](https://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf)
- [Introduction to Python Programming](https://assets.openstax.org/oscms-prodcms/media/documents/Introduction_to_Python_Programming_-_WEB.pdf)
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
- [Automate the boring stuff](https://automatetheboringstuff.com/)


# Datasets
- [Datos registro civil montevideo](https://ckan.montevideo.gub.uy/dataset/partidas-de-registro-civil-de-montevideo)
- [Estadísticas de uso: Cómo Ir](https://ckan.montevideo.gub.uy/dataset/estadisticas-de-uso-como-ir)
- [Info frutas](https://www.fruityvice.com/)
- [Review Amazon](https://snap.stanford.edu/data/web-Amazon-links.html)
- [Open Apis](https://github.com/public-apis/public-apis?tab=readme-ov-file#food--drink)
