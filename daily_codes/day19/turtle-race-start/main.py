from turtle import Turtle, Screen
import random

is_race_on = False


colors =["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?Enter a color:")
screen.setup(width=500, height=400)

contestants = []

for x in range(0, 6):
    y = Turtle(shape = "turtle")
    y.penup()
    y.color(colors[x])
    y.goto(x=-230, y=-100+x*30)
    contestants.append(y)

if user_bet:
    is_race_on = True
first = ""
while is_race_on:
    for turtle in contestants:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() >= 230:
            first = turtle.pencolor()
            is_race_on = False



print(f"You chose {user_bet},{first} is the winning color!")

if user_bet == first:
    print("You won!")
else:
    print("You lost!")












screen.exitonclick()