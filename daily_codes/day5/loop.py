# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum = 0
count = 0
# actually can use sum() and len() but this question asked to use loop
for height in student_heights :
    sum+=height
    count= count+1

average = round(sum/count)
print(average)
    