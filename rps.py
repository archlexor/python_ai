import random 

choices = ["rock", "paper", "scissors"]

ai = random.choice(choices)
print("###########################################################################")
print("                         GAME ROCK PAPER SCISSORS                          ")
print("###########################################################################")
print("-------------------------------q to exit-----------------------------------")

while True:
    
    user = input("choose rock, paper or scissors: ").lower()
    if user == "q":
        print("Game over")
        break

    if user not in choices:
        print("Invalid chooice!")
        break

    print(f"you have choosen {user}")
    print(f"computer have choosen {ai}")

    if user == ai:
        print("Draw!")
    elif user == "rock" and ai == "scissors":
        print("you won!")
    elif user == "scissors" and ai == "paper":
        print("you won!")
    elif user == "paper" and ai == "rock":
        print("you won!")
    else:
        print("computer won!")
    
    



