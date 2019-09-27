# By Kwame Boamah

import math

# Question 1


def make_shape():
    print("   _______")
    print(" /         \\")
    print("/           \\")
    print("\\           /")
    print(" \\ _______ /")


def make_line():
    print("_\"_\'_\"_\'_\"_")


def top_half_shape():
    print("   _______")
    print(" /         \\")
    print("/           \\")


def bottom_half_shape():
    print("\\           /")
    print(" \\ _______ /")


for x in range(2):
    make_shape()
    make_line()

bottom_half_shape()
top_half_shape()
make_line()
bottom_half_shape()

print()

# Question 2


def happy_birthday_song(name):
    for z in range(2):
        print("Happy Birthday to you!")
    print("Happy Birthday dear", name)
    print("Happy Birthday to you!")


happy_birthday_song("Kwame")

print()

# Question 3 and 4


def total(num1, num2):
    return num1 + num2


def main():
    number1 = float(input("Whats your favorite number?"))
    number2 = float(input("What is your least favorite number"))
    answer = total(number1, number2)
    print("The sum of your favorite number,", number1, ",and your least favorite number", number2,
          "is", answer)


main()

print()

# Question 5


def area_of_triangle(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def main():
    a = float(input("What is the length of the first side?"))
    b = float(input("What is the length of the second side?"))
    c = float(input("What is the length of the third side?"))
    print("The area of the triangle is", area_of_triangle(a, b, c))


main()

print()
