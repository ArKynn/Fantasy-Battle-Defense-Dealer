def exitgamecheck(): #If ESC is pressed, shutsdown program
    global mouse1
    for event in pygame.event.get(eventtype=KEYDOWN):
        if event.key==pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

#Checks for mouse position, lights up button in red and checks if mouse is pressed
def checkmousestate(rectanglearea): #Based on answer by skrx on StackOverfow (https://stackoverflow.com/questions/44998943/how-to-check-if-the-mouse-is-clicked-in-a-certain-area-pygame)
    global mouse1
    if rectanglearea.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(display, 'red', rectanglearea, 1)
        for event in pygame.event.get(eventtype=MOUSEBUTTONDOWN):
            if event.button == 1:
                return True


def starting(): #Starting screen, renders a simple starting button
    starting = True
    while starting == True:
        exitgamecheck()
        display.fill('black')

        display.blit(font.render("Start?", True, 'white'), [displayx / 2, displayy / 2])
        pygame.draw.rect(display, 'white', startarea, 1)
    
        if checkmousestate(startarea) == True:
            starting = False
            
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

        pygame.display.flip()
        clock.tick(60)
        
def craftmenu():
    equipmenttypearea = pygame.Rect(displayx / 4, displayy / 2, 175, 75)
    typeupbutton = pygame.Rect(displayx / 4, displayy / 2, 75, 30)
    typedownbutton = pygame.Rect(displayx / 4, displayy / 2 + 45, 75, 30)
    equipmentlvlarea = pygame.Rect(displayx / 4 + 275, displayy / 2, 75, 75)
    lvlupbutton = pygame.Rect(displayx / 4 + 350, displayy / 2, 75, 30)
    lvldownbutton = pygame.Rect(displayx / 4 + 350, displayy / 2 + 45, 75, 30)
    recipematerialarea = pygame.Rect(displayx / 4, displayy / 2 + 100, 250, 30)
    craftbutton =  pygame.Rect(displayx / 4 + 475, displayy / 2, 75, 30)
    gotosellbutton = pygame.Rect(displayx- 300, displayy - 100, 200, 50)

    selectedequipmenttype = "not yet"
    selectedequipmentlvl = "null"

    display.blit(font.render(f"{selectedequipmenttype}", True, 'white'), (equipmenttypearea[0] + 10, equipmentlvlarea[1] + 10))

    display.blit(font.render(f"{selectedequipmentlvl}", True, 'white'), (equipmenttypearea[0] + 10, equipmentlvlarea[1] + 10))


    craftmenu = True
    while craftmenu == True:

        exitgamecheck()
        display.fill('black')
        display.blit(font.render("Exit = ESC", True, 'white'),[50,50])

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
startarea = pygame.Rect(displayx/2 - 100, displayy/2 - 25, 250, 75)

win = False #This will turn true when the player has reached the win condition, otherwise it just enables looping the game



while True:
    starting()

    while win == False:
        buymenu()
    
        craftmenu()

    pygame.display.flip()
    clock.tick(60)
    