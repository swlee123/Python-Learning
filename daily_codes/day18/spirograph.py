import turtle as t
import random
tim = t.Turtle()
screen = t.Screen()
tim.speed("fastest")
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_spiro(size_of_gap):
    for x in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.left(size_of_gap)

draw_spiro(5)



screen.exitonclick()