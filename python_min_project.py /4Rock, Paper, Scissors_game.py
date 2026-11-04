import random as rnd
cho=["rock",'paper','scissor']

def get_computer_choice():
    comp=rnd.choice(["rock",'paper','scissor'])
    return comp

def get_player_choice():
    player=input('Rock OR Paper OR Scissor:' ).lower()
    return player

def check_winner():
    p=get_player_choice()
    c=get_computer_choice()
    print(c)
    if c==p:
        return "Draw"
    elif c=="rock":
        if p=="paper":
            return "player wins"
        else:
            return "computer wins"
    elif c=="paper":
            if p=="scissor":
                return "player wins"
            else:
                return "computer wins"
    elif c=="scissor":
            if p=="rock":
                return "player wins"
            else:
                return "computer wins"

 
print(check_winner())