import numpy as np
import matplotlib.pyplot as plt
import csv

# Datos originales
distancias = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6])  # en cm
voltajes = np.array([0.0, 0.044, 0.225, 0.538, 1.408, 2.278, 2.947, 3.456, 3.978, 4.492, 4.814, 4.951, 5.0])  # en V

# Constantes
Vin = 5.0  # Voltaje de entrada
R_total = 100000  # Ohms

# Calcular resistencia en base al voltaje
resistencias = R_total * voltajes / Vin  # R = R_total * (Vout / Vin)

# Ajuste de curva: regresión polinómica (grado 3)
grado = 3
coeficientes = np.polyfit(distancias, resistencias, grado)
polinomio = np.poly1d(coeficientes)
resistencias_calculadas = polinomio(distancias)

# Guardar tabla en CSV
with open("tabla_resistencias.csv", mode="w", newline="") as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerow(["Distancia (cm)", "Resistencia (Ohmios)"])
    for d, r in zip(distancias, resistencias):
        escritor.writerow([d, round(r, 2)])

# Crear gráfica
plt.figure(figsize=(8, 5))
plt.plot(distancias, resistencias, 'o', label="Datos Calculados", color='blue')
plt.plot(distancias, resistencias_calculadas, '-', label=f"Ajuste Polinómico (grado {grado})", color='green')
plt.title("Resistencia vs Distancia en Potenciómetro de 100kΩ")
plt.xlabel("Distancia (cm)")
plt.ylabel("Resistencia (Ω)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("grafica_resistencia_vs_distancia.png")
plt.show()
