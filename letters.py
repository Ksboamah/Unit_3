# By Kwame Boamah

import turtle

turtle.speed(0)

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


def p():
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.right(10)
    for z in range(230):
        turtle.forward(1)
        turtle.left(0.9)
    turtle.left(60)

def space():
    turtle.penup()
    turtle.seth(0)
    turtle.forward(20)
    turtle.pendown()



def mississippi():
    m()
    space()
    i()
    space()
    turtle.penup()
    turtle.left(90)
    turtle.forward(100)
    turtle.seth(0)
    turtle.pendown()


mississippi()

turtle.exitonclick()
