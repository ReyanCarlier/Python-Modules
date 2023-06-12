from book import Book
from recipe import Recipe
import time

def main():
    myBook = Book("Grandma's book")
    newRecipe = Recipe("tourte", 3, 40, {"parmesan", "aubergine"}, "lunch", "Ma's tourte")
    time.sleep(0.04)
    myBook.add_recipe(newRecipe)
    myBook.add_recipe(Recipe("crepe", 5, 60, {"wheat", "milk", "eggs", "butter"}, "dessert", "Pa's famous crepes"))
    
    #print(myBook)
    #print(myBook.get_recipe_by_name("tourte"))
    print(myBook.get_recipes_by_type("lunch"))
    print(myBook.get_recipe_by_name("crepe"))

if (__name__ == "__main__"):
    main()