import random
gamerule={1:"rock" , 2:"paper" , 3:"scissors"}
print(gamerule)

computer=random.randint(1,3)
computer_gamerule=gamerule[computer]
player=int(input("enter number: "))
player_gamerule=gamerule[player]
if(player<1 and player>3):
    print("Game over, wrong number")
if(player==computer):
    print("draw! try again")
    print(f"you chose {player_gamerule} and computer chose {computer_gamerule}")
else:
    if(player==1 and computer==2):
        print("you lose")
    elif(player==1 and computer==3):
        print("you win")
    elif(player==2 and computer==3):
        print("you lose")
    elif(player==3 and computer==2):
        print("you win")
    elif(player==3 and computer==1):
        print("you lose")
    print(f"you chose {player_gamerule} and computer chose {computer_gamerule}")