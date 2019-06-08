# game.py

import random

def my_message():
    return "Hello"

def determine_winner(user_choice,computer_choice):
    winners = {
        "rock":{
            "rock": None,   # TIE
            "paper": "paper",
            "scissors": "rock",
        },
        "paper":{
            "rock": "paper",
            "paper": None,  # TIE
            "scissors": "scissors",
        },
        "scissors":{
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,   # TIE
        },
    }
    winning_choice = winners[user_choice][computer_choice]
    return winning_choice

# Only if this scrip t is executed from the command-line
if __name__ == "__main__": 


    print("Rock, Paper, Scissors, SHOOT!")  # this is also a comment

    # 1.Capture Inputs

    user_choice = input("Please choose one of the following options: 'rock', 'paper', or 'scissors' (without the quotes):")

    print("-----------------")
    print("You chose:", user_choice)
    #print("-----------------")


    # 2.VALIDATE INPUTS

    #version 1 of validation
    #if user_choice in ["rock", "paper", "scissors"]:
    #    #print("VALID!")
    #    pass
    #else:
    #    print ("Invalid Selection, Please try this again!")
    #    exit()

    #simplified version of validation

    options = ["rock", "paper", "scissors"]
    if user_choice not in options:
        print ("Invalid Selection, Please try this again!")
        exit()


    # 3.Generate Computer selection

    computer_choice = random.choice(options)

    #override for test
    #user_choice="rock"
    #computer_choice="rock"


    print("-----------------")
    print("Generating...")
    print("Computer chose:", computer_choice)


    # 4.Determine the winer

    # rock beats scissors
    # scissor beats papers
    # paer beats rocks
    # same selection is a tie


    #if user_choice == computer_choice:
    #    print("TIE!")
    #
    #elif user_choice == "rock" and computer_choice == "paper":
    #
    ##complicated way to show winner
    ##    print("Winner is paper")
    ##    print("Computer wins")
    #elif user_choice == "rock" and computer_choice == "scissors":
    #    print("Rock")
    #
    #elif user_choice == "paper" and computer_choice == "rock":
    #    print("paper")
    #elif user_choice == "paper" and computer_choice == "scissors":
    #    print("scissors")
    #
    #elif user_choice == "scissors" and computer_choice == "rock":
    #    print("rock")
    #elif user_choice == "scissors" and computer_choice == "paper":
    #    print("scissors")



    #In-class working version

    # first attribute represents the user, second represents the computer
    winners = {
            "rock":{
                "rock": None,
                "paper": "paper",
                "scissors": "rock",
            },
        "paper":{
                "rock": "paper",
                "paper": None,
                "scissors": "scissors",
            },
        "scissors":{
                "rock": "rock",
                "paper": "scissors",
                "scissors": None,
            },
        }       

    winning_choice = winners[user_choice][computer_choice]

    # 5.DISPLAY FINAL OUTPUTS / OUTCOMES

    if winning_choice:
        if winning_choice == user_choice:
            print("YOU WON")
        elif winning_choice == computer_choice:
            print("YOU LOST")
    else:
        print("TIE")

    print("Thanks for playing. Please play again!")




