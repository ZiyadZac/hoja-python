#QUESTION 1: Alice has some cards with numbers written on them. 
# She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. 
# She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. 
# Write a function to help Bob locate the card.
def locate_card(cards, query):
    cards=sorted(cards)
    cards=cards[::-1]
    position=cards.index(query)
    guess=len(cards)//2
    if guess==position:
        print('computer quessed,position is',guess+1)
    
    higher=len(cards)-1
    attempt=1
    while guess!=position:
        print("Computer turned over",guess+1,"position card.Number was",cards[guess])
        if query>cards[guess]:
         guess-=1
        elif query<cards[guess]:
         guess+=1
        attempt+=1
    print("Computer turned over",guess+1,"position card.Number was",cards[guess])  
    print('wins in',attempt,'attemps')

# Optional test helper if a test module is available:
from test import evaluate_test_case





