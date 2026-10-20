# Sesión 1 · Generación de datos por medio de una ecuación

**Objetivo.** Generar en Colab los datos de tres divisores de tensión, reproducir la gráfica en una hoja de cálculo a partir de `combined_data.csv` y analizar sus errores.

**Herramientas.** Python en Colab · Google Sheets o Excel

La presentación de la sesión y los archivos de datos grandes están en Classroom.

## Archivos

| Archivo | Qué es | Versión |
|---|---|---|
| [`arduino/sketch_divT/sketch_divT.ino`](arduino/sketch_divT/sketch_divT.ino) | programa para cargar en el Arduino | 2024 |
| [`datos/combined_data.csv`](datos/combined_data.csv) | datos | 2024 |
| [`python/divisor_de_tension.py`](python/divisor_de_tension.py) | programa de Python (se pega en una celda de Colab) | 2025 |

## Cargar el programa en el Arduino

Descargue la carpeta completa del programa (el IDE de Arduino exige que el archivo `.ino` esté dentro de una carpeta con su mismo nombre), ábrala con el IDE y súbala a la tarjeta. Los datos se leen en el Monitor Serie a 9600 baudios.
