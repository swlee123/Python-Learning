import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)
screen = turtle.Screen()
color = ["magenta", "misty rose", "medium purple", "cyan", "medium spring green", "orange", "yellow"]
tim.width(10)
tim.speed(8)
direction = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

for x in range(70):
    tim.color(random_color())
    direc = random.choice(direction)
    tim.setheading(direc)
    tim.forward(20)

screen.exitonclick()

