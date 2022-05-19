from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.tracer(0)


game_is_on = True

while game_is_on:
    # detect collision with top and btm
    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce_vertical()

    # detect leaving at left or right
    if ball.xcor() > 400:
        ball.refresh()
        scoreboard.l_score += 1
        scoreboard.add_score()

    elif ball.xcor() < -400:
        ball.refresh()
        scoreboard.r_score += 1
        scoreboard.add_score()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_horizontal()
        ball.accelerate()

    screen.update()
    ball.move()

screen.exitonclick()