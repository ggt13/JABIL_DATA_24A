# Sesión 7 · Análisis de datos para el mantenimiento de motores

**Objetivo.** Aplicar agrupamiento (k-means) y matrices de correlación a datos de vibración y fallas de un motor, e interpretar las correlaciones en términos de su operación.

**Herramientas.** Python en Colab (scikit-learn, seaborn) · Google Sheets o Excel

La presentación de la sesión y los archivos de datos grandes están en Classroom.

## Archivos

| Archivo | Qué es | Versión |
|---|---|---|
| [`datos/data.csv`](datos/data.csv) | datos | 2024 |
| [`notebooks/mantenimiento_predictivo_motor_2024.ipynb`](notebooks/mantenimiento_predictivo_motor_2024.ipynb) | cuaderno de Colab | 2024 |
| [`notebooks/sesion_07_mantenimiento.ipynb`](notebooks/sesion_07_mantenimiento.ipynb) | cuaderno de Colab | 2025 |
| [`python/mantenimiento_predictivo.py`](python/mantenimiento_predictivo.py) | programa de Python (se pega en una celda de Colab) | 2024 |

## Abrir en Colab

- `mantenimiento_predictivo_motor_2024.ipynb` [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ggt13/JABIL_DATA_24A/blob/main/sesion_07_mantenimiento_de_motores/notebooks/mantenimiento_predictivo_motor_2024.ipynb)
- `sesion_07_mantenimiento.ipynb` [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ggt13/JABIL_DATA_24A/blob/main/sesion_07_mantenimiento_de_motores/notebooks/sesion_07_mantenimiento.ipynb)

## Notas de revisión

- **datos/data.csv**: Tiene cuatro renglones vacíos al final; pandas los lee como valores faltantes.
