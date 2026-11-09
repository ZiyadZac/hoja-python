import random as rnd
num=rnd.randint(1,1000)
#print(num)
x=0
guess=0
while x!=num:
    x=int(input('Guess the number '))
    if x<num:
        print('Guess higher')
    
    elif x>num:
        print('Guess lower')
    guess+=1
    
print('You won <3')
print('Number of attemps-->',guess)