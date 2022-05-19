f = open("demo.txt")
# to open file lah

# print(f.read())
# read entire file

# print(f.read(5))
# read five characters

# print(f.readline())
# read one line only

for x in f:
    print(x)

# print each lines

f.close()