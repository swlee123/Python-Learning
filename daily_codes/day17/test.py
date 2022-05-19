
cock_price = 5
hen_price = 3
chick_price = 1

#def loop_solution():
    #for cock_num in range(0, 20):
        #for hen_num in range(0, 33):
            #chick_num = 100 - cock_num - hen_num
            #if 5*cock_num+3*hen_num+chick_num/3==100:
                #print(f"Cock = {cock_num} Hen = {hen_num} Chick = {chick_num}")

def list_comprehension():
    list1 = []
    for cock_num in range(0, 20):
        for hen_num in range(0, 33):
            chick_num = 100 - cock_num - hen_num
            if 5*cock_num+3*hen_num+chick_num/3==100:
                list1.append(f"Cock = {cock_num},Hen= {hen_num},Chick= {chick_num}")


    return list1



#loop_solution()
list = [x for x in list_comprehension()]
print(list)
