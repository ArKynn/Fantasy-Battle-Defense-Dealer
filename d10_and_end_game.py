from Items and Inventory.py import playerinventory
import random

#Dice throw 1-10
def d10throw() -> int:
    return random.randint(1,10)




def end_game (current_money) -> bool:
    current_money = playerinventory.money
    if current_money == 100000:
        return current_money


