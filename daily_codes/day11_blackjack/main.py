############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

from ctypes import sizeof
from art import logo
import os
import random

def check_bj(your_score, computer_score):
    if (computer_score or your_score)==21 or your_score>21:
        return True
    
def final(your_cards, your_score, computer, computer_score):
    print(f"\tYour final hands: {your_cards}, final score = {your_score}")
    print(f"\tComputer's final hand:{computer}, final score = {computer_score} ")
    if (computer_score==21 and your_score !=21) or (computer_score<=21 and computer_score>your_score) or your_score>21:
        print(f"You lose! \U0001F643")
    elif your_score == computer_score and computer_score!=21:
        print(f"It's a draw! \U0001F923	")
    elif your_score>computer_score or (computer_score>21 and your_score<22) :
        print(f"You win! \U0001F604")
        
    print("\n")
    
def add(deck):
    score =0 
    lenght = len(deck)
    if lenght ==2 :
        for x in deck :
            if x not in symbol :
                score+=x
            else :
                score+=two_cards[x]
    else :
        for x in deck :
            if x not in symbol :
                score+=x
            else :
                score+=more_cards[x]
                
    return score     


while input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ").lower() == 'y':
    cards = ['A','A','A','A',2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,
             'J','J','J','J','Q','Q','Q','Q','K','K','K','K']
    
    symbol = ['A','J','Q','K']
    
    two_cards = {
        'J':10,
        'Q':10,
        'K':10,
        'A':11
    }
    
    more_cards = {
        'J':10,
        'Q':10,
        'K':10,
        'A':1
    }
    
    def draw_two(player):
        for num in range(2):
            a =random.choice(cards)
            cards.remove(a)
            player.append(a)
    
    
    def ask_draw(your_score):
        ask = input("Type 'y' to get another card, type 'n' to pass: ")
        if ask == 'y':
            a= random.choice(cards)
            your_cards.append(a) 
            cards.remove(a)
            your_score = add(your_cards)
            return False
        else:
            return True
        
    player_continue = True
    
    os.system("cls")
    print(logo)
    your_cards = []
    computer = []
    your_score = 0
    computer_score = 0
    
    def show_score():
        print(f"\n\tYour cards: {your_cards}, current score = {your_score}")
        print(f"\tComputer's first card:{computer[0]}\n\n ")

    draw_two(your_cards)
    draw_two(computer)
    print(f"comp {computer}")
        
    while player_continue:
        
        if symbol not in your_cards and computer:
            your_score = add(your_cards)
            computer_score = add(computer)
        else :
            add(your_cards)
        
        show_score()
        
        if check_bj(your_score,computer_score):
            break
        
        if ask_draw(your_score):
            break
        
    while (computer_score<16):
        computer.append(random.choice(cards))
        computer_score = add(computer)
        
    final(your_cards, your_score, computer, computer_score)
        
        
            
        
        
        

    
