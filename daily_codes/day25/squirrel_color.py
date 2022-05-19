import pandas as pd
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color = data["Primary Fur Color"].tolist()

gray = 0
cinnamon = 0
black = 0

for c in color:
    if c == "Gray":
        gray += 1
    elif c == "Black":
        black += 1
    elif c == "Cinnamon":
        cinnamon += 1

data_dict = {
    "Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}

data = pd.DataFrame(data_dict)
data.to_csv("squirrel_primary_color.csv")
