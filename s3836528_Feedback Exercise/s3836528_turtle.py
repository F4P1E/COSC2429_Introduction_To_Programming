# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022A
# Assignment: 1
# Author: Duong Phu Dong (s3836528)
# Created date: 10/11/2022
# Last modified date: 11/11/2022

import turtle

tito = turtle.Turtle()
tito.screen.bgcolor("black")  # background color change to black
tito.pensize(2)  # the size of pen
tito.color("green")

tito.left(90)

tito.backward(100)
tito.speed(200)
tito.shape('turtle')


def tree(i):
    if i < 10:
        return
    else:
        tito.forward(i)
        tito.color("orange")
        tito.circle(2)
        tito.color("brown")
        tito.left(30)
        tree(3 * i / 4)
        tito.right(60)
        tree(3 * i / 4)
        tito.left(30)
        tito.backward(i)


tree(100)
turtle.done()
