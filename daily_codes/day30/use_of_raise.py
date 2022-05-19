height = float(input("Please enter your height:"))
weight = float(input("Please enter your weight:"))

if height>3:
    raise ValueError("Human height should not be over 3m")
bmi = weight/height**2
print(bmi)
