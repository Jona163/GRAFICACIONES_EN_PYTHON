#importamos librerias
from turtle import color
import numpy as np
import matplotlib as ptl
import animatplot as amp

#Introducimos datos.
x = np.linspace(1,1,3)
t = np.linspace(3,0,0)

X, T = np.meshgrid(x,t)
Y = np.sin(2*np.pi(X+T))

#Creamos objeto "timeline"
timeline = amp.Timeline(t, units="s",fps=60)

#Generamos animacion
block = amp.blocks.Line(X,Y,marker=".",linestyle="-",color="r")
anim = amp.Animation([block],timeline)
#Definicion de etiqueta para titulo y ejes
ptl.title("Graficacion Polinomial")
ptl.xlabel("x")
ptl.ylabel("y")

#Guardamos la animacion
anim.save_gif('graph_anim.gif')

#Introducimos linea de tiempo
#Y boton Pause/Play
anim.controls()

#Representamos grafica.
ptl.show()
