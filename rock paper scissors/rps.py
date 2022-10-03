# Quick rock paper scissors game
from random import randint

def menu():
    start = str(input("start game? y/n ")).lower()
    if start == "y":
        game()
        print("Thanks for playing!")
    else:
        pass


def game():
    choices = ["rock", "paper", "scissors"]
    inputs = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    while True:
        computer_choice = choices[randint(0, 2)]
        user_choice = str(
            input("select rock, paper or scissors (quit to stop game): ")
        ).lower()
        if user_choice == "quit":
            return
        elif user_choice in inputs:
            print("I chose {}!".format(computer_choice))
            if computer_choice == inputs[user_choice]:
                print("Nice one! You win! ")
            elif computer_choice == user_choice:
                print("Draw! Try again!")
            else:
                print("Unlucky... You lose!")
        else:
            print("Incorrect choice try again")


if __name__ == "__main__":
    menu()
