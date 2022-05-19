file_1 = open("file1.txt", "r")
file_2 = open("file2.txt", "r")

x = file_1.readlines()
y = file_2.readlines()

result = [int(ans) for ans in x if (ans in y)]

print(result)

file_1.close()
file_2.close()