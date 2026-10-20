import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Entrada de valores de resistencia fija R1 y voltaje de alimentación (VIN)
R1 = 1000
R2 = 10000
R3 = 100000
VIN = 5

# Rango de valores de la resistencia variable
RVAR = np.arange(1, 100001, 100)

# Cálculo del voltaje de salida del divisor de tensión
VO1 = VIN * (RVAR / (R1 + RVAR))
VO2 = VIN * (RVAR / (R2 + RVAR))
VO3 = VIN * (RVAR / (R3 + RVAR))

# Combinar todos los datos en una matriz y guardarla como CSV
data_matrix = np.column_stack((RVAR, VO1, VO2, VO3))
df = pd.DataFrame(data_matrix, columns=['RVAR', 'VO1', 'VO2', 'VO3'])
df.to_csv('combined_data.csv', index=False)

# Graficar los datos
plt.plot(RVAR, VO1, 'k:', label='VO1')
plt.plot(RVAR, VO2, 'r*', label='VO2')
plt.plot(RVAR, VO3, 'b--', label='VO3')
plt.title("Gráfica Act 1 JRGM")
plt.xlabel("Resistencia variable")
plt.ylabel("Voltaje de salida")
plt.legend()
plt.savefig("divT_GGT.png")
plt.show()
