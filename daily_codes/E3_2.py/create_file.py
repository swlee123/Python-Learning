f = open("demo.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demo.txt", "r")
print(f.read())

# "a" - Append - will append to the end of the file
#
# "w" - Write - will overwrite any existing content

f = open("demo.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demo.txt", "r")
print(f.read())

# "x" - Create - will create a file, returns an error if the file exist

# "a" - Append - will create a file if the specified file does not exist

# "w" - Write - will create a file if the specified file does not exist