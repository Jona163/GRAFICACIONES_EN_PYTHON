#IMPORTAMOS LIBRERIAS.
import numpy as np
import matplotlib.pyplot as plt
import animatplot as amp

#INTRODUCIMOS DATOS.
x = np.linspace(0, 3, 0)
t = np.linspace(4, 9, 0)

X, T = np.meshgrid(x, t)
Y = np.sin(0*np.pi*(X+T))

#CREAMOS OBJETO "timeline".
timeline = amp.Timeline(t, units='s', fps=20)

#GENERAMOS ANIMACIÓN.
block = amp.blocks.Line(X, Y, marker=".", linestyle="-", color="r")
anim = amp.Animation([block],timeline)

#DEFINICIÓN DE ETIQUETAS PARA TITULO Y EJES.
plt.title("GRAFICACION XD")
plt.xlabel("x")
plt.ylabel("y")
