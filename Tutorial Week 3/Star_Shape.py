import turtle

screen = turtle.Screen()
tito = turtle.Turtle()
tito.pensize(3)

for i in range(0, 5):
    tito.forward(100)
    tito.left(2 * 360/5)

screen.exitonclick()