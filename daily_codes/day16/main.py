from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import time

a = Menu()
b = CoffeeMaker()
c = MoneyMachine()

while True:

    choice = input(f"What would you like?({a.get_items()}):")
    if choice == "report":
        b.report()
        c.report()
        continue
    elif choice == "off":
        print("Terminating Machine.....")
        for x in range(1,4):
            time.sleep(1)
            print("......")
        print("Closed !")
        break
    else:
        for item in a.menu:
            if choice == item.name:
                if b.is_resource_sufficient(item):
                    enough_money = c.make_payment(item.cost)
                    if enough_money:
                        b.make_coffee(item)










