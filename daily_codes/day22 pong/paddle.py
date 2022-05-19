from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.shape("square")
        self.width(20)
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(x, y)
        self.color("white")
        self.penup()

    def up(self):
        self.y += 20
        self.goto(self.x, self.y)

    def down(self):
        self.y -= 20
        self.goto(self.x, self.y)


