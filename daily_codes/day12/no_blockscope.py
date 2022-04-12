game_level = 2
enemies = ["Skeleton","Zombie","Alien"]

if game_level<5:
    new_enemy = enemies[0]
    #inside if is still consider as global scope
    
def create_enemy():
    if game_level<5:
        new1_enemy = enemies[0]
    #inside if is still consider as global scope
    
    
print(new_enemy)
# print(new1_enemy) # error cuz inside funstion scope