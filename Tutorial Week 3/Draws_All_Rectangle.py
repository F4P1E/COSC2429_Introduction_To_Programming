import turtle
screen = turtle.Screen()
tito = turtle.Turtle()
tito.pensize(3)

for i in range(0, 3):
    tito.forward(100)
    tito.left(120)

tito.up()
tito.goto(-100, -100)
tito.down()

for i in range(0, 4):
    tito.forward(100)
    tito.left(90)

tito.up()
tito.goto(-200, -200)
tito.down()

for i in range(0,6):
    tito.forward(100)
    tito.left(60)

tito.up()
tito.goto(100, 100)
tito.down()

for i in range(0, 8):
    tito.forward(100)
    tito.left(45)

screen.exitonclick()
