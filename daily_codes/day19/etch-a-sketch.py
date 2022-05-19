import turtle as t

tim = t.Turtle()
screen = t.Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.forward(10)

def turn_left():
    tim.setheading(tim.heading()+90)

def turn_right():
    tim.setheading(tim.heading()-90)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkeypress(move_forwards, "w")
screen.onkeypress(move_backwards, "s")
screen.onkeypress(turn_right, "d")
screen.onkeypress(turn_left, "a")
screen.onkeypress(clear_screen, "c")

screen.exitonclick()
