def add(*args):
    sum = 0
    for n in args:
        sum+=n
    return sum

print(add(2, 3, 4, 5, 6, 7))

# unlimited keywords arguments
def cal(**kwargs):
    print(kwargs)
    # can use as dictionary
    print(kwargs["add"])

cal(add=3, multi=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        # kw.get() if didn't input will return None

my_car = Car(make="nissan")
print(my_car.model)



