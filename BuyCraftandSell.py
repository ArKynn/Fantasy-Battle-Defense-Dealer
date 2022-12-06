import Items_and_Inventory
def buy_materials(input):

    if input in Items_and_Inventory.allmaterials:
        if Items_and_Inventory.playerinventory.money >= input.value:
            Items_and_Inventory.playerinventory.money += -input.value
            input.count += 1
            return True
        else:
            return False        
    raise Exception("Input is not of the same type as material or does not exist.")
    
def craftattempt(craftexp, d10):

    craftquality = craftexp * d10
    return craftquality

def craft(materialinventory, allrecipes, equipmentinventory, input):
    
    if input in allrecipes:
        pass
    else:
        raise Exception("Input is not of the same type as equipment or does not exist.")

def sell(input, playerinventory):
    if input.count >= 1:
        input.count += -1
        playerinventory += input.value
        return True
    return False