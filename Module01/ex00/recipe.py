from dataclasses import dataclass

@dataclass
class Recipe:
    name: str
    cooking_lvl: int
    cooking_time: int
    ingredients: list
    description: str
    recipe_type: str

    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description=""):
        if (cooking_lvl < 1 or cooking_lvl > 5):
            print("Cooking level must be 1 <= x <= 5")
            raise ValueError
        if (cooking_time < 0):
            print("Cooking time must be a positive integer")
            raise ValueError
        if (len(ingredients) == 0):
            print("A recipe can't be made of thin air!")
            raise ValueError
        if (len(name) == 0):
            print("Recipe must have a name !")
            raise ValueError
        if (recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert"):
            print("Invalid recipe type")
            raise ValueError
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
    
    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        txt += "Recipe : " + self.name
        txt += "\nType : " + self.recipe_type
        txt += "\nCooking level required : " + str(self.cooking_lvl)
        txt += "\nCooking time : " + str(self.cooking_time)
        txt += "\nIngredients : " + str(self.ingredients)
        txt += "\nDescription : " + self.description
        return txt