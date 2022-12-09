def exitgamecheck(): #If ESC is pressed, shutsdown program
    global mouse1
    for event in pygame.event.get(eventtype=KEYDOWN):
        if event.key==pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

#Checks for mouse position, lights up button in red and checks if mouse is clicked
def checkmousestate(button):
    global mouse1
    if button.collidepoint(pygame.mouse.get_pos()):  #Based on answer by skrx on StackOverfow (https://stackoverflow.com/questions/44998943/how-to-check-if-the-mouse-is-clicked-in-a-certain-area-pygame)
        pygame.draw.rect(display, 'red', button, 1)
        for event in pygame.event.get(eventtype=MOUSEBUTTONDOWN):
            if event.button == 1:
                return True

def starting(): #Starting screen, renders a simple starting button
    global daynum

    startarea = pygame.Rect(displayx/2 - 100, displayy/2 - 25, 250, 75)

    starting = True
    while starting == True:
        exitgamecheck()
        display.fill('black')

        display.blit(font.render("Start?", True, 'white'), [displayx / 2, displayy / 2])
        pygame.draw.rect(display, 'white', startarea, 1)
    
        if checkmousestate(startarea) == True:
            starting = False
            daynum = 1
            
        pygame.display.flip()
        clock.tick(60)

def buymenu(): #Buymenu screen

    #these are the areas where the different buttons will be located
    woodarea = pygame.Rect(300, displayy/2 - 200, 250, 75)
    stringarea = pygame.Rect(woodarea[0], woodarea[1] +100, 250, 75)
    leatherarea = pygame.Rect(woodarea[0], woodarea[1] +200, 250, 75)
    ironarea = pygame.Rect(woodarea[0], woodarea[1] +300, 250, 75)
    goldarea = pygame.Rect(woodarea[0], woodarea[1] +400, 250, 75)
    precisousarea = pygame.Rect(woodarea[0], woodarea[1] +500, 250, 75)
    materialareas = (woodarea, stringarea, leatherarea, ironarea, goldarea, precisousarea)
    recipegachaarea = pygame.Rect(displayx/2, displayy/2 + 100, 250, 75)
    gotocrafingarea = pygame.Rect(displayx- 300, displayy - 100, 200, 50)

    buymenu = True 
    while buymenu == True:

        exitgamecheck()
        display.fill('black')
        display.blit(font.render("Exit = ESC", True, 'white'),[50,50])  #renders Esc = Exit
        display.blit(font.render(f"Day {daynum}", True, 'white'),[50,100]) #renders current day

        num = 0 #index used to scroll through the materialareas so each material button is sinced with the material being rendered
        for materialname in Items_and_Inventory.allmaterials: #Renders strings and buttons for each existing material in their respective button
            display.blit(font.render(f"{materialname.name}", True, 'white'),[materialareas[num][0] + 10, materialareas[num][1] + 10])
            display.blit(font.render(f"Value: {materialname.value}", True, 'white'),[materialareas[num][0] + 10, materialareas[num][1] + 30])
            display.blit(font.render(f"Owned: {materialname.count}", True, 'white'),[materialareas[num][0] + 10, materialareas[num][1] + 50])
            display.blit(font.render(f"Buy?", True, 'white'),[materialareas[num][0] + 140, materialareas[num][1] + 27])
            pygame.draw.rect(display, 'white', materialareas[num], 1)
            num += 1

        for materialarea in materialareas: #checks for mouse state for each material button
            if checkmousestate(materialarea) == True:
                index = materialareas.index(materialarea)
                material = Items_and_Inventory.allmaterials[index]
                BuyCraftandSell.buy_materials(material)

        display.blit(font.render(F"Currency: {Items_and_Inventory.playerinventory.money}", True, 'white'), (displayx/2, displayy/2))
        display.blit(font.render(F"Recipe Gacha", True, 'white'), (recipegachaarea[0] + 10, recipegachaarea[1] + 10))
        display.blit(font.render(f"Value: {20 + round(1.3 ** len(Items_and_Inventory.OwnedRecipes))}", True, 'white'),[recipegachaarea[0] + 10, recipegachaarea[1] + 30])
        display.blit(font.render(f"Owned: {len(Items_and_Inventory.OwnedRecipes)}", True, 'white'),[recipegachaarea[0] + 10, recipegachaarea[1] + 50])

        #the following condition checks the player has bought all recipes and if so disables the buy button
        if len(Items_and_Inventory.allrecipes) != len(Items_and_Inventory.OwnedRecipes):
            display.blit(font.render(f"Buy?", True, 'white'),[recipegachaarea[0] + 140, recipegachaarea[1] + 27])
        else:
            display.blit(font.render(f"All recipes owned", True, 'white'),[recipegachaarea[0] + 110, recipegachaarea[1] + 27])
        pygame.draw.rect(display, 'white', recipegachaarea, 1)

         #the following condition checks the player hasn't bought all recipes and if so it selects a random recipe to be unlocked when the buy button is pressed 
        if len(Items_and_Inventory.allrecipes) != len(Items_and_Inventory.OwnedRecipes):
            if checkmousestate(recipegachaarea) == True:
                if Items_and_Inventory.playerinventory.money >= 20 + round(1.3 ** len(Items_and_Inventory.OwnedRecipes)):
                    rolling = True
                    while rolling == True:
                        boughtrecipe = random.choice(Items_and_Inventory.allrecipes)
                        if boughtrecipe not in Items_and_Inventory.OwnedRecipes:
                            Items_and_Inventory.playerinventory.money += -(20 + round(1.3 ** len(Items_and_Inventory.OwnedRecipes)))
                            Items_and_Inventory.OwnedRecipes.append(boughtrecipe)
                            rolling = False

        display.blit(font.render(f"Proceed to Crafting", True, 'white'), (gotocrafingarea[0] + 10, gotocrafingarea[1] + 10))
        pygame.draw.rect(display, 'white', gotocrafingarea, 1)
        if checkmousestate(gotocrafingarea) == True:
            buymenu == False
            break
        pygame.display.flip()
        clock.tick(60)
        
def craftmenu(): #Craftmenu screen
    global Items

    weapontypes = {
    "sword" : Items_and_Inventory.allswords,
    "hammer" : Items_and_Inventory.allhammers,
    "bow" : Items_and_Inventory.allbows,
    "helmet" : Items_and_Inventory.allhelmets,
    "chestplate" : Items_and_Inventory.allchestplates,
    "greaves" : Items_and_Inventory.allgreaves}

    #these are the areas where the different buttons will be located
    equipmenttypearea = pygame.Rect(displayx / 4 +75, displayy / 2, 175, 75)
    typeupbutton = pygame.Rect(displayx / 4, displayy / 2, 75, 30)
    typedownbutton = pygame.Rect(displayx / 4, displayy / 2 + 45, 75, 30)
    equipmentlvlarea = pygame.Rect(displayx / 4 + 275, displayy / 2, 75, 75)
    lvlupbutton = pygame.Rect(displayx / 4 + 350, displayy / 2, 75, 30)
    lvldownbutton = pygame.Rect(displayx / 4 + 350, displayy / 2 + 45, 75, 30)
    craftbutton =  pygame.Rect(displayx / 4 + 475, displayy / 2, 175, 75)
    gotosellbutton = pygame.Rect(displayx- 300, displayy - 100, 200, 50)

    #list of always unlocked craft related buttons
    allcraftbuttons = (equipmenttypearea, typeupbutton, typedownbutton, 
                        equipmentlvlarea, lvlupbutton, lvldownbutton)

    allequipmenttypes = ("sword", "hammer", "bow", "helmet", "chestplate", "greaves")
    allequipmentlvls = (1, 2, 3, 4)

    equipmenttypeindex = 0 #Used to scroll between the possible equipment types
    equipmentlvlindex = 0 #Used to scroll between the possible equipment levels
    
    craftmenu = True
    while craftmenu == True:

        selectedequipmenttype = allequipmenttypes[equipmenttypeindex] 
        selectedequipmentlvl = allequipmentlvls[equipmentlvlindex]

        exitgamecheck()
        display.fill('black')
        display.blit(font.render("Exit = ESC", True, 'white'),[50,50])
        display.blit(font.render(f"Day {daynum}", True, 'white'),[50,100])

        display.blit(font.render(f"Type: {selectedequipmenttype}", True, 'white'), (equipmenttypearea[0] + 10, equipmenttypearea[1] + 10))
        display.blit(font.render(f"Lvl {selectedequipmentlvl}", True, 'white'), (equipmentlvlarea[0] + 10, equipmentlvlarea[1] + 10))

        for button in allcraftbuttons:
            pygame.draw.rect(display, 'white', button, 1)
        
        #these 4 functions all draw an arrow in diferent locations to simulate scrolling between equipment types and lvls
        pygame.draw.lines(display, 'white', False, [(displayx /4 +27, displayy /2 +23),(displayx /4 +35, displayy /2 + 7),(displayx /4 +43, displayy /2 +23)], 1)
        pygame.draw.lines(display, 'white', False, [(displayx /4 +27, displayy /2 +52),(displayx /4 +35, displayy /2 + 68),(displayx /4 +43, displayy /2 +52)], 1)

        pygame.draw.lines(display, 'white', False, [(displayx /4 +377, displayy /2 +23),(displayx /4 +385, displayy /2 + 7),(displayx /4 +393, displayy /2 +23)], 1)
        pygame.draw.lines(display, 'white', False, [(displayx /4 +377, displayy /2 +52),(displayx /4 +385, displayy /2 + 68),(displayx /4 +393, displayy /2 +52)], 1)

        if checkmousestate(typeupbutton) == True and equipmenttypeindex != 5:
            equipmenttypeindex += 1
        elif checkmousestate(typedownbutton) == True and equipmenttypeindex != 0:
            equipmenttypeindex += -1
        elif checkmousestate(lvlupbutton) == True and equipmentlvlindex != 3:
            equipmentlvlindex += 1
        elif checkmousestate(lvldownbutton) == True and equipmentlvlindex != 0:
            equipmentlvlindex += -1
        
        selecteditem = weapontypes[selectedequipmenttype][selectedequipmentlvl -1]
        display.blit(font.render(f"Amount owned: {selecteditem.count}, {selecteditem.recipe.description}", True, 'white'), (displayx / 4, displayy / 2 + 100))

        #unlocks the craft button if selected recipe is unlocked
        if selecteditem.recipe in Items_and_Inventory.OwnedRecipes:
            pygame.draw.rect(display, 'white', craftbutton, 1)
            display.blit(font.render(f"Attempt to Craft?", True, 'white'), (craftbutton[0] +25, craftbutton[1] +25))
            #runs the necessary procedures to simulate a crafting attempt
            if checkmousestate(craftbutton) == True:
                materialnumber = -1 #used to scroll inside the recipe quantities for each material
                enoughmaterials = True
                for materialtype in selecteditem.recipe.materials:
                    materialnumber += 1
                    if materialtype.count < selecteditem.recipe.quantities[materialnumber]:
                        enoughmaterials = False
                if enoughmaterials == True:
                    BuyCraftandSell.craftattempt(selecteditem)
                    materialnumber = -1 #used to scroll inside the recipe quantities for each material
                    for materialtype in selecteditem.recipe.materials:
                        materialnumber += 1
                        materialtype.count += -selecteditem.recipe.quantities[materialnumber] 
                       
                    
        else:
            display.blit(font.render(f"Recipe not Owned", True, 'white'), (craftbutton[0] +25, craftbutton[1] +25))

        materialtext = f"Owned materials: {Items_and_Inventory.wood.count} Wood, {Items_and_Inventory.string.count} String,  {Items_and_Inventory.leather.count} Leather, {Items_and_Inventory.iron.count} Iron, {Items_and_Inventory.gold.count} Gold, {Items_and_Inventory.precious_stone.count} Precious Stones"
        display.blit(font.render(materialtext, True, 'white'), (350, 300))

        display.blit(font.render(f"Proceed to Selling", True, 'white'), (gotosellbutton[0] + 10, gotosellbutton[1] + 10))
        pygame.draw.rect(display, 'white', gotosellbutton, 1)
        if checkmousestate(gotosellbutton) == True:
            buymenu == False
            break
        pygame.display.flip()
        clock.tick(60)

def sellmenu(): #Sellmenu screen
    global daynum
    #majority of the following code is the same as the used in the previous function

    weapontypes = {
    "sword" : Items_and_Inventory.allswords,
    "hammer" : Items_and_Inventory.allhammers,
    "bow" : Items_and_Inventory.allbows,
    "helmet" : Items_and_Inventory.allhelmets,
    "chestplate" : Items_and_Inventory.allchestplates,
    "greaves" : Items_and_Inventory.allgreaves}

    equipmenttypearea = pygame.Rect(displayx / 4 +75, displayy / 2, 175, 75)
    typeupbutton = pygame.Rect(displayx / 4, displayy / 2, 75, 30)
    typedownbutton = pygame.Rect(displayx / 4, displayy / 2 + 45, 75, 30)
    equipmentlvlarea = pygame.Rect(displayx / 4 + 275, displayy / 2, 75, 75)
    lvlupbutton = pygame.Rect(displayx / 4 + 350, displayy / 2, 75, 30)
    lvldownbutton = pygame.Rect(displayx / 4 + 350, displayy / 2 + 45, 75, 30)
    priceupbutton = pygame.Rect(displayx / 4 + 650, displayy / 2, 75, 30)
    pricedownbutton = pygame.Rect(displayx / 4 + 650, displayy / 2 +45, 75, 30)
    sellbutton =  pygame.Rect(displayx / 4 + 475, displayy / 2, 175, 75)
    finishdaybutton = pygame.Rect(displayx- 300, displayy - 100, 200, 50)

    allsellbuttons = (equipmenttypearea, typeupbutton, typedownbutton, 
                        equipmentlvlarea, lvlupbutton, lvldownbutton,
                        priceupbutton, pricedownbutton)

    equipmenttypeindex = 0
    equipmentlvlindex = 0
    modifiedsellprice = 0 #modification to the base sell price to be used in the threshold function

    allequipmenttypes = ("sword", "hammer", "bow", "helmet", "chestplate", "greaves")
    allequipmentlvls = (1, 2, 3, 4)
    
    sellmenu = True
    while sellmenu == True:

        selectedequipmenttype = allequipmenttypes[equipmenttypeindex]
        selectedequipmentlvl = allequipmentlvls[equipmentlvlindex]

        exitgamecheck()
        display.fill('black')
        display.blit(font.render("Exit = ESC", True, 'white'),[50,50])
        display.blit(font.render(f"Day {daynum}", True, 'white'),[50,100])

        display.blit(font.render(f"Type: {selectedequipmenttype}", True, 'white'), (equipmenttypearea[0] + 10, equipmenttypearea[1] + 10))
        display.blit(font.render(f"Lvl {selectedequipmentlvl}", True, 'white'), (equipmentlvlarea[0] + 10, equipmentlvlarea[1] + 10))

        for button in allsellbuttons:
            pygame.draw.rect(display, 'white', button, 1)
        
        pygame.draw.lines(display, 'white', False, [(displayx /4 +27, displayy /2 +23),(displayx /4 +35, displayy /2 + 7),(displayx /4 +43, displayy /2 +23)], 1)
        pygame.draw.lines(display, 'white', False, [(displayx /4 +27, displayy /2 +52),(displayx /4 +35, displayy /2 + 68),(displayx /4 +43, displayy /2 +52)], 1)

        pygame.draw.lines(display, 'white', False, [(displayx /4 +377, displayy /2 +23),(displayx /4 +385, displayy /2 + 7),(displayx /4 +393, displayy /2 +23)], 1)
        pygame.draw.lines(display, 'white', False, [(displayx /4 +377, displayy /2 +52),(displayx /4 +385, displayy /2 + 68),(displayx /4 +393, displayy /2 +52)], 1)

        pygame.draw.lines(display, 'white', False, [(displayx /4 +677, displayy /2 +23),(displayx /4 +685, displayy /2 + 7),(displayx /4 +693, displayy /2 +23)], 1)
        pygame.draw.lines(display, 'white', False, [(displayx /4 +677, displayy /2 +52),(displayx /4 +685, displayy /2 + 68),(displayx /4 +693, displayy /2 +52)], 1)

        #modifiedsellprice gets reset so it isn't possible to increase that value event when the item is not owned
        if checkmousestate(typeupbutton) == True and equipmenttypeindex != 5:
            equipmenttypeindex += 1
            modifiedsellprice = 0
        elif checkmousestate(typedownbutton) == True and equipmenttypeindex != 0:
            equipmenttypeindex += -1
            modifiedsellprice = 0
        elif checkmousestate(lvlupbutton) == True and equipmentlvlindex != 3:
            equipmentlvlindex += 1
            modifiedsellprice = 0
        elif checkmousestate(lvldownbutton) == True and equipmentlvlindex != 0:
            equipmentlvlindex += -1
            modifiedsellprice = 0
        elif checkmousestate(priceupbutton) == True and modifiedsellprice != 99:
            modifiedsellprice += 1
        elif checkmousestate(pricedownbutton) == True and equipmentlvlindex != -selecteditem.value:
            modifiedsellprice += -1
        
        selecteditem = weapontypes[selectedequipmenttype][selectedequipmentlvl -1]
        display.blit(font.render(f"Amount owned: {selecteditem.count}, Starting sell price: {selecteditem.value}", True, 'white'), (displayx / 4, displayy / 2 + 100))

        #renders the sell button if selected item is owned
        if selecteditem.count > 0:
            pygame.draw.rect(display, 'white', sellbutton, 1)
            display.blit(font.render(f"Sell for {selecteditem.value + modifiedsellprice}", True, 'white'), (sellbutton[0] +25, sellbutton[1] +25))

            if checkmousestate(sellbutton) == True:
                if dthreshold.dthreshold.client_decision(selecteditem.value, selecteditem.value, selecteditem.value + modifiedsellprice)[0] == True:
                    selecteditem.count += -1
                    Items_and_Inventory.playerinventory.money += selecteditem.value + modifiedsellprice
                    

                    
        else:
            display.blit(font.render(f"Item not Owned", True, 'white'), (sellbutton[0] +25, sellbutton[1] +25))

        display.blit(font.render(f"Proceed to next day", True, 'white'), (finishdaybutton[0] + 10, finishdaybutton[1] + 5))
        #the game will gift the player some money each end of day so it isnt possible to softlock by using all the money on materials/crafting attempts
        display.blit(font.render(f"You will receive {round(len(Items_and_Inventory.OwnedRecipes) ** 1.1 -1) } coins", True, 'white'), (finishdaybutton[0] + 10, finishdaybutton[1] + 25))
        pygame.draw.rect(display, 'white', finishdaybutton, 1)
        if checkmousestate(finishdaybutton) == True:
            sellmenu == False
            Items_and_Inventory.playerinventory.money += round(len(Items_and_Inventory.OwnedRecipes) ** 1.1 -1) 
            daynum += 1
            break

        pygame.display.flip()
        clock.tick(60)

import pygame, sys, Items_and_Inventory, BuyCraftandSell, random, dthreshold, d10_and_end_game
from pygame.locals import *
pygame.font.init()
pygame.init()

clock = pygame.time.Clock()
displayx = 1920
displayy = 1080
display = pygame.display.set_mode((displayx, displayy))

font = pygame.font.SysFont('Comic Sans MS', 15)

starting()

win = False #This will turn true when the player has reached the win condition, otherwise it just enables looping the game
while win == False:
    buymenu()

    craftmenu()

    sellmenu()
    
    if d10_and_end_game.end_game() == True:
        win = True
        break

while win == True:
    exitgamecheck()
    display.fill('black')
    display.blit(font.render("Exit = ESC", True, 'white'),[50,50])
    display.blit(font.render(f"Day {daynum}", True, 'white'),[50,100])

    display.blit(font.render("You Won", True, 'white'), (displayx/2 - 20, displayy/2))
    display.blit(font.render(f"You reached 10K in {daynum} days", True, 'white'), (displayx/2- 65, displayy/2 + 20))

    pygame.display.flip()
    clock.tick(60)

