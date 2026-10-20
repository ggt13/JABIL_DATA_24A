import matplotlib.pyplot as plt

# Datos
entrada = [0.000, 1.000, 2.000, 3.000, 4.000, 5.000, 6.000, 7.000, 8.000, 9.000, 10.000]
salidaAsc = [-1.12, 0.21, 1.18, 2.09, 3.33, 4.50, 5.26, 6.59, 7.73, 8.68, 9.80]
salidaDesc = [-0.69, 0.42, 1.65, 2.48, 3.62, 4.71, 5.87, 6.89, 7.92, 9.10, 10.20]
salidaIdeal = [0.000, 1.000, 2.000, 3.000, 4.000, 5.000, 6.000, 7.000, 8.000, 9.000, 10.000]

# Graficar
plt.figure(figsize=(8, 6))
plt.plot(entrada, salidaAsc, 'o-', label='Salida Ascendente')
plt.plot(entrada, salidaDesc, 's-', label='Salida Descendente')
plt.plot(entrada, salidaIdeal, 'k-', label='Salida Ideal')

# Etiquetas y título
plt.xlabel('Entrada')
plt.ylabel('Salida')
plt.title('Comparación de Salidas vs Entrada')
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.tight_layout()
plt.show()
