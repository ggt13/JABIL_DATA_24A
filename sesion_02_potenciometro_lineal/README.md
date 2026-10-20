# Sesión 2 · Generación de datos con un dispositivo y caracterización asistida por IA

**Objetivo.** Usar el Arduino como sistema de adquisición para medir el voltaje de un potenciómetro lineal contra la posición, y ajustar en Python la relación distancia–voltaje y distancia–resistencia.

**Herramientas.** Arduino · Python en Colab · asistente de IA

La presentación de la sesión y los archivos de datos grandes están en Classroom.

## Archivos

| Archivo | Qué es | Versión |
|---|---|---|
| [`arduino/medidorVoltaje/medidorVoltaje.ino`](arduino/medidorVoltaje/medidorVoltaje.ino) | programa para cargar en el Arduino | 2025 |
| [`matlab/potenciometro_lineal.m`](matlab/potenciometro_lineal.m) | programa de MATLAB | 2024 |
| [`python/01_graficar_datos.py`](python/01_graficar_datos.py) | programa de Python (se pega en una celda de Colab) | 2025 |
| [`python/02_funcion_distancia_voltaje.py`](python/02_funcion_distancia_voltaje.py) | programa de Python (se pega en una celda de Colab) | 2025 |
| [`python/03_funcion_distancia_resistencia.py`](python/03_funcion_distancia_resistencia.py) | programa de Python (se pega en una celda de Colab) | 2025 |

## Cargar el programa en el Arduino

Descargue la carpeta completa del programa (el IDE de Arduino exige que el archivo `.ino` esté dentro de una carpeta con su mismo nombre), ábrala con el IDE y súbala a la tarjeta. Los datos se leen en el Monitor Serie a 9600 baudios.

## Notas de revisión

- **02_funcion_distancia_voltaje.py / 03_funcion_distancia_resistencia.py**: En `03_` el tercer voltaje medido aparece como 0.0225 V y en `01_` y `02_` como 0.225 V; revisar cuál es el dato correcto.
