
your_score =0
symbol = ['A','J','Q','K']
your_cards = ['A',4]
sm = {
    'A':1
}


for x in your_cards:
    if x not in symbol:
        your_score += x
    else :
        your_score+= sm[x]
            
print(your_score)        