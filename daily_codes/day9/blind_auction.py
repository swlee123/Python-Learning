import os
from art import logo

print(logo)
print("Welcome to the secret auction program.")

contestants = {}

def add_contestant(name,bid):
    contestants[name] = bid
    
def ask_end():
    end = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if end == "yes":
        return True
    elif end == "no":
        return False
    
    
while True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    
    add_contestant(name,bid)
    
    if not ask_end():
        break
    else:
        os.system("cls")

winner = ""
bid = 0  

for bidders in contestants:
    if contestants[bidders]>bid:
        winner = bidders
        bid = contestants[bidders]

print(f"The winner is {winner} with a bid of ${bid}")


    
    
        
    
    
    
    