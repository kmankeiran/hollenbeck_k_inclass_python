# import the random package so that we can generate random numbers
from random import randint

# chices is an array => a container that can hold multiple items
# arrays are 0-based -> the first item is 0, the second is 1, etc
choices = ["Rock", "Paper", "Scissors"]
player = False

# make the computer choose 1 wepon from the choices array at random
computer_choice = choices[randint(0,2)]

# print the choice to the terminal window
print("Computer chooses: ", computer_choice)

# set up our loop
while player is False:
    #set player yo True by making a selection
    print("Choose your weapon!")
    player = input("Rock, Paper or Scissors?\n")

    print(player, "\n")
    
    # check for a tie = choices are the same
    if player == computer_choice:
        print("Tie! You live to shoot another day")

    # check to see if the computer choice beats our choice or not
    elif player == "Rock":
        if computer_choice == "Paper":
            # computer won. Damn!!
            print("You lose! Paper covers Rock")
        else:
            # we win! Eat it computer
            print("You win!", player, "smashes", computer_choice)

    elif player == "Paper":
        if computer_choice == "Scissors":
            print("You lose!", computer_choice, "cut", player)
        else:
            print("You won!", player, "covers", computer_choice)

    elif player == "Scissors":
        if computer_choice == "Rock":
            print("You lose!", computer_choice, "smashes", player)
        else:
            print("You win!", player, "cut", computer_choice)

    elif player == "quit":
        exit()
    else:
        print("Check your spelling... that's not a valid choice\n")
    
    # reset the game loop and start over again
    player = False
    computer_choice = choices[randint(0, 2)]
    
    # we have to add and take away lives now

