import colorgram
import random
import turtle as t


#rgb = []

#color = colorgram.extract('spot.jpg', 30)

#for x in color:
    #r = x.rgb.r
    #g = x.rgb.g
    #b = x.rgb.b
    #new_color = (r, g, b)
    #rgb.append(new_color)

#print(rgb)
color = [ (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157),
  (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31),
  (60,14, 8),
  (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232),
  (11,227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243),
 (3, 67, 40)]


tim = t.Turtle()
tim.hideturtle()
screen = t.Screen()
tim.speed("fastest")
tim.penup()
tim.sety(-300)
t.colormode(255)

for y in range(10):
    tim.sety(tim.ycor()+50)
    tim.setx(-300)
    for x in range(10):

        tim.color(random.choice(color))
        tim.dot(20)

        tim.forward(50)




screen.exitonclick()

