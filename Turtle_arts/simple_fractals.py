from turtle import *
import turtle

speed(0)
tracer(5)

right(-90)

angle = 30


def yaxis(size, lvl):
    if lvl > 0:
        colormode(255)

        pencolor(0, 255 // lvl, 0)

        forward(size)

        right(angle)

        yaxis(0.8 * size, lvl - 1)

        pencolor(0, 255 // lvl, 0)

        lt(2 * angle)

        yaxis(0.8 * size, lvl - 1)

        pencolor(0, 255 // lvl, 0)

        right(angle)
        forward(-size)


for i in range(0, 4):
    home()
    setheading(0)
    rt(90 * i)
    yaxis(80, 7)



turtle.done()