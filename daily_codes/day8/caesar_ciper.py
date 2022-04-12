from art import logo
import os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

restart = True

def re ():
    res = input(("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower())
    if res == "yes":
        os.system("cls")
        return True
    elif res == "no":
        print("Goodbye")
        return False

def caesar(text,shift,direction):
        if shift>26:
            shift = shift%26
        if direction=="decode":
            shift*=-1
        plain_text=""
        for char in text:
            if char not in alphabet:
                plain_text+=char
                continue
            a=alphabet.index(char)
            a+=shift
            plain_text+=alphabet[a]
        print(f"The {direction} text is {plain_text}")
       
    
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

    caesar(text,shift,direction)
    if re()==False:
        break
    
        
    
    

    

        
    
    



