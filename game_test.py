# game_test.py

from game import my_example, my_message, determine_winner     #determine_winner

# pytest 1 - example
def test_my_example():
    assert 3 == 3

# pytest 2 - message
def test_my_message():
    #with variable
    x = my_message()
    print(x)
    assert x == "Hello"#
    #without variable
    assert my_message() == "Hello"

# pytest 3 - determine winner
def test_determine_winner():
  
#    assert determine_winner("rock","scissors") == "rock" # for testing

    assert determine_winner("rock", "rock") == None # represents a tie
    assert determine_winner("rock", "paper") == "paper"
    assert determine_winner("rock", "scissors") == "rock"

    assert determine_winner("paper", "rock") == "paper"
    assert determine_winner("paper", "paper") == None # represents a tie
    assert determine_winner("paper", "scissors") == "scissors"

    assert determine_winner("scissors", "rock") == "rock"
    assert determine_winner("scissors", "paper") == "scissors"
    assert determine_winner("scissors", "scissors") == None # represents a tie
