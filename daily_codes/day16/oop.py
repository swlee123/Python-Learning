#from turtle import Turtle,Screen

#timmy = Turtle()
#print(timmy)
#timmy.shape("turtle")
#timmy.color("coral")
#timmy.forward(100)
#myscreen = Screen()
#print(myscreen.canvheight)


#attribute associated to screen

#myscreen.exitonclick()

from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes
from prettytable import MSWORD_FRIENDLY

table = PrettyTable()

table.add_column("Pokemon Name",[ "Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align["Pokemon Name"] = "l"
table.align["Type"] = "l"

table.set_style(MSWORD_FRIENDLY)

print(table)