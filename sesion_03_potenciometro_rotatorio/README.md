# Sesión 3 · Generación, manipulación y caracterización de datos con un dispositivo

**Objetivo.** Medir con el Arduino el voltaje de un potenciómetro rotatorio contra el ángulo, subiendo y bajando, y analizar la histéresis y la relación ángulo–resistencia.

**Herramientas.** Arduino · Python en Colab

La presentación de la sesión y los archivos de datos grandes están en Classroom.

## Archivos

| Archivo | Qué es | Versión |
|---|---|---|
| [`arduino/sketch_potL_aex/sketch_potL_aex.ino`](arduino/sketch_potL_aex/sketch_potL_aex.ino) | programa para cargar en el Arduino | 2024 |
| [`datos/datos_pot.py`](datos/datos_pot.py) | datos | 2025 |
| [`python/01_graficar_datos.py`](python/01_graficar_datos.py) | programa de Python (se pega en una celda de Colab) | 2025 |
| [`python/02_grafica_resistencia_angulo.py`](python/02_grafica_resistencia_angulo.py) | programa de Python (se pega en una celda de Colab) | 2025 |

## Cargar el programa en el Arduino

Descargue la carpeta completa del programa (el IDE de Arduino exige que el archivo `.ino` esté dentro de una carpeta con su mismo nombre), ábrala con el IDE y súbala a la tarjeta. Los datos se leen en el Monitor Serie a 9600 baudios.
