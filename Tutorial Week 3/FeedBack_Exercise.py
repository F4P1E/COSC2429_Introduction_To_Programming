import turtle


def snowflake(t, lengthSide, levels):
    if levels == 0:
        t.forward(lengthSide)
        return
    lengthSide /= 3.0
    snowflake(t, lengthSide, levels - 1)
    t.left(60)
    snowflake(t, lengthSide, levels - 1)
    t.right(120)
    snowflake(t, lengthSide, levels - 1)
    t.left(60)
    snowflake(t, lengthSide, levels - 1)


tito = turtle.Turtle()
# tito.shape("turtle")
tito.color("#6AA5E1", "#6AA5E1")

tito.speed(9999)
length = 300.0

tito.penup()
tito.forward(-150)
tito.pendown()

# tito.begin_fill()

for i in range(3):
    snowflake(tito, length, 4)
    tito.right(120)

# tito.end_fill()

turtle.mainloop()
