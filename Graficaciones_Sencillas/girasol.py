import math
import turtle

# Configuración inicial de la ventana y la tortuga
turtle.bgcolor("black")
turtle.shape("turtle")
turtle.speed(0)
turtle.fillcolor("brown")
turtle.color("brown")  # Color del centro del girasol

# Constante phi para calcular los ángulos
phi = 137.5 * (math.pi / 180.0)  # Convertimos a radianes

# Dibujar el girasol
for i in range(200):  # Aumentar el número de iteraciones para un girasol más completo
    r = 4 * math.sqrt(i)  # Calcular el radio para la posición
    theta = i * phi  # Calcular el ángulo
