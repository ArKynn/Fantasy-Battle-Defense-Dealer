import Items_and_Inventory, d10_and_end_game

def buy_materials(input):

    if input in Items_and_Inventory.allmaterials:
        if Items_and_Inventory.playerinventory.money >= input.value:
            Items_and_Inventory.playerinventory.money += -input.value
            input.count += 1
            return True
        else:
            return False
    
def craftattempt(craftitem):
    
    craftquality = Items_and_Inventory.playerinventory.craftexp * d10_and_end_game.d10throw() /10
    Items_and_Inventory.playerinventory.craftexp += craftitem.value
    if craftquality >= craftitem.min_quality:
        craftitem.count += 1

def sell(input, playerinventory):
    
    if input.count >= 1:
        input.count += -1
        playerinventory += input.value
        return True
    return False