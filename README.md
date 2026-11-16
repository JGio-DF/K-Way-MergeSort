# External Merge Sort

> Núm. cuenta - Delgado Flores Jesús Giovani

> 323134745 - Luna Gutierrez Sayuri

> 323023834 - Medina Alonso Patrick

> Núm. cuenta - Riveroll Hernández Alexis Eduardo


---

### Descripción del proyecto

Este proyecto aborda el funcionamiento del algoritmo External Merge Sort (Ordenamiento Externo), el cual es una técnica utilizada para ordenar grandes cantidades de datos que no pueden almacenarse completamente en la memoria principal (RAM) de una computadora.

Lo haremos a través de una explicación teórica y una implementación en Python, se estudiará cómo dividir un archivo en fragmentos pequeños, ordenarlos individualmente y posteriormente combinarlos mediante una estrategia de mezcla de múltiples vías (K-way Merge), utilizando un Min-Heap para optimizar el proceso.

El proyecto nos permitirá comprender la importancia de la administración de memoria, el manejo de archivos en disco y el análisis de eficiencia de los algoritmos cuando se trabaja con grandes volúmenes de información.

### Objetivo

Investigar, comprender e implementar el algoritmo de External Merge Sort mediante Python, analizando su funcionamiento, las estructuras de datos que utiliza y su rendimiento al ordenar archivos que superan la capacidad disponible de la memoria RAM. Asimismo, se busca aplicar los conocimientos adquiridos en la asignatura de Estructura de Datos y Algoritmos II, trabajar colaborativamente y comunicar los resultados mediante una exposición y una demostración práctica.

## Contexto y teoría

¿Qué es el Ordenamiento Externo?

El Ordenamiento Externo es un algoritmo diseñado para ordenar archivos de gran tamaño cuando estos exceden la capacidad de la memoria principal de una computadora.
A diferencia de los algoritmos de ordenamiento interno, que trabajan principalmente con datos almacenados en RAM, el Ordenamiento Externo utiliza el almacenamiento secundario (disco) para procesar la información por partes.

Su funcionamiento se divide principalmente en dos fases:


**Fase 1. Generación de runs (fragmentos ordenados)**

1. Se lee una parte del archivo original, denominada chunk, cuyo tamaño debe ajustarse a la memoria disponible.
2. El fragmento se ordena en memoria utilizando un algoritmo de ordenamiento interno, como Merge Sort.
3. El bloque ordenado se guarda en disco como un archivo temporal denominado run.
4. El procedimiento se repite hasta procesar todos los datos del archivo original.


**Fase 2. Mezcla de runs (Merge)**

Una vez generados los archivos temporales ordenados, se realiza una mezcla de múltiples vías (K-way Merge) para obtener un único archivo completamente ordenado.
Para llevar a cabo esta fase se utiliza un Min-Heap, una estructura de datos que permite mantener el menor elemento disponible en la raíz.

El procedimiento consiste en:

1. Leer el primer elemento de cada run.
2. Insertar los elementos en el Min-Heap.
3. Extraer el elemento mínimo y escribirlo en el archivo de salida.
4. Leer el siguiente elemento del mismo run del que provino el valor extraído.
5. Insertar el nuevo elemento en el Heap.
6. Repetir el procedimiento hasta procesar todos los elementos.


| Concepto | Descripción |
|---|---|
| RAM | Memoria principal utilizada para procesar temporalmente los datos |
| Chunk | Fragmento del archivo original que se carga en memoria para ordenarlo |
| Run | Fragmento ordenado que se almacena temporalmente en el disco |
| Merge | Proceso de combinación de varios fragmentos ordenados |
| Min-Heap | Estructura de datos que mantiene el menor elemento en la raíz, facilitando su extracción |
| K-way Merge | Técnica que permite combinar K archivos ordenados simultáneamente en uno solo |
| Buffer | Espacio temporal de memoria utilizado para facilitar la lectura y escritura de datos |


### Complejidad y rendimiento

Durante la fase de mezcla, cada uno de los N elementos se procesa mediante operaciones de extracción e inserción en un Min-Heap de tamaño K.

**Tiempo de mezcla: O(N log K).**

**Espacio del Min-Heap: O(K).**

El tamaño de los chunks también influye en el rendimiento: los fragmentos más grandes generan menos runs y, por lo general, reducen el trabajo de mezcla. Sin embargo, deben respetar la memoria disponible para el procesamiento y los buffers. Además, el acceso secuencial al disco es importante para reducir operaciones de búsqueda y mejorar la eficiencia de lectura y escritura.

---
## Demo


---
## Análisis de resultados



---
## Conclusiones



---
## Referencias

- Ola
