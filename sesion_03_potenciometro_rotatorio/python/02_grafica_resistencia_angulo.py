import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Datos
voltaje_ascendente = [0.000, 0.000, 0.005, 0.220, 0.415, 0.606, 0.821, 1.007, 1.183, 1.393, 1.603, 1.808, 2.028, 2.278, 2.473, 2.669, 2.874, 3.079, 3.309, 3.524, 3.739, 3.930, 4.120, 4.301, 4.506, 4.663, 4.848, 5, 5, 5]
grados = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290]

# Constantes
Vin = 5.0          # Voltaje de entrada
R_pot = 100000.0   # Resistencia total del potenciómetro (100kΩ)

# Calcular R2 usando la fórmula del divisor de voltaje
resistencia = [(Vout * R_pot) / Vin for Vout in voltaje_ascendente]

# Ajustar una función polinomial (grado 2)
coef = np.polyfit(grados, resistencia, 2)
polinomio = np.poly1d(coef)

# Crear puntos para graficar la curva ajustada
grados_fit = np.linspace(0, 290, 300)
resistencia_fit = polinomio(grados_fit)

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(grados, resistencia, 'bo', label='Datos calculados')
plt.plot(grados_fit, resistencia_fit, 'r-', label=f'Ajuste: {coef[0]:.2e}·x² + {coef[1]:.2e}·x + {coef[2]:.2f}')
plt.title('Relación entre Grados y Resistencia (R2)')
plt.xlabel('Grados')
plt.ylabel('Resistencia (Ω)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()