import turtle
import math


window = turtle.Screen()
window.title("computer_graphics_1 - DSEA")
turtle.pensize(1.5)
turtle.speed(1.5)


def make_triangle(side, forward_length):
    turtle.forward(forward_length)
    side(120)
    turtle.forward(forward_length)
    side(120)
    turtle.forward(forward_length)


def make_changes(forward_length, color, side, direction):
    turtle.penup()
    turtle.forward(forward_length)
    turtle.down()
    turtle.color(color)
    side(direction)


make_triangle(turtle.left, 200)  # 1 
make_changes(50, "red", turtle.left, math.pi / 6)

make_triangle(turtle.left, 200)  # 2
make_changes(50, "green", turtle.left, 60)

make_triangle(turtle.right, 200)  # 3
turtle.penup()
turtle.color("blue")
turtle.left(60)
turtle.forward(25)
turtle.left(90)
turtle.forward(225)
turtle.down()
turtle.left(150)

make_triangle(turtle.left, 66)  # 4

window.exitonclick()
