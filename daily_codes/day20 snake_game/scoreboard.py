from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.goto(-50, 265)
        self.color("white")

    def Printscore(self):
        self.clear()
        self.write(f"Score :{self.score}High Score ：{self.high_score}", move=False, align='left', font=('Courier', 15, 'normal'))

    #def gameover(self):
        #self.goto(0, 0)
        #self.write("Game Over", move=False, align='center', font=('Courier', 22, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.Printscore()

