
profit = 0

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "quarters": 0,
    "dimes": 0,
    "nickels": 0,
    "pennies": 0
}




def insert_coin() :
    print("Please insert coins.")
    for coin in coins:
        coins[coin] = int(input(f"How many {coin}?: "))
    sum = coins["quarters"]*0.25+coins["dimes"]*0.1+coins["nickels"]*0.05+coins["pennies"]*0.01
    return sum

def check_bal( bal,  coffee ) :
    if bal >= MENU[coffee]["cost"]:
        print(f"Here is {round(count_change(money, choice), 2)}$ in change.")
        print(f"Here is your {choice} ☕.Enjoy!")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def count_change(bal,coffee):
    change = bal-MENU[coffee]["cost"]
    global profit
    profit += MENU[coffee]["cost"]
    return change

def check_resources(coffee) :
    lack_resources = ""
    enough_resource = True
    cof = MENU[coffee]["ingredients"]
    list1 = ["water", "milk", "coffee"]

    for key in list1:
        if resources[key] < cof[key]:
            lack_resources = key
            enough_resource = False
            break

    if not enough_resource:
        print(f"Sorry there is not enough {lack_resources}")
        return enough_resource
    else :
        return True

def deduce_resource(coffee):

    for key in resources:
        resources[key] -= MENU[coffee]["ingredients"][key]





while True :

    money = 0
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "report":
        print(f"Water: {resources['water'] }ml ")
        print(f"Milk: {resources['milk'] }ml ")
        print(f"Coffee: {resources['coffee']}ml ")
        print(f"Money: {profit}$ ")
        continue
    elif choice in MENU:
        a = check_resources(choice)
        if not a:
            continue
        money = insert_coin()
        enough_bal = check_bal(money, choice)
        if enough_bal == True:
            deduce_resource(choice)
        else :
            money = 0
            continue
    elif choice == "off":
        print("Terminating Machine....\nBye!")
        break









