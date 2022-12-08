
class recipe:

    def __init__(self, name, materials, quantities, description):
        self.name = name
        self.materials = materials
        self.quantities = quantities
        self.description = description
    

    def display(self):
        print("Recipe")
        print("   Name: " + self.name)
        print("   Description " + self.description)
        





