#Step 2

import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
end_of_game = False
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display=[]
for x in chosen_word:
    display.append("_")
print(display)

flag = True


lifes = 6

def check():
    
    for x in display:
        if x=="_":
            flag =False
    
    return flag
            
    

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    if guess not in chosen_word:
        lifes-=1
        print(stages[lifes])
        if lifes==0:
            end_of_game =True
            print("You lose")
    
 
    for x in range(0,len(chosen_word)):
        if chosen_word[x] == guess:
            display[x] = guess
            
    if "_"not in display:
        end_of_game = True
        print("You won!")

    

    

    

