from art import logo
import random 

print(logo)
print("Welcome To The Number Guessing Game!")
print("I'm thinking of number between 1 and 100")
ans = random.randint(1,100)
print(f"Correct ans: {ans}")#for testing purpose ,will dlt later

def difficulty():
    level = input("Choose a difficulty.Type 'easy' or 'hard' : ")
    return level

def easy_level():
    chances = 10

    while chances:
        
        print(f"You have {chances} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == ans:
            print(f"You got it! The answer was {ans}")
            return 0
        elif guess>ans:
            print("Too high.\nGuess again")
        else :
            print("Too low.\nGuess again")
        chances-=1
    
    print("You've run out of guesses, you lose.")
    return 0

def hard_level():
    
    chances = 5
    while chances:
        
        print(f"You have {chances} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == ans:
            print(f"You got it! The answer was {ans}")
            return 0
        elif guess>ans:
            print("Too high.\nGuess again")
        else :
            print("Too low.\nGuess again")
        chances-=1
    
    print("You've run out of guesses, you lose.")
    return 0
    
    
level = difficulty()

if level=='easy':
    easy_level()
elif level == 'hard':
    hard_level()
    
    



