import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")

states = data["state"].tolist()
x_coordinate = data["x"].tolist()
y_coordinate = data["y"].tolist()
guessed_states = []
revision_sheet = []

def show_name(index):

    a = turtle.Turtle()
    a.penup()
    a.ht()
    state_name = states[index]
    a.goto(x_coordinate[index], y_coordinate[index])
    a.write(arg=state_name, move=False, align="center", font=("Times New Romans", 10, "normal"))


correct = 0

while len(guessed_states) < 50:
    answer_states = screen.textinput(title=f"Guess the states: {correct}/50",
                                     prompt="What's another state's name?").title()
    # check whether the answer is correct
    if answer_states in states:

        num = states.index(answer_states)
        show_name(num)
        correct += 1
        guessed_states.append(answer_states)
    # if want to exit
    elif answer_states == "Exit":
        # create a revision sheet for learning
        # changed to list comprehensions
        revision_sheet = [state for state in states if state not in guessed_states]
        revision = pd.DataFrame(revision_sheet)
        revision.to_csv("revision_sheet.csv")
        break

screen.exitonclick()
