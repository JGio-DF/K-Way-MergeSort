# External Merge Sort

> 323063609 - Delgado Flores Jesús Giovani

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

A través de esta investigación y del desarrollo del proyecto, logramos comprender la importancia del External Merge Sort como una alternativa para organizar grandes cantidades de información cuando estas superan la capacidad disponible de la memoria RAM.

Durante el estudio del algoritmo identificamos sus dos etapas principales, comprendimos la función del Min-Heap como una herramienta que facilita la selección del menor elemento de cada fragmento, permitiendo construir un archivo final ordenado de manera eficiente.

La implementación en Python nos permitió llevar los conceptos teóricos a la práctica, observar cómo se administran los archivos temporales y comprender la importancia de utilizar adecuadamente la memoria y el almacenamiento durante el procesamiento de los datos. Del mismo modo, reconocimos que el tamaño de los fragmentos influye en la cantidad de archivos temporales generados y en el rendimiento general del algoritmo.

Finalmente, este proyecto nos permitió reforzar nuestros conocimientos sobre algoritmos de ordenamiento, estructuras de datos y manejo de archivos, además de desarrollar habilidades de investigación, programación y trabajo en equipo. Concluimos que el Ordenamiento Externo es una solución útil para el procesamiento de grandes volúmenes de información y que conocer su funcionamiento nos ayuda a comprender cómo se resuelven problemas computacionales cuando los recursos disponibles son limitados.

---
## Referencias

- External sorting — Wikipedia — Aportó los fundamentos del ordenamiento externo, su necesidad cuando los datos no caben en memoria principal y el funcionamiento general de sus fases. https://en.wikipedia.org/wiki/External_sorting
- File Handling in Python — GeeksforGeeks — Aportó información sobre la apertura, lectura, escritura y cierre de archivos en Python, necesaria para trabajar con archivos de entrada, temporales y de salida. https://www.geeksforgeeks.org/python/file-handling-python/
- K-way merge algorithm — Wikipedia — Aportó información sobre la mezcla de múltiples secuencias ordenadas y las estrategias utilizadas para realizarla, incluyendo el uso de heaps. https://en.wikipedia.org/wiki/K-way_merge_algorithm
- chunk — Documentación oficial de Python 3.8 — Se consultó como referencia sobre el concepto de fragmentos (chunks) en archivos. https://docs.python.org/es/3.8/library/chunk.html
- Merge Sort — GeeksforGeeks — Aportó los fundamentos del algoritmo Merge Sort, su estrategia de dividir y combinar y su aplicación para ordenar los fragmentos en memoria. https://www.geeksforgeeks.org/dsa/merge-sort/
- K-way Merge: A Comprehensive Guide to Merging Sorted Arrays — AlgoCademy — Aportó una explicación complementaria del K-way Merge, sus aplicaciones, implementación y análisis de complejidad temporal y espacial. https://algocademy.com/blog/k-way-merge-a-comprehensive-guide-to-merging-sorted-arrays/
- External Merge Sort — GitHub — Se tomó como referencia complementaria para consultar un proyecto de implementación del algoritmo External Merge Sort en Python. https://github.com/melvilgit/external-Merge-Sort
