from turtle import Turtle
import time

class Ball (Turtle):

    def __init__(self):
        super().__init__()
        self.speed(1)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_x = 10
        self.move_y = 10
        self.sleep_time = 0.13

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        time.sleep(self.sleep_time)
        self.goto(new_x, new_y)

    def bounce_vertical(self):
        self.move_y *= -1

    def bounce_horizontal(self):
        self.move_x *= -1

    def refresh(self):
        self.goto(0, 0)
        self.sleep_time = 0.13
        self.bounce_horizontal()

    def accelerate(self):
        self.sleep_time -= 0.01










