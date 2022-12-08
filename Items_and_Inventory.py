#----------Items and inventory---------#
from Recipe import recipe


class item:
    def __init__(self, name, value, count):
        self.name = name
        self.value = value
        self.count = count
    
    def display(self):
        print("Name: " + self.name)
        print("Value: " + str(self.value))
        print("Count: " + str(self.count))


class weapon(item):
    def __init__(self, name, value, modified_value, count, damage, min_quality, recipe, c_rdr ,recipeowned):
        super(weapon, self).__init__(name, value, count) #Based on answer by Ozgur Vatansever on StackOverflow (https://stackoverflow.com/questions/31899465/python-how-to-correctly-set-up-hierarchy-of-classes)
        self.damage = damage
        self.min_quality = min_quality
        self.recipe = recipe
        self.c_rdr = c_rdr
        self.recipeowned = recipeowned
        self.modified_value = modified_value

    def display(self):
        super().display()
        print("Damage: " + str(self.damage))
        print("Quality: " + str(self.min_quality))

class armor(item):
    def __init__(self, name, value, modified_value, count, protection, min_quality, recipe, c_rdr, recipeowned):
        super(armor, self).__init__(name, value, count)
        self.protection = protection
        self.min_quality = min_quality
        self.recipe = recipe
        self.c_rdr = c_rdr
        self.recipeowned = recipeowned
        self.modified_value = modified_value 

    def display(self):
        super().display()       
        print("Protection: " + str(self.protection))
        print("Quality: " + str(self.min_quality))
    


class material(item):
    def __init__(self, name, value, count):
        super().__init__(name, value, count)


wood = material("Wood", 5, 0)
string = material("String", 5, 0)
leather = material("Leather", 6, 0)
iron = material("Iron", 10, 0)
gold = material("Gold", 20, 0)
precious_stone = material("Precious Stone", 50, 0)

recipe_sword_lvl1 = recipe("Common Sword recipe", (wood, iron, leather), (1, 1, 1), "Needs 1*wood, 1*iron, 1*leather")
recipe_sword_lvl2 = recipe("Rare Sword recipe", (wood, iron, leather), (1, 2, 1), "Needs 1*wood, 2*iron, 1*leather")
recipe_sword_lvl3 = recipe("Exotic Sword recipe", (wood, iron, leather , gold), (1, 2, 1, 1), "Needs 1*wood, 2*iron, 1*leather , 1*gold")
recipe_sword_lvl4 = recipe("Legendary Sword recipe", (wood, iron, leather , gold, precious_stone), (1, 2, 1, 2, 1), "Needs 1*wood, 2*iron, 1*leather, 2*gold, 1*precious stone")

recipe_hammer_lvl1 = recipe("Common Hammer recipe", (wood, iron, leather), (1, 2, 2), "Needs 1*wood, 2*iron, 2*leather")
recipe_hammer_lvl2 = recipe("Rare Hammer recipe", (wood, iron, leather), (1, 3, 2), "Needs 1*wood, 3*iron, 2*leather")
recipe_hammer_lvl3 = recipe("Exotic Hammer recipe", (wood, iron, leather), (1, 4, 2), "Needs 1*wood, 4*iron, 2*leather")
recipe_hammer_lvl4 = recipe("Legendary Hammer recipe", (wood, iron, leather , precious_stone), (1, 5, 2, 1), "Needs 1*wood, 5*iron, 2*leather, 1*precious stone")

recipe_bow_lvl1 = recipe("Common Bow recipe", (wood, iron, string), (2, 1, 1), "Needs 2*wood, 1*iron, 1*string")
recipe_bow_lvl2 = recipe("Rare Bow recipe", (wood, iron, string), (3, 1, 1), "Needs 3*wood, 1*iron, 1*string")
recipe_bow_lvl3 = recipe("Exotic Bow recipe", (wood, gold, string), (4, 1, 1), "Needs 4*wood, 1*gold, 1*string")
recipe_bow_lvl4 = recipe("Legendary Bow recipe", (wood, gold, string, precious_stone), (4, 2, 2, 1), "4*wood, 2*gold, 2*string, 1*precious stone")

recipe_helmet_lvl1 = recipe("Common Helmet recipe", (iron), (3), "Needs 3*iron")
recipe_helmet_lvl2 = recipe("Rare Helmet recipe", (iron, leather), (3, 2), "Needs 3*iron, 2*leather")
recipe_helmet_lvl3 = recipe("Exotic Helmet recipe", (iron, leather, gold), (4, 2, 1), "Needs 4*iron, 2*leather, 1*gold")
recipe_helmet_lvl4 = recipe("Legendary Helmet recipe", (iron, leather, gold, precious_stone), (4, 2, 2, 1), "Needs 4*iron, 2*leather, 2*gold, 1*precious stone")

recipe_chestplate_lvl1 = recipe("Common Chestplate recipe", (iron, leather), (6, 1), "Needs 6*iron, 1*leather")
recipe_chestplate_lvl2 = recipe("Rare Chestplate recipe", (iron, leather), (7, 1), "Needs 7*iron, 1*leather")
recipe_chestplate_lvl3 = recipe("Exotic Chestplate recipe", (iron, leather, gold), (7, 2, 1), "Needs 7*iron, 2*leather, 1*gold")
recipe_chestplate_lvl4 = recipe("Legendary Chestplate recipe", (iron, leather , precious_stone), (8, 2, 2, 1), "Needs 8*iron, 2*leather, 1*gold, 1*precious stone")

recipe_greaves_lvl1 = recipe("Common Greaves recipe", (iron, leather), (3, 1), "Needs 3*iron, 1*leather")
recipe_greaves_lvl2 = recipe("Rare Greaves recipe", (iron, leather), (4, 1), "Needs 4*iron, 1*leather")
recipe_greaves_lvl3 = recipe("Exotic Greaves recipe", (iron, leather, gold), (4, 1, 1), "Needs 4*iron, 1*leather, 1*gold")
recipe_greaves_lvl4 = recipe("Legendary Greaves recipe", (iron, leather , precious_stone), (5, 1, 2, 1), "Needs 4*iron, 1*leather, 1*gold, 1*precious stone")



sword_lvl1 = weapon("Common Sword", 20, 0, 0, 1, 1, recipe_sword_lvl1, 10, True)
sword_lvl2 = weapon("Rare Sword", 25, 0, 2, 2, recipe_sword_lvl2, 12, False) 
sword_lvl3 = weapon("Exotic Sword", 40, 0, 3, 3, recipe_sword_lvl3, 19, False) 
sword_lvl4 = weapon("Legendary Sword", 100, 0, 4, 4, recipe_sword_lvl4, 24, False)

hammer_lvl1 = weapon("Common Hammer", 25, 0, 0, 1, 1, recipe_hammer_lvl1, 12, True)
hammer_lvl2 = weapon("Rare Hammer", 30, 0, 2, 2, recipe_hammer_lvl2, 15, False)
hammer_lvl3 = weapon("Exotic Hammer", 50, 0, 3, 3, recipe_hammer_lvl3, 20, False)
hammer_lvl4 = weapon("Legendary Hammer", 150, 0, 4, 4, recipe_hammer_lvl4, 28, False)

bow_lvl1 = weapon("Common Bow", 10, 0, 0, 1, 1, recipe_bow_lvl1, 13, True)
bow_lvl2 = weapon("Rare Bow", 15, 0, 0, 2, 2, recipe_bow_lvl2, 18, False)
bow_lvl3 = weapon("Exotic Bow", 30, 0, 0, 3, 3, recipe_bow_lvl3, 25, False)
bow_lvl4 = weapon("Legendary Bow", 80, 0, 0, 4, 4, recipe_bow_lvl4, 28, False)

helmet_lvl1 = armor("Common Helmet", 30, 0, 0, 1, 1, recipe_helmet_lvl1, 10, True)
helmet_lvl2 = armor("Rare Helmet", 35, 0, 0, 2, 2, recipe_helmet_lvl2, 14, False)
helmet_lvl3 = armor("Exotic Helmet", 60, 0, 0, 3, 3, recipe_helmet_lvl3, 16, False)
helmet_lvl4 = armor("Legendary Helmet", 180, 0, 0, 4, 4, recipe_helmet_lvl4, 22, False)

chestplate_lvl1 = armor("Common Chestplate", 35, 0, 0, 1, 1, recipe_chestplate_lvl1, 14, True)
chestplate_lvl2 = armor("Rare Chestplate", 40, 0, 0, 2, 2, recipe_chestplate_lvl2, 20, False)
chestplate_lvl3 = armor("Exotic Chestplate", 70, 0, 0, 3, 3, recipe_chestplate_lvl3, 23, False)
chestplate_lvl4 = armor("Legendary Chestplate", 200, 0, 0, 4, 4, recipe_chestplate_lvl4, 29, False)

greaves_lvl1 = armor("Common Greaves", 30, 0, 0, 1, 1, recipe_greaves_lvl1, 10, True)
greaves_lvl2 = armor("Rare Greaves", 35, 0, 0, 2, 2, recipe_greaves_lvl2, 15, False)
greaves_lvl3 = armor("Exotic Greaves", 60, 0, 0, 3, 3, recipe_greaves_lvl3, 20, False)
greaves_lvl4 = armor("Legendary Greaves", 170, 0, 0, 4, 4, recipe_greaves_lvl4, 25, False)


allmaterials = [wood, string, leather, iron, gold, precious_stone]

allswords = [sword_lvl1, sword_lvl2, sword_lvl3, sword_lvl4]
allhammers = [hammer_lvl1, hammer_lvl2, hammer_lvl3, hammer_lvl4]
allbows = [bow_lvl1, bow_lvl2, bow_lvl3, bow_lvl4]
allhelmets = [helmet_lvl1, helmet_lvl2, helmet_lvl3, helmet_lvl4]
allchestplates = [chestplate_lvl1, chestplate_lvl2, chestplate_lvl3, chestplate_lvl4]
allgreaves = [greaves_lvl1, greaves_lvl2, greaves_lvl3, greaves_lvl4]



OwnedRecipes = [recipe_sword_lvl1, recipe_bow_lvl1, recipe_hammer_lvl1, recipe_chestplate_lvl1, recipe_greaves_lvl1, recipe_helmet_lvl1]
allrecipes = [recipe_sword_lvl1, recipe_bow_lvl1, recipe_hammer_lvl1, recipe_chestplate_lvl1, recipe_greaves_lvl1, recipe_helmet_lvl1,
                recipe_sword_lvl2, recipe_bow_lvl2, recipe_hammer_lvl2, recipe_chestplate_lvl2, recipe_greaves_lvl2, recipe_helmet_lvl2,
                recipe_sword_lvl3, recipe_bow_lvl3, recipe_hammer_lvl3, recipe_chestplate_lvl3, recipe_greaves_lvl3, recipe_helmet_lvl3,
                recipe_sword_lvl4, recipe_bow_lvl4, recipe_hammer_lvl4, recipe_chestplate_lvl4, recipe_greaves_lvl4, recipe_helmet_lvl4]

class playerinventory:
    def __init__(self, money, craftexp):
        self.money = money
        self.craftexp = craftexp

playerinventory = playerinventory(100, 0)




    

