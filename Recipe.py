
class recipe:

    def __init__(self, name, materials, quantities, value, acquired:bool):
        self.name = name
        self.materials = materials
        self.quantities = quantities
        self.value = value        
        self.acquired = False
        self.description = self.desc
    

    def display(self):
        print("Recipe")
        print("   Name: " + self.name)
        print("   Description " + self.description)

    #function that builds each recipe description based on materials and quantities required
    def desc(self):
        ret = "Needs"
        for i in range (0 , len(self.materials)):
            ret += str(self.quantities[i]) + "*" + (self.materials[i]) + ", "
        return ret.strip (", ") # A way to remove some characters at the end of a string. https://www.pythonforbeginners.com/basics/string-manipulation-in-python





