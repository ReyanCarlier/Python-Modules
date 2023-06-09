cookbook = {
    "Sandwich":{
        "ingredients":("ham", "bread", "cheese", "tomatoes"),
        "meal":"lunch",
        "prep_time":10
	},
    "Cake":{
        "ingredients":("flour", "sugar", "eggs"),
        "meal":"dessert",
        "prep_time":60
	},
    "Salad":{
        "ingredients":("avocado", "arugula", "tomatoes", "spinach"),
        "meal":"lunch",
        "prep_time":15
	}
}

def print_all_recipes():
    for k in cookbook:
        print(k)

def print_recipe_details(recipe_name):
    for recipe in cookbook:
        if (recipe == recipe_name):
            print("Recipe for", recipe_name, ":")
            print("To be eaten for".rjust(2), cookbook[recipe_name]["meal"])
            print("Takes".rjust(2), cookbook[recipe_name]["prep_time"], "minutes of cooking.")
            print("Ingredients :".rjust(2))
            for ingredient in cookbook[recipe_name]["ingredients"]:
                print("- ", ingredient)
            return
    print("This recipe doesn't exist !")

def delete_recipe(recipe_name):
    for k in cookbook:
        if (k == recipe_name):
            cookbook.__delitem__(recipe_name)
            break

def add_recipe_from_input():
    new_recipe = {}
    recipe_name = input("Enter a name:")
    new_recipe["ingredients"] = ()
    print("Type ingredients:")
    while (1):
        new_ingredient = input("> ")
        if new_ingredient != "":
            new_recipe["ingredients"] += tuple([new_ingredient])
        else:
            break
    while (1):
        print("Enter a meal type:")
        meal_type = input("> ")
        if (meal_type != "lunch" and meal_type != "dessert"):
            print("Invalid meal type, can only be : 'lunch' or 'dessert'")
        else:
            new_recipe["meal"] = meal_type
            break
    while (1):
        print("Enter a preparation time:")
        prep_time = input("> ")
        try:
            prep_time = int(prep_time)
            if (prep_time <= 0):
                print("Preparation time must be a positive integer")
                continue
            new_recipe["prep_time"] = prep_time
            break
        except:
            print("Preparation time must be a positive integer")
    cookbook[recipe_name] = new_recipe

def main():
    print("Welcome to the Python Cookbook !")

    while (1):
        print("--------------------------")
        print("List of available option:")
        print("1: Add a recipe".rjust(4))
        print("2: Delete a recipe".rjust(4))
        print("3: Print a recipe".rjust(4))
        print("4: Print the cookbook".rjust(4))
        print("5: Quit".rjust(4))
        print("--------------------------")
        print("Please select an option :")
        option = input(">> ")
        match option:
            case "1":
                add_recipe_from_input()
            case "2":
                print("Please enter the name of the recipe you would like to delete:")
                delete_recipe(input(">> "))
            case "3":
                print("Please enter a recipe name to get its details:")
                print_recipe_details(input(">> "))
            case "4":
                print_all_recipes()
            case "5":
                break
            case _:
                print("Sorry, this option does not exist.")
    print("Cookbook closed. Goodybe !")

if (__name__ == "__main__"):
    main()