def exitgamecheck(): #If ESC is pressed, shutsdown program
    global mouse1
    for event in pygame.event.get(eventtype=KEYDOWN):
        if event.key==pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

#Checks for mouse position, lights up button in red and checks if mouse is pressed
def checkmousestate(rectanglearea):
    global mouse1
    if rectanglearea.collidepoint(pygame.mouse.get_pos()):  #Based on answer by skrx on StackOverfow (https://stackoverflow.com/questions/44998943/how-to-check-if-the-mouse-is-clicked-in-a-certain-area-pygame)
        pygame.draw.rect(display, 'red', rectanglearea, 1)
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
        display.blit(font.render("Exit = ESC", True, 'white'),[50,50])
        display.blit(font.render(f"Day {daynum}", True, 'white'),[50,100])

        num = 0
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
        display.blit(font.render(f"Value: {4 + len(Items_and_Inventory.OwnedRecipes)}", True, 'white'),[recipegachaarea[0] + 10, recipegachaarea[1] + 30])
        display.blit(font.render(f"Owned: {len(Items_and_Inventory.OwnedRecipes)}", True, 'white'),[recipegachaarea[0] + 10, recipegachaarea[1] + 50])
        if len(Items_and_Inventory.allrecipes) != len(Items_and_Inventory.OwnedRecipes):
            display.blit(font.render(f"Buy?", True, 'white'),[recipegachaarea[0] + 140, recipegachaarea[1] + 27])
        else:
            display.blit(font.render(f"All recipes owned", True, 'white'),[recipegachaarea[0] + 110, recipegachaarea[1] + 27])
        pygame.draw.rect(display, 'white', recipegachaarea, 1)


        if len(Items_and_Inventory.allrecipes) != len(Items_and_Inventory.OwnedRecipes):
            if checkmousestate(recipegachaarea) == True:
                if Items_and_Inventory.playerinventory.money >= 4 + len(Items_and_Inventory.OwnedRecipes):
                    rolling = True
                    while rolling == True:
                        boughtrecipe = random.choice(Items_and_Inventory.allrecipes)
                        if boughtrecipe not in Items_and_Inventory.OwnedRecipes:
                            Items_and_Inventory.OwnedRecipes.append(boughtrecipe)
                            Items_and_Inventory.playerinventory.money += -(4 + len(Items_and_Inventory.OwnedRecipes))
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

    equipmenttypearea = pygame.Rect(displayx / 4 +75, displayy / 2, 175, 75)
    typeupbutton = pygame.Rect(displayx / 4, displayy / 2, 75, 30)
    typedownbutton = pygame.Rect(displayx / 4, displayy / 2 + 45, 75, 30)
    equipmentlvlarea = pygame.Rect(displayx / 4 + 275, displayy / 2, 75, 75)
    lvlupbutton = pygame.Rect(displayx / 4 + 350, displayy / 2, 75, 30)
    lvldownbutton = pygame.Rect(displayx / 4 + 350, displayy / 2 + 45, 75, 30)
    craftbutton =  pygame.Rect(displayx / 4 + 475, displayy / 2, 175, 75)
    gotosellbutton = pygame.Rect(displayx- 300, displayy - 100, 200, 50)

    allcraftbuttons = (equipmenttypearea, typeupbutton, typedownbutton, 
                        equipmentlvlarea, lvlupbutton, lvldownbutton)

    allequipmenttypes = ("sword", "hammer", "bow", "helmet", "chestplate", "greaves")
    allequipmentlvls = (1, 2, 3, 4)

    equipmenttypeindex = 0
    equipmentlvlindex = 0
    
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

        if selecteditem.recipe in Items_and_Inventory.OwnedRecipes:
            pygame.draw.rect(display, 'white', craftbutton, 1)
            display.blit(font.render(f"Attempt to Craft?", True, 'white'), (craftbutton[0] +25, craftbutton[1] +25))

            if checkmousestate(craftbutton) == True:
                materialnumber = -1
                enoughmaterials = True
                for materialtype in selecteditem.recipe.materials:
                    materialnumber += 1
                    if materialtype.count < selecteditem.recipe.quantities[materialnumber]:
                        enoughmaterials = False
                if enoughmaterials == True:
                    BuyCraftandSell.craftattempt(selecteditem)
                    materialnumber = -1
                    for materialtype in selecteditem.recipe.materials:
                        materialtype.count += -selecteditem.recipe.quantities[materialnumber] 
                        materialnumber += 1
                    
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
    modifiedsellprice = 0

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

        if selecteditem.count > 0:
            pygame.draw.rect(display, 'white', sellbutton, 1)
            display.blit(font.render(f"Sell for {selecteditem.value + modifiedsellprice}", True, 'white'), (sellbutton[0] +25, sellbutton[1] +25))

            if checkmousestate(sellbutton) == True:
                pass #threshold + normal sell function
                    
        else:
            display.blit(font.render(f"Item not Owned", True, 'white'), (sellbutton[0] +25, sellbutton[1] +25))

        display.blit(font.render(f"Proceed to next day", True, 'white'), (finishdaybutton[0] + 10, finishdaybutton[1] + 5))
        display.blit(font.render(f"You will receive {5 + Items_and_Inventory.playerinventory.craftexp} coins", True, 'white'), (finishdaybutton[0] + 10, finishdaybutton[1] + 25))
        pygame.draw.rect(display, 'white', finishdaybutton, 1)
        if checkmousestate(finishdaybutton) == True:
            sellmenu == False
            Items_and_Inventory.playerinventory.money += 5 + Items_and_Inventory.playerinventory.craftexp
            daynum += 1
            break

        pygame.display.flip()
        clock.tick(60)
        pass

import pygame, sys, Items_and_Inventory, BuyCraftandSell, random
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