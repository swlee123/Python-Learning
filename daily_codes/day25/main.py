#file = open("weather_data.csv", "r")
#data = file.readlines()
#print(data)
#file.close()

#import csv
#file = open("weather_data.csv", "r")
#data = csv.reader(file)
#temperature = []

#for row in data:
   # temp = row[1]
    #if temp != "temp":
      #  temperature.append(int(temp))

#print(temperature)

import pandas
data = pandas.read_csv("weather_data.csv")
# print(type(data))
# this will be pandas data frame
# print(type(data["temp"]))
# this will be a series
# print data in column

#data_dict = data.to_dict()
# convert dataframe to dictionary
#print(data_dict)

#temp_list = data["temp"].to_list()
# convert series to list
#s = sum(temp_list)
#l = len(temp_list)
#average = s/l
#print(average)

# or use build in method of series
#print(data["temp"].mean())
#max = data["temp"].max()
#print(max)


# get data in row
#print(data[data.day == "Monday"])

# get row of data with highest temperature
#max = data["temp"].max()
#print(data[data.temp == max])

# access the monday row and print condition in the row
#monday =data[data.day == "Monday"]
#print(monday.condition)

# get temp of monday and convert to farenheit

#faren = int(monday.temp)*9/5+32
#print(f"{faren}F")

# create dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 67, 89]
}

data = pandas.DataFrame(data_dict)
# convert the dataframe to csv
data.to_csv("new_data.csv")



