import random
import turtle


window = turtle.Screen()


turtle.bgcolor("red")
star = turtle.Turtle()
star.pensize(2)
star.pencolor("yellow")
star.fillcolor("yellow")
star.begin_fill()
star.penup()
star.goto(200,50)
star.pendown()
for i in range(5):
    star.right(144)
    star.forward(400)
star.end_fill()
star.hideturtle()

window.exitonclick()
