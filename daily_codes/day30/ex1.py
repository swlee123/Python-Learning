fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")

try:
    make_pie(2)
except IndexError:
    print("An index error occurred!")
    print("Fruit Pie")


