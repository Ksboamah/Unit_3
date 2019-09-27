# By Kwame Boamah

import turtle


def m():
    for x in range(2):
        turtle.left(90)
        turtle.forward(100)
        turtle.right(135)
        turtle.forward(100)


def i():
    turtle.left(90)
    turtle.forward(100)


def s():
    turtle.right(10)
    for z in range(200):
        turtle.forward(1)
        turtle.left(0.9)
    for y in range(200):
        turtle.right(0.9)
        turtle.forward(1)



turtle.exitonclick()