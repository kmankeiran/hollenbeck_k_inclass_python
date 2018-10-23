# print a message to the terminal wondow
print("Rules that govern the sate of water")

# set up a variable to hold the temperature we input
current_temp = False

while current_temp is False:
	# make this a number and clean the code up (DRY it out)
    current_temp = input("Enter a temperature:\n")
    # see what current temp is
    print("you input:", current_temp)
    
    # if the current temp is at freezing or below, water is a solid
    if (int(current_temp) < 0 or (int(current_temp) == 0)):
        print("water is a solid! cuz it's at or below freezong")
        current_temp = False
    # else check another condition. if it's not freezing, is below boiling?
    elif (int(current_temp) < 100):
        print("Water is a liquid, because it's above freezing and below boiling")
        current_temp = False

    elif (int(current_temp) > 100 or (int(current_temp) == 100)):
        print("Water is a gas. Cuz it's, like, really hot")
        current_temp = False
