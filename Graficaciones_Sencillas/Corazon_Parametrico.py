
import turtle
import time

# Movimiento de curva
def curveMove():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)


def drawHeart():
    turtle.title("")
    turtle.speed(1) # La velocidad del cepillo se ajusta al máximo
    turtle.color('red','pink')
    turtle.begin_fill()
    turtle.left(140) # Gire 140 grados en sentido antihorario
    turtle.forward(111.65) # Avanzar 111,65 píxeles
