from turtle import Turtle, Screen

import random

timmy = Turtle()
timmy.shape("turtle")
j = 0
color = ["magenta", "misty rose", "medium purple", "cyan", "medium spring green", "orange", "beige"]
for i in range(3, 10):
    timmy.color(color[j])
    angle = 360/i
    j += 1
    for x in range(i):

        timmy.forward(50)
        timmy.right(angle)

screen = Screen()
screen.exitonclick()