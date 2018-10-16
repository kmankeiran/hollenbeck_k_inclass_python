# import the random package so that we can generate random numbers
from random import randint

# chices is an array => a container that can hold multiple items
# arrays are 0-based -> the first item is 0, the second is 1, etc
choices = ["Rock", "Paper", "Scissors"]

# make the computer choose 1a wepon from the choices array at random
computer_choice = choices[randint(0,2)]

# print the choice to the terminal window
print("Computer chooses: ", computer_choice)