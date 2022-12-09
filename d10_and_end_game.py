import Items_and_Inventory
import random

#function for a random dice throw between 1-10
def d10throw() -> int:
    return random.randint(1,10)



#function that evaluates if player money has reached a certain value 
def end_game():
    if Items_and_Inventory.playerinventory.money >= 10000:
        return True


