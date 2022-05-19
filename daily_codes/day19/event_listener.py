from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)
screen.listen()
screen.onkey(key="space", fun=move_forwards)

## no need parenthesis for the fun function
screen.exitonclick()