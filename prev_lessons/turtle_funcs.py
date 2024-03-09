from turtle import *
from random import randint, choice
choice([1,2,3])
def sky(col):
    speed(0)
    color(col)
    pu(); goto(-700, 250); pd()
    width(310)
    fd(1400)

# def star("параметри функції"):
def stars(repeats):
    width(1)
    for c in range(repeats):
        x = randint(-500, 250)
        y = randint(180, 500)
        pu(); goto(x, y); pd()
        color("yellow")
        begin_fill()
        speed(0)
        for z in range(5):
            fd(35)
            rt(144)
        end_fill()


def moon():
    ht()
    speed(0)
    color("yellow")
    width(1)
    pu(); goto(330, 200); pd()
    begin_fill()
    for z in range(22):
        lt(10)
        fd(15)
    lt(140)
    for z in range(22):
        rt(5)
        fd(8)
    end_fill()
