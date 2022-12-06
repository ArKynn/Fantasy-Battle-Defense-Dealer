from Items_and_Inventory import playerinventory
from d10_and_end_game import end_game



day = 1
while True:
    print(" DAY " + str(day) + ":")

    #Resource Buying
    print ("What do you want to do? ")



    #Crafting



    #Selling










    if end_game == True :
        print ("GAME COMPLETED!!!")
        print("You have obtained " + end_game(playerinventory.money))
        break


    print(" DAY " + str(day) + " RESULTS:")
    print()
    day = day + 1
