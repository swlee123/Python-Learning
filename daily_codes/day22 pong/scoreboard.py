from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.ht()
        self.setposition(0, 250)
        self.add_score()

    def add_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"Left_Score = {self.l_score} ", align="center", font=("Arial", 10, 'normal'))
        self.goto(100, 200)
        self.write(f"Right_Score = {self.r_score}", align="center", font=("Arial", 10, 'normal'))
