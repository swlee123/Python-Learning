
from art import logo,vs
from game_data import data
import random
import os

game_continue = True
score = 0



def format(A):
    
    name = A["name"]
    description = A["description"]
    country = A["country"]
    return f"{name},a {description}, from {country}" 
    
def check_ans(ans,other):
    if ans['follower_count']>other['follower_count']:
        return True
    else :
        return False   
    
def check_empty(dict):
    if len(dict)==0:
        return random.choice(data)
    else:
        return dict
    
    
    
A = {
    
    }
B = {
}
        
while game_continue:
    
    
        
    print(logo)
    
    if score> 0:
        print(f"You are right! Current Score : {score}.")
        
        
    A = check_empty(A)
    B = check_empty(B)
    
    print("Compare A:" + format(A))
    print(vs)
    print("Compare B:" + format(B))
    
    ans  = {
        
    }
    other = {
        
    }
    
    if input("Who has more followers? Type 'A' or 'B': ").upper()=='A':
        ans = A
        other =B
    else:
        ans = B
        other =  A
        
    
    game_continue = check_ans(ans,other)
    os.system("cls")
    print(logo)
    if game_continue:
        score+=1
        A = ans
        B = {}
    else :
        print(f"Sorry,that's wrong.Final Score : {score}.")
        

    
        
    
    
    
    
    
    
    
    
    
    
    
    
