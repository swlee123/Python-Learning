import random


test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def r_p_s(i):
    print(image[i])

n=1

while n>0:
    choice = int(input("What do you choose?Type 0 for rock, 1 for paper or 2 for scissors."))

    image = [rock,paper,scissors]

    if choice>2:
        print("Invalid number,you lose!\nTry again!")
        continue
    
    r_p_s(choice)

    comp = random.randint(0,2)
    
    print("Computer choose: ")

    r_p_s(comp)

    if(choice==comp):
        print("Its a draw!\n")
    elif((choice==comp+1)or(choice==comp-2)):
        print("You win!\n")
    else:
        print("You lose!\n")
    
        
    n = int(input("Press 1 to play again or 0 to exit."))







