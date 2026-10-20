# Sistemas de adquisición de datos

**TSU en Electrónica y Pruebas · Jabil** · Dr. Guillermo García Torales (CUCEI, Universidad de Guadalajara)

Programas, cuadernos de Colab y datos de las ocho sesiones del curso. Las presentaciones, las instrucciones de cada actividad y las entregas viven en Google Classroom; aquí está lo que se ejecuta.

## Mapa del curso

| Sesión | Tema | Herramientas |
|---|---|---|
| 0 | [Presentación del curso](sesion_00_presentacion/) | Google Colab |
| 1 | [Generación de datos por medio de una ecuación](sesion_01_datos_por_ecuacion/) | Python en Colab · Google Sheets o Excel |
| 2 | [Generación de datos con un dispositivo y caracterización asistida por IA](sesion_02_potenciometro_lineal/) | Arduino · Python en Colab · asistente de IA |
| 3 | [Generación, manipulación y caracterización de datos con un dispositivo](sesion_03_potenciometro_rotatorio/) | Arduino · Python en Colab |
| 4 | [Generación, manipulación y análisis de error de datos sintéticos](sesion_04_analisis_de_error/) | Python en Colab · asistente de IA |
| 5 | [Análisis de tendencias con datos sintéticos](sesion_05_tendencias_y_ruido/) | Python en Colab (ipywidgets) · Google Sheets o Excel |
| 6 | [Análisis de datos a partir de información en internet](sesion_06_datos_de_internet_arima/) | Python en Colab (statsmodels) · datos públicos |
| 7 | [Análisis de datos para el mantenimiento de motores](sesion_07_mantenimiento_de_motores/) | Python en Colab (scikit-learn, seaborn) · Google Sheets o Excel |
| 8 | [Generación de datos con una IA](sesion_08_datos_con_ia/) | Python en Colab · generador de imágenes con IA |

## Cómo usar este repositorio (alumnos)

1. Entre a la carpeta de la sesión: su `README` dice qué hay y para qué sirve cada archivo.
2. Los cuadernos (`.ipynb`) se abren directamente en Google Colab con el botón **Abrir en Colab**.
3. Los programas de Python (`.py`) se copian en una celda de Colab y se ejecutan.
4. Los programas de Arduino se descargan con su carpeta y se abren con el IDE de Arduino.
5. Para descargar todo el curso: botón verde **Code → Download ZIP**.

## Organización

```
sesion_NN_tema/
├── README.md      qué hay en la sesión
├── arduino/       un programa por carpeta
├── python/        programas de Python
├── notebooks/     cuadernos de Colab
├── datos/         datos de entrada
└── figuras/       resultados de ejemplo
```

## Versiones

Cada generación del curso queda marcada con una etiqueta (*tag*): `v2024A` es el curso de 2024 antes de esta reorganización. Para ver una versión anterior: menú de ramas → pestaña **Tags**.

## Videos de consulta

- NI · Conceptos fundamentales de adquisición de datos y sensores: https://www.youtube.com/watch?v=uL37PFoHOzA
- ¿Qué es un sistema de adquisición de datos (DAQ)?: https://www.youtube.com/watch?v=-0LzMfhoSts
- NI · ¿Qué es CompactRIO?: https://www.youtube.com/watch?v=ksaeXq84PAg
- Regresión lineal por mínimos cuadrados en Excel: https://www.youtube.com/watch?v=N82LfxJTpa4
- Videos complementarios: https://www.youtube.com/watch?v=bwatwGpDuFM · https://www.youtube.com/watch?v=bnOBA0MQhlI

## Licencia

GPL-3.0. Vea el archivo `LICENSE`.
