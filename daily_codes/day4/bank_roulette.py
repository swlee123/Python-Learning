import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ") 
# str.split(", ") separate string between", "and make them into list
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
length = len(names) 
#len() gets total number of item in list
rand_int = random.randint(0,length-1)
person = names[rand_int]
print(person+" is going to buy the meal today!")

