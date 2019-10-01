import turtle

def legnth_of_hexagon_side():
    side = input("What is the length of the hexagons side")
    return side

def color_of_flowers_petals():
    input("What color do you want your flowers petals to be?")


def color_of_flowers_center():
    input("What color do you want your flowers center to be?")


def hexagon():
    for x in range(6):
        turtle.forward(side)
        turtle.left(60)


def makeflower():
    turtle.color()
    turtle.begin_fill()
    hexagon()
    turtle.end_fill()


turtle.exitonclick()
