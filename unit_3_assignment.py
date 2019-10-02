import turtle

t = turtle.Pen()


def legnth_of_hexagon_side():
    side = int(input("What is the length of the hexagons side?"))
    return side


def color_of_flowers_petals():
    return input("What color do you want your flowers petals to be?")


def color_of_flowers_center():
    return input("What color do you want your flowers center to be?")


def hexagon1(side):
    for x in range(6):
        t.forward(side)
        t.left(60)


def hexagon2(side):
    for x in range(6):
        t.forward(side)
        t.right(60)


def make_flower_center(side, color_c):
    t.color(color_c)
    t.begin_fill()
    hexagon1(side)
    t.end_fill()


def make_flower_petals(side, color_p):
    t.color(color_p)
    t.begin_fill()
    hexagon2(side)
    t.end_fill()


def main():
    side = legnth_of_hexagon_side()
    color_c = color_of_flowers_center()
    color_p = color_of_flowers_petals()
    make_flower_center(side, color_c)
    for x in range(6):
        t.forward(side)
        t.left(60)
        make_flower_petals(side, color_p)


main()


t.exitonclick()
