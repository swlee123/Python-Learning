programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
    }

programming_dictionary["Loop"] = "The action of doing something over and over again"
##add something to dictionary
#print(programming_dictionary)

#wipe entire dictionary
#programming_dictionary ={}

#print(programming_dictionary)

#edit an item in dictionary
programming_dictionary["Bug"] = "A moth in your computer"
#print(programming_dictionary["Bug"])

for key in programming_dictionary:
    print(key) #this only print the key 
    print(programming_dictionary[key])

