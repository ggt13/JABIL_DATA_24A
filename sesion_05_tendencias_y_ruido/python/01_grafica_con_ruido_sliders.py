import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from ipywidgets import interact, FloatSlider, IntSlider
import ipywidgets as widgets

# Función que genera, grafica y guarda los datos simulados
def graficar_datos(nivel_ruido=2.0, pendiente=0.5, cantidad_puntos=1000):
    # Generar datos
    tiempo = np.linspace(1, 100, cantidad_puntos)
    temperatura = pendiente * tiempo + 10 + np.random.randn(cantidad_puntos) * nivel_ruido

    # Ajuste por mínimos cuadrados
    X = np.vstack((np.ones_like(tiempo), tiempo))
    coeficientes = np.linalg.lstsq(X.T, temperatura, rcond=None)[0]
    valores_ajustados = X.T @ coeficientes

    # Guardar en archivo CSV
    df = pd.DataFrame({
        'tiempo': tiempo,
        'temperatura': temperatura
    })
    df.to_csv('datos_simulados.csv', index=False)

    # Graficar
    plt.figure(figsize=(10, 6))
    plt.plot(tiempo, temperatura, '.', markersize=5, label='Datos simulados')
    plt.plot(tiempo, valores_ajustados, 'r', linewidth=2, label='Recta ajustada')
    plt.xlabel('Tiempo')
    plt.ylabel('Temperatura')
    plt.title(f'Ajuste por mínimos cuadrados (Ruido = {nivel_ruido}, Pendiente = {pendiente})')
    plt.legend()
    plt.grid(True)
    plt.show()

# Controles interactivos
interact(
    graficar_datos,
    nivel_ruido=FloatSlider(value=2.0, min=0.0, max=10.0, step=0.1, description='Ruido'),
    pendiente=FloatSlider(value=0.5, min=-2.0, max=2.0, step=0.1, description='Pendiente'),
    cantidad_puntos=IntSlider(value=100, min=50, max=1000, step=10, description='N° puntos')
);
