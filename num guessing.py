import random
def game():
    num=random.randint(1,3)
    for i in range(3):
        rem=3-i
        print(f"you have {rem} rounds to guess it correctly")
        guess=int(input("guess your number between 1-3: "))
        if(guess<1 or guess>3):
            print("invalid number! Disqualified!")
            break
        if(guess==num):
            print(f"the guess was correct! the number was {num}")
            break
        else:
            print("try again!")
        
    print("Game Over!")  


game()