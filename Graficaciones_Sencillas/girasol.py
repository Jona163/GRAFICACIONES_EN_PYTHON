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

    # Calcular las coordenadas x, y
    x = r * math.cos(theta)
    y = r * math.sin(theta)

    # Mover la tortuga a la nueva posición
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(i * 137.5)  # Orientar la tortuga
    turtle.pendown()

    # Dibujar el centro o los pétalos
    if i < 100:  # Los primeros 100 serán el centro del girasol
        turtle.stamp()
    else:
        turtle.fillcolor("yellow")  # Cambiar el color a amarillo para los pétalos
        turtle.begin_fill()
        for _ in range(2):  # Dibujar el pétalo
            turtle.forward(70)
            turtle.left(40)
            turtle.forward(70)
            turtle.left(140)
        turtle.end_fill()

# Esconder la tortuga al final
turtle.hideturtle()

# Mantener la ventana abierta
turtle.done()
