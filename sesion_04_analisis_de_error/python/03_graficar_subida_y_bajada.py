import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Datos
datain = np.array([0.000, 1.000, 2.000, 3.000, 4.000, 5.000, 6.000, 7.000, 8.000, 9.000, 10.000])
dataoutup = np.array([-1.12, 0.21, 1.18, 2.09, 3.33, 4.50, 5.26, 6.59, 7.73, 8.68, 9.80])
dataoutdown = np.array([-0.69, 0.42, 1.65, 2.48, 3.62, 4.71, 5.87, 6.89, 7.92, 9.10, 10.20])

# Crear gráfica
plt.figure(figsize=(8, 6))
plt.plot(datain, dataoutup, marker='o', label='Salida Ascendente')
plt.plot(datain, dataoutdown, marker='s', label='Salida Descendente')
plt.title('Lecturas del Sensor')
plt.xlabel('Entrada')
plt.ylabel('Salida')
plt.grid(True)
plt.legend()
plt.tight_layout()

# Guardar como imagen PNG
plt.savefig('grafica_lecturas_sensor.png')
plt.close()

# Crear DataFrame para CSV
df = pd.DataFrame({
    'Entrada': datain,
    'Salida_Ascendente': dataoutup,
    'Salida_Descendente': dataoutdown
})

# Guardar en archivo CSV
df.to_csv('lecturas_sensor.csv', index=False)

print("Gráfica guardada como 'grafica_lecturas_sensor.png'")
print("Datos guardados en 'lecturas_sensor.csv'")
