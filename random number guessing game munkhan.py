import random
invitation=print("welcome to random number guessing game")

count=0
def game():
    global count #declare count as a global variable in function
    level=input("enter the level of game(easy,difficult or medium)")
    if level.lower()=="easy":
        x=random.randint(1,10)
    elif level.lower()=="medium":
        x=random.randint(1,100)
    elif level.lower()=="difficult":
        x=random.randint(1,1000)
    else:
        breakpoint
    for i in range(10):
        num=int(input("guess a number"))
        if num<x:
            print("too low,think again you have",10-(i+1),"remaining chances")
        elif num>x:
            print("too high,think again you have",10-(i+1),"remaining chances")
        elif num==x:
            print("congratulations! you guessed correct number in",i+1,"chances")
            count+=1
            break
        if i==10:
            print("SORRY: you donot have lost all your chances")
            break
game()
ask=input("do you want to play again(yes/no)")
while ask.lower()=="yes":
    game()
    ask=input("do you want to play again(yes/no)")
print("you total score is",count)






