
#----------Items and inventory---------#

class weapon:
    def __init__(self, name, value, damage, count):
        self.name = name
        self.value = value
        self.damage = damage
        self.count = count

class sword_lvl1(weapon):
    super().__init__("Common Sword", 1, 1, 0)
class sword_lvl2(weapon):
    super().__init__("Uncommon Sword", 2, 2, 0)
class sword_lvl3(weapon):
    super().__init__("Rare Sword", 3, 3, 0)
class sword_lvl4(weapon):
    super().__init__("Legendary Sword", 4, 4, 0)

class hammer_lvl1(weapon):
    super().__init__("Common Hammer", 1, 1, 0)
class hammer_lvl2(weapon):
    super().__init__("Uncommon Hammer", 2, 2, 0)
class hammer_lvl3(weapon):
    super().__init__("Rare Hammer", 3, 3, 0)
class hammer_lvl4(weapon):
    super().__init__("Legendary Hammer", 4, 4, 0)

class bow_lvl1(weapon):
    super().__init__("Common Bow", 1, 1, 0)
class bow_lvl2(weapon):
    super().__init__("Uncommon Bow", 2, 2, 0)
class bow_lvl3(weapon):
    super().__init__("Rare Bow", 3, 3, 0)
class bow_lvl4(weapon):
    super().__init__("Legendary Bow", 4, 4, 0)

class armor:
    def __init__(self, name, value, protection, count):
        self.name = name
        self.value = value
        self.protection = protection
        self.count = count

class helmet_lvl1(armor):
    super().__init__("Common Helmet", 1, 1, 0)
class helmet_lvl2(armor):
    super().__init__("Uncommon Helmet", 2, 2, 0)
class helmet_lvl3(armor):
    super().__init__("Rare Helmet", 3, 3, 0)
class helmet_lvl4(armor):
    super().__init__("legendary Helmet", 4, 4, 0)

class chestplate_lvl1(armor):
    super().__init__("Common Chestplate", 1, 1, 0)
class chestplate_lvl2(armor):
    super().__init__("Uncommon Chestplate", 2, 2, 0)
class chestplate_lvl3(armor):
    super().__init__("Rare Chestplate", 3, 3, 0)
class chestplate_lvl4(armor):
    super().__init__("legendary Chestplate", 4, 4, 0)

class greave_lvl1(armor):
    super().__init__("Common Greaves", 1, 1, 0)
class greave_lvl2(armor):
    super().__init__("Uncommon Greaves", 2, 2, 0)
class greave_lvl3(armor):
    super().__init__("Rare Greaves", 3, 3, 0)
class greave_lvl4(armor):
    super().__init__("legendary Greaves", 4, 4, 0)

class material:
    def __init__(self, name, value, count):
        self.name = name
        self.value = value

class wood(material):
    super().__init__("Wood", 1, 0)
class leather(material):
    super().__init__("Leather", 2, 0)
class iron(material):
    super().__init__("Iron", 3, 0)
class gold(material):
    super().__init__("Gold", 4, 0)

allswords = [sword_lvl1, sword_lvl2, sword_lvl3, sword_lvl4]
allhammers = [hammer_lvl1, hammer_lvl2, hammer_lvl3, hammer_lvl4]
allbows = [bow_lvl1, bow_lvl2, bow_lvl3, bow_lvl4]

allhelmets = [helmet_lvl1, helmet_lvl2, helmet_lvl3, helmet_lvl4]
allchestplates =[chestplate_lvl1, chestplate_lvl2, chestplate_lvl3, chestplate_lvl4]
allgreaves = [greave_lvl1, greave_lvl2, greave_lvl3, greave_lvl4]

allmaterials = [wood, leather, iron, gold]