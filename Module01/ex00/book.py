from dataclasses import dataclass
from datetime import datetime

@dataclass
class Book:
    name: str
    last_update: datetime
    creation_date: datetime
    recipes_list: dict
    
    def __init__(self, name):
        if (len(name) == 0):
            print("Book must have a name.")
            raise ValueError
        self.name = name
        timer = datetime.now()
        self.last_update = timer
        self.creation_date = timer
        self.recipes_list = {
            "starter":[],
            "lunch":[],
            "dessert":[]
		}

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name and returns the instance"""
        for types in self.recipes_list:
            for rec in self.recipes_list[types]:
                if (rec.name == name):
                    print(str(rec))
                    return rec

    def get_recipes_by_type(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        str = ""
        i = 0
        for rec in self.recipes_list[recipe_type]:
            str += rec.name
            if (i < len(self.recipes_list[recipe_type]) - 1):
                str += " "
            i+=1
        return str

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        try:
            self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.now()
        except ValueError:
            print("Invalid recipe.")