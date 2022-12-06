def exitgamecheck(): #If ESC is pressed, shutsdown program
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

#Checks for mouse position, lights up rectangle in red and checks if mouse is pressed
def checkmousestate(rectanglearea): #Based on answer by skrx on StackOverfow (https://stackoverflow.com/questions/44998943/how-to-check-if-the-mouse-is-clicked-in-a-certain-area-pygame)
    if rectanglearea.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(display, 'red', rectanglearea, 1)
        if pygame.mouse.get_pressed()[0]:
            return True

def starting(): #Starting screen
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
                if BuyCraftandSell.buy_materials(material) == True:
                    pass
                else:
                    pass #render error message
                pygame.time.wait(150)
                print(str(materialarea))

        display.blit(font.render(F"Currency: {Items_and_Inventory.playerinventory.money}", True, 'white'), (displayx/2, displayy/2))
        
        display.blit(font.render(F"Recipe Gacha", True, 'white'), (recipegachaarea[0] + 10, recipegachaarea[1] + 10))
        display.blit(font.render(f"Value: {4 + len(Items_and_Inventory.OwnedRecipes)}", True, 'white'),[recipegachaarea[0] + 10, recipegachaarea[1] + 30])
        display.blit(font.render(f"Owned: {len(Items_and_Inventory.OwnedRecipes)}", True, 'white'),[recipegachaarea[0] + 10, recipegachaarea[1] + 50])
        display.blit(font.render(f"Buy?", True, 'white'),[recipegachaarea[0] + 140, recipegachaarea[1] + 27])
        pygame.draw.rect(display, 'white', recipegachaarea, 1)

        if checkmousestate(recipegachaarea) == True:
            if Items_and_Inventory.playerinventory.money >= 4 + len(Items_and_Inventory.OwnedRecipes):
                pass 

        pygame.display.flip()
        clock.tick(60)
        





import pygame, sys, Items_and_Inventory, BuyCraftandSell
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

woodarea = pygame.Rect(300, displayy/2 - 200, 250, 75)
stringarea = pygame.Rect(woodarea[0], woodarea[1] +100, 250, 75)
leatherarea = pygame.Rect(woodarea[0], woodarea[1] +200, 250, 75)
ironarea = pygame.Rect(woodarea[0], woodarea[1] +300, 250, 75)
goldarea = pygame.Rect(woodarea[0], woodarea[1] +400, 250, 75)
precisousarea = pygame.Rect(woodarea[0], woodarea[1] +500, 250, 75)

materialareas = (woodarea, stringarea, leatherarea, ironarea, goldarea, precisousarea)

recipegachaarea = pygame.Rect(displayx/2, displayy/2 + 100, 250, 75)

while True:
    starting()

    while win == False:
        buymenu()
    
    pygame.display.flip()
    clock.tick(60)
    