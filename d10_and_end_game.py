import Items_and_Inventory
import random

#Dice throw 1-10
def d10throw() -> int:
    return random.randint(1,10)




def end_game():
    if Items_and_Inventory.playerinventory.money >= 10000:
        return True


