
# 这个是中学学的 2!,4! 这样的东西，用递归(recursion)计算，可以试看在纸上try算一下，factorial(3)
def factorial(x):
    if x > 1:
        return x * factorial(x - 1)
    else:
        return x

def calculate(x):
    total = 1.0
    term = 1.0
    val = 1.0
    # 重复计算然后加入total,直到 value的 绝对值小于10^-10
    while abs(val) > 10**(-10):
        val = x**term / factorial(term)
        total += val
        term += 1
    return total


while True:
    num = input("Please enter a number.... ")
    if num == "":
        print("bye......")
        break
    else:
        ans = calculate(float(num))
        print(f"e**{num} = {ans}")





