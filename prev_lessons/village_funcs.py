from turtle import *


def derevo():
    color("brown")
    width(17)
    left(90)
    fd(150)
    lenght = 10
    for i in range(26):
        width(10)
        color("Green")
        fd(lenght)
        lenght += 5
        left(90)
    penup()
    fd(150)
    lt(90)
    pendown()


def sad():
    speed(0)
    for x, y in ((-200, 50), (-100, -50), (0, 50), (100, -50), (200, 50)):
        penup(); goto(x, y); pendown()
        derevo()



def triangle(side, col):
    color(col)
    for z in range(3):
        fd(side)
        lt(120)


def square(side, col):
    color(col)
    for z in range(4):
        fd(side)
        rt(90)


def house(col1, col2):
    triangle(100, col1)
    square(100, col2)

