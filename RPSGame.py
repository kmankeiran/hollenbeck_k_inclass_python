# import the random package so that we can generate random numbers
from random import randint

# chices is an array => a container that can hold multiple items
# arrays are 0-based -> the first item is 0, the second is 1, etc
choices = ["Rock", "Paper", "Scissors"]
player = False

player_lives = 3
computer_choice_lives = 3

# make the computer choose 1 wepon from the choices array at random
computer_choice = choices[randint(0,2)]

# win or lose function
def winorlose(status):
    print("Called win or lose function")
    print("***************************************")
    print("You", status, "! Would you like to play again?")
    choice = input("Y / N: ")


    #reset the lives
    if choice == "Y" or choice == "y"
        # change global variables
        global player_lives
        global computer_choice_lives
        global player
        global computer

        player_lives = 5
        computer_choice_lives = 5
        player = False
        computer =choices[randint(0, 2)]

    elif choice == "N" or choice == "n"
        print("you chose to quit!")
        print("**************************")
        exit()





# print the choice to the terminal window


# set up our loop
while player is False:
    #set player to True by making a selection
    print("Player lives:", player_lives, "/3")
    print("Computer lives:", computer_choice_lives, "/3")
    print("Choose your weapon!")
    player = input("Rock, Paper or Scissors?\n")

    print("Player chooses", player, "\n")
    print("Computer chooses: ", computer_choice)
    
    # check for a tie = choices are the same
    if player == computer_choice:
        print("Tie! You live to shoot another day")

    # check to see if the computer choice beats our choice or not
    elif player == "Rock":
        if computer_choice == "Paper":
            # computer won. Damn!!
            print("You lose!", computer_choice, "covers", player, "You lose a life")
            player_lives = player_lives - 1
        else:
            # we win! Eat it computer
            print("You win!", player, "smashes", computer_choice, "Computer loses a life")
            computer_choice_lives = computer_choice_lives - 1

    elif player == "Paper":
        if computer_choice == "Scissors":
            print("You lose!", computer_choice, "cut", player, "You lose a life")
            player_lives = player_lives - 1
        else:
            print("You won!", player, "covers", computer_choice, "Computer loses a life")
            computer_choice_lives = computer_choice_lives - 1

    elif player == "Scissors":
        if computer_choice == "Rock":
            print("You lose!", computer_choice, "smashes", player, "You lose a life")
            player_lives = player_lives - 1
        else:
            print("You win!", player, "cut", computer_choice, "Computer loses a life")
            computer_choice_lives = computer_choice_lives - 1
    

    elif player == "quit":
        exit()
    else:
        print("Check your spelling... that's not a valid choice\n")


    #If the player or the computer loses all of their lives, then the game ends
    if (computer_choice_lives < 1):
        winorlose("won")
    
    elif (player_lives < 1):
        winorlose("lose")
    
    
    # reset the game loop and start over again
    player = False
    computer_choice = choices[randint(0, 2)]
    
    # we have to add and take away lives now

