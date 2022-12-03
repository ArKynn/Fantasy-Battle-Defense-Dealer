
#----------Items and inventory---------#
class item:
    def __init__(self, name, value, count, min_quality):
        self.name = name
        self.value = value
        self.count = count
        self.min_quality = min_quality

class weapon(item):
    def __init__(self, name, value, damage, count, min_quality):
        super(weapon, self).__init__(name, value, count, min_quality) #Based on answer by Ozgur Vatansever on StackOverflow (https://stackoverflow.com/questions/31899465/python-how-to-correctly-set-up-hierarchy-of-classes)
        self.damage = damage

sword_lvl1 = weapon("Common Sword", 1, 0, 1, 1)
sword_lvl2 = weapon("Rare Sword", 2, 0, 2, 2)
sword_lvl3 = weapon("Exotic Sword", 3, 0, 3, 3)
sword_lvl4 = weapon("Legendary Sword", 4, 0, 4, 4)

hammer_lvl1 = weapon("Common Hammer", 1, 1, 0, 1)
hammer_lvl2 = weapon("Rare Hammer", 2, 2, 0, 2)
hammer_lvl3 = weapon("Exotic Hammer", 3, 3, 0, 3)
hammer_lvl4 = weapon("Legendary Hammer", 4, 4, 0, 4)

bow_lvl1 = weapon("Common Bow", 1, 1, 0, 1)
bow_lvl2 = weapon("Rare Bow", 2, 2, 0, 2)
bow_lvl3 = weapon("Exotic Bow", 3, 3, 0, 3)
bow_lvl4 = weapon("Legendary Bow", 4, 4, 0, 4)

allswords = [sword_lvl1, sword_lvl2, sword_lvl3, sword_lvl4]
allhammers = [hammer_lvl1, hammer_lvl2, hammer_lvl3, hammer_lvl4]
allbows = [bow_lvl1, bow_lvl2, bow_lvl3, bow_lvl4]

class armor(item):
    def __init__(self, name, value, protection, count, min_quality):
        super(armor, self).__init__(name, value, count, min_quality)
        self.protection = protection

helmet_lvl1 = armor("Common Helmet", 1, 1, 0, 1)
helmet_lvl2 = armor("Rare Helmet", 2, 2, 0, 2)
helmet_lvl3 = armor("Exotic Helmet", 3, 3, 0, 3)
helmet_lvl4 = armor("Legendary Helmet", 4, 4, 0, 4)

chestplate_lvl1 = armor("Common Chestplate", 1, 1, 0, 1)
chestplate_lvl2 = armor("Rare Chestplate", 2, 2, 0, 2)
chestplate_lvl3 = armor("Exotic Chestplate", 3, 3, 0, 3)
chestplate_lvl4 = armor("Legendary Chestplate", 4, 4, 0, 4)

greaves_lvl1 = armor("Common Greaves", 1, 1, 0, 1)
greaves_lvl2 = armor("Rare Greaves", 2, 2, 0, 2)
greaves_lvl3 = armor("Exotic Greaves", 3, 3, 0, 3)
greaves_lvl4 = armor("Legendary Greaves", 4, 4, 0, 4)

allhelmets = [helmet_lvl1, helmet_lvl2, helmet_lvl3, helmet_lvl4]
allchestplates =[chestplate_lvl1, chestplate_lvl2, chestplate_lvl3, chestplate_lvl4]
allgreaves = [greaves_lvl1, greaves_lvl2, greaves_lvl3, greaves_lvl4]

class material(item):
    def __init__(self, name, value, count):
        super().__init__(name, value, count)
    
wood = material("Wood", 1, 0)
leather = material("Leather", 2, 0)
iron = material("Iron", 3, 0)
gold = material("gold", 4, 0)

allmaterials = [wood, leather, iron, gold]

weapontypes = [allswords, allhammers, allbows]
armortypes = [allhelmets, allchestplates, allgreaves]
itemtypes = [weapontypes, armortypes]


class playerinventory:
    def __init__(self, money, craftexp):
        self.money = money
        self.craftexp = craftexp

playerinventory = playerinventory(0, 0)

print(f"{itemtypes[1][1][1].name}")