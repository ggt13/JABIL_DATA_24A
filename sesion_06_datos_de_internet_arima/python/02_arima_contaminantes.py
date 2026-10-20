# -*- coding: utf-8 -*-
"""
### Parte 2: Análisis de Contaminantes
#### Autor: [Guillero García Torales]
#### Objetivo: Demostración de predicción de contaminantes utilizando modelos de regresión lineal y ARIMA
"""

# Importar las librerías necesarias
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from IPython.display import display, clear_output
from ipywidgets import widgets

# Cargar el archivo de datos (Asegúrate de cargar el archivo 'datos_2022.xlsx' en el entorno de Colab)
file_path = '/content/datos_2023.xlsx'  # Reemplaza con la ruta a tu archivo en Google Colab
sheet_name = 'base datos 2023'          #remplaza el nombre con el de la hoja de tu archivo

# Leer el archivo de Excel
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Mostrar las primeras filas del DataFrame
print(df.head())

# Extraer las columnas necesarias
#Asegúrate de que tu arhivo tenga estos nombres en sus columnas, sin espacio, acentos, etc...

data = df[['Estacion', 'Date_Time', 'SO2', 'NO', 'NO2', 'NOX', 'CO']]

# Crear un menú desplegable para seleccionar la estación
estaciones = data['Estacion'].unique()
estacion_selector = widgets.Dropdown(
    options=estaciones,
    description='Estación:',
    disabled=False,
)
display(estacion_selector)

# Crear un menú desplegable para seleccionar el contaminante
contaminantes = ['SO2', 'NO', 'NO2', 'NOX', 'CO']
contaminante_selector = widgets.Dropdown(
    options=contaminantes,
    description='Contaminante:',
    disabled=False,
)
display(contaminante_selector)

# Función para actualizar la gráfica y el análisis basado en la estación y el contaminante seleccionados
def analizar_estacion_contaminante(estacion, contaminante):
    # Limpiar la salida anterior
    clear_output(wait=True)
    display(estacion_selector)
    display(contaminante_selector)

    # Filtrar las filas donde la 'Estacion' es la seleccionada
    data_filtrada = data[data['Estacion'] == estacion]

    print(f"Datos filtrados para la estación: {estacion}")
    print(data_filtrada.head())

    # Convertir 'Date_Time' a formato datetime
    data_filtrada['Date_Time'] = pd.to_datetime(data_filtrada['Date_Time'])

    # Remover filas donde el contaminante contiene valores no válidos
    data_filtrada = data_filtrada[~data_filtrada[contaminante].isin(['IR', 'IF', 'ND'])]

    # Convertir el contaminante a valores numéricos, 'errors=coerce' convertirá los valores no numéricos a NaN
    data_filtrada[contaminante] = pd.to_numeric(data_filtrada[contaminante], errors='coerce')

    # Eliminar filas con valores NaN
    data_filtrada = data_filtrada.dropna(subset=[contaminante])

    print(f"Datos después del preprocesamiento para la estación: {estacion} y contaminante: {contaminante}")
    print(data_filtrada.head())

    if data_filtrada.shape[0] < 2:
        print(f"No hay suficientes datos para analizar {contaminante} en la estación {estacion}")
        return

    # Preparar los datos para la regresión lineal
    # Convertir 'Date_Time' a formato numérico (por ejemplo, timestamp)
    data_filtrada['Date_Time_Num'] = data_filtrada['Date_Time'].astype(int) / 10**9  # Convertir a segundos

    X = data_filtrada[['Date_Time_Num']]
    y = data_filtrada[contaminante]

    # Crear y ajustar el modelo de regresión lineal
    model = LinearRegression()
    model.fit(X, y)

    # Predecir usando el modelo
    data_filtrada[f'{contaminante}_Predicted'] = model.predict(X)

    # Graficar los resultados de la regresión lineal
    plt.figure(figsize=(10, 6))
    plt.scatter(data_filtrada['Date_Time'], data_filtrada[contaminante], color='blue', label=f'Actual {contaminante}')
    plt.plot(data_filtrada['Date_Time'], data_filtrada[f'{contaminante}_Predicted'], color='red', linewidth=2, label=f'Predicted {contaminante}')
    plt.xlabel('Date Time')
    plt.ylabel(contaminante)
    plt.title(f'Linear Regression of {contaminante} over Time ({estacion}) GGT')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Explicación de la gráfica de regresión lineal
    print(f"""
    Esta gráfica muestra los resultados del modelo de regresión lineal aplicado a los datos de {contaminante} para la estación {estacion}.
    - Los puntos azules representan los valores reales de {contaminante} a lo largo del tiempo.
    - La línea roja representa los valores predichos por el modelo de regresión lineal.
    Observamos cómo el modelo lineal intenta ajustar una línea recta a los datos de {contaminante}, lo que puede ayudar a identificar tendencias generales.
    """)

    # Usar 'Date_Time' como índice para el análisis de series temporales
    data_filtrada.set_index('Date_Time', inplace=True)

    # Ajustar el modelo ARIMA (los parámetros del orden pueden ajustarse)
    arima_model = ARIMA(data_filtrada[contaminante], order=(5, 1, 0))
    arima_result = arima_model.fit()

    # Predecir usando el modelo ARIMA
    data_filtrada[f'{contaminante}_ARIMA_Predicted'] = arima_result.predict(start=0, end=len(data_filtrada)-1, dynamic=False)

    # Graficar los resultados del ARIMA
    plt.figure(figsize=(10, 6))
    plt.plot(data_filtrada.index, data_filtrada[contaminante], color='blue', label=f'Actual {contaminante}')
    plt.plot(data_filtrada.index, data_filtrada[f'{contaminante}_ARIMA_Predicted'], color='green', linewidth=2, label=f'ARIMA Predicted {contaminante}')
    plt.xlabel('Date Time')
    plt.ylabel(contaminante)
    plt.title(f'ARIMA Analysis of {contaminante} over Time ({estacion}) GGT')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Explicación de la gráfica de ARIMA
    print(f"""
    Esta gráfica muestra los resultados del modelo ARIMA aplicado a los datos de {contaminante} para la estación {estacion}.
    - La línea azul representa los valores reales de {contaminante} a lo largo del tiempo.
    - La línea verde representa los valores predichos por el modelo ARIMA.
    Observamos cómo el modelo ARIMA sigue más de cerca los cambios en los datos de {contaminante} en comparación con el modelo de regresión lineal, capturando tanto las tendencias como las fluctuaciones.
    """)

# Conectar los menús desplegables a la función de análisis
def actualizar_analisis(change):
    analizar_estacion_contaminante(estacion_selector.value, contaminante_selector.value)

estacion_selector.observe(actualizar_analisis, names='value')
contaminante_selector.observe(actualizar_analisis, names='value')
