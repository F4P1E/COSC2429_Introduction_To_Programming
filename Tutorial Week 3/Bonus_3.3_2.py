import turtle

screen = turtle.Screen()
tito = turtle.Turtle()
tito.pensize(3)


def drawPolygon(size):
    for i in range(0, size):
        tito.forward(100)
        tito.left(360 / size)


for i in ["3", "4", "6", "8"]:
    drawPolygon(int(i))

screen.exitonclick()
