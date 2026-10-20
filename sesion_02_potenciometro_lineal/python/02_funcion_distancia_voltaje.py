import numpy as np
import matplotlib.pyplot as plt
import csv

# Datos
distancias = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6])
voltajes_medidos = np.array([0.0, 0.044, 0.225, 0.538, 1.408, 2.278, 2.947, 3.456, 3.978, 4.492, 4.814, 4.951, 5.0])

# Ajuste de una función polinómica (grado 3 es una buena elección para este comportamiento)
grado = 3
coeficientes = np.polyfit(distancias, voltajes_medidos, grado)
polinomio = np.poly1d(coeficientes)

# Calcular voltajes estimados
voltajes_calculados = polinomio(distancias)

# Guardar datos en CSV
with open("tabla_datos.csv", mode="w", newline="") as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerow(["Distancia (cm)", "Voltaje Medido (V)", "Voltaje Calculado (V)"])
    for d, vm, vc in zip(distancias, voltajes_medidos, voltajes_calculados):
        escritor.writerow([d, round(vm, 4), round(vc, 4)])

# Crear gráfica
plt.figure(figsize=(8, 5))
plt.plot(distancias, voltajes_medidos, 'o', label="Datos Medidos", color='blue')
plt.plot(distancias, voltajes_calculados, '-', label=f"Ajuste Polinómico (grado {grado})", color='red')
plt.title("Comparación: Voltaje Medido vs Calculado")
plt.xlabel("Distancia (cm)")
plt.ylabel("Voltaje (V)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("grafica_comparativa.png")  # Guardar la imagen
plt.show()
