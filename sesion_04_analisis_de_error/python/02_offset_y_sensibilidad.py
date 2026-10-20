import numpy as np
import matplotlib.pyplot as plt

# Datos originales
datain = np.array([0.000, 1.000, 2.000, 3.000, 4.000, 5.000, 6.000, 7.000, 8.000, 9.000, 10.000])
dataoutup_original = np.array([-1.12, 0.21, 1.18, 2.09, 3.33, 4.50, 5.26, 6.59, 7.73, 8.68, 9.80])
dataoutdown_original = np.array([-0.69, 0.42, 1.65, 2.48, 3.62, 4.71, 5.87, 6.89, 7.92, 9.10, 10.20])

# 🚨 Parámetros independientes
# Para la salida ascendente
offset_up = 0
sensibilidad_up = 1

# Para la salida descendente
offset_down = 0
sensibilidad_down = 1

# Aplicar transformaciones
dataoutup_mod = dataoutup_original * sensibilidad_up + offset_up
dataoutdown_mod = dataoutdown_original * sensibilidad_down + offset_down

# Línea ideal
ideal_output = datain

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(datain, ideal_output, 'k--', label='Ideal (1:1)')
plt.plot(datain, dataoutup_mod, 'bo-', label=f'Salida Ascendente\nSensibilidad={sensibilidad_up}, Offset={offset_up}')
plt.plot(datain, dataoutdown_mod, 'ro-', label=f'Salida Descendente\nSensibilidad={sensibilidad_down}, Offset={offset_down}')

plt.title("Simulación con Offset y Sensibilidad Independientes")
plt.xlabel("Entrada")
plt.ylabel("Salida")
plt.grid(True)
plt.legend()
plt.ylim([-2, 14])
plt.tight_layout()
plt.savefig("salida_asc_desc_modificadas.png")
plt.show()
