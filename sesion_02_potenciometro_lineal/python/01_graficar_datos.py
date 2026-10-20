import matplotlib.pyplot as plt

# Datos proporcionados
distancias_cm = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]
voltajes_v = [0.0, 0.044, 0.225, 0.538, 1.408, 2.278, 2.947, 3.456, 3.978, 4.492, 4.814, 4.951, 5.0]

# Crear la gráfica
plt.figure(figsize=(8, 5))
plt.plot(distancias_cm, voltajes_v, marker='o', linestyle='-', color='b')

# Etiquetas y título
plt.title('Voltaje vs Distancia del Potenciómetro Slider')
plt.xlabel('Distancia (cm)')
plt.ylabel('Voltaje (V)')
plt.grid(True)
plt.tight_layout()

# Mostrar la gráfica
plt.show()
