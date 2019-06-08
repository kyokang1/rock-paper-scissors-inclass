# game.py

# import
import random

# test code for pytest 1 - exmaple
def my_example():
    return True

# test code for pytest 2 - message
def my_message():
    return "Hello"

# test code for pytest 3 - determine winner
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


    # ================================================================ #
    # 0.Starting
    print("Rock, Paper, Scissors, SHOOT!")  # this is also a comment


    # ================================================================ #
    # 1.Capture Inputs

    user_choice = input("Please choose one of the following options: 'rock', 'paper', or 'scissors' (without the quotes):")

    print("-----------------")
    print("You chose:", user_choice)
    #print("-----------------")


    # ================================================================ #
    # 2.VALIDATE INPUTS

    # Validation version 1
    #if user_choice in ["rock", "paper", "scissors"]:
    #    #print("VALID!")
    #    pass
    #else:
    #    print ("Invalid Selection, Please try this again!")
    #    exit()

    # Validation version 2 - simplified version
    options = ["rock", "paper", "scissors"]
    if user_choice not in options:
        print ("Invalid Selection, Please try this again!")
        exit()


    # ================================================================ #
    # 3.Generate Computer selection

    computer_choice = random.choice(options)

    #override for test
    #user_choice="rock"
    #computer_choice="rock"

    print("-----------------")
    print("Generating...")
    print("Computer chose:", computer_choice)


    # ================================================================ #
    # 4.Determine the winer

    # Logic Planing
    # - rock beats scissors
    # - scissor beats papers
    # - paer beats rocks
    # - same selection is a tie

    # Version 1 - Inclass Unfined Version
    #if user_choice == computer_choice:
    #    print("TIE!")
    #
    #elif user_choice == "rock" and computer_choice == "paper":
    #    print("Winner is paper")
    #    print("Computer wins")
    #elif user_choice == "rock" and computer_choice == "scissors":
    #    print("Winner is rock")
    #    print("You win")
    #elif user_choice == "paper" and computer_choice == "rock":
    #    print("Winner is paper")
    #    print("You win")
    #elif user_choice == "paper" and computer_choice == "scissors":
    #    print("Winner is scissors")
    #    print("Computer wins")
    #elif user_choice == "scissors" and computer_choice == "rock":
    #    print("Winner is rock")
    #    print("Computer wins")
    #elif user_choice == "scissors" and computer_choice == "paper":
    #    print("Winner is scissors")
    #    print("You win")

    # Version 2 - Alternative way
    if user_choice == computer_choice:
        winning_choice = None   # result = tie
    else: 
        choices = [user_choice, computer_choice]    # choices: order does not matter
        choices.sort()  # .sort() arrays the choices in ascending order in alphabet. rock -> paper -> scissors

        # works
        if choices == ["paper", "rock"]:
            winning_choice = "paper"
        elif choices == ["paper", "scissors"]:
            winning_choice = "scissors"
        elif choices == ["scissors", "rock"]:
            winning_choice = "rock"

        # does not work
        #if choices == ["paper", "rock"]:
        #    winning_choice = "paper"
        #elif choices == ["scissors", "paper"]:  # if "scissors" comes first, this does not work. Logically, it is right.
        #    winning_choice = "scissors"
        #elif choices == ["rock", "scissors"]:
        #    winning_choice = "rock"

    # Version 3 - Define winning choice with dictionary 
    # first attribute represents the user, second represents the computer
    #winners = {
    #        "rock":{
    #            "rock": None,
    #            "paper": "paper",
    #            "scissors": "rock",
    #        },
    #    "paper":{
    #            "rock": "paper",
    #            "paper": None,
    #            "scissors": "scissors",
    #        },
    #    "scissors":{
    #            "rock": "rock",
    #            "paper": "scissors",
    #            "scissors": None,
    #        },
    #    }       
    #winning_choice = winners[user_choice][computer_choice]


    # ================================================================ #
    # 5.DISPLAY FINAL OUTPUTS / OUTCOMES

    # For Vesrion 2&3
    if winning_choice:
        if winning_choice == user_choice:
            print("YOU WON")
        elif winning_choice == computer_choice:
            print("YOU LOST")
    else:
        print("TIE")


    # ================================================================ #
    # 6.Closing

    print("Thanks for playing. Please play again!")
