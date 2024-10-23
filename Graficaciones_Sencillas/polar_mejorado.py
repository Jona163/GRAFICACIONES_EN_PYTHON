import numpy as np
import matplotlib.pyplot as plt
import math

# Configuración del gráfico polar
plt.axes(projection='polar')

# Parámetros
x = 5
y = 8

# Rango de valores para los ángulos (rad)
rads = np.arange(0, 8 * np.pi, 0.01)  # Empezamos desde 0 para cubrir todo el rango

# Calcular los valores de r para cada radian
r = (x * y) / np.sqrt((x * np.sin(rads))**2 + (y * np.cos(rads))**2)

# Graficar los puntos en el gráfico polar
plt.polar(rads, r, 'g.')  # 'g.' indica puntos verdes

# Mostrar el gráfico
plt.show()
