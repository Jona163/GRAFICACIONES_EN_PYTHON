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
