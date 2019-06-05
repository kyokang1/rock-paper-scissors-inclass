# game.py

print("Rock, Paper, Scissors, SHOOT!")  # this is also a comment

# 1.Capture Inputs

user_choice = input("Please choose one of the following options: 'rock', 'paper', or 'scissors' (without the quotes):")

print("------------")
print("You chose:", user_choice)
#print("------------")


# 2.VALIDATE INPUTS

#version 1 of validation
#if user_choice in ["rock", "paper", "scissors"]:
#    #print("VALID!")
#    pass
#else:
#    print ("Invalid Selection, Please try this again!")
#    exit()

#simplified version of validation
if user_choice not in ["rock", "paper", "scissors"]:
    print ("Invalid Selection, Please try this again!")
    exit()



# Generate COmputer selection



print("Generating...")

# Determine the winer



# Display final outputs/outcomes



