import json

class RecipeApp:
    def __init__(self):
        self.recipes = {}

    def add_recipe(self):
        name = input("Enter recipe name: ").strip()
        if name in self.recipes:
            print("Recipe already exists.")
            return

        ingredients = input("Enter ingredients (comma-separated): ").strip()
        instructions = input("Enter cooking instructions: ").strip()

        self.recipes[name] = {
            "ingredients": ingredients.split(","),
            "instructions": instructions
        }
        print(f"Recipe '{name}' added successfully!")

    def view_recipes(self):
        if not self.recipes:
            print("No recipes found.")
            return

        for name, details in self.recipes.items():
            print(f"\nRecipe Name: {name}")
            print(f"Ingredients: {', '.join(details['ingredients'])}")
            print(f"Instructions: {details['instructions']}")

    def search_recipe(self):
        name = input("Enter the recipe name to search: ").strip()
        if name in self.recipes:
            details = self.recipes[name]
            print(f"\nRecipe Name: {name}")
            print(f"Ingredients: {', '.join(details['ingredients'])}")
            print(f"Instructions: {details['instructions']}")
        else:
            print("Recipe not found.")

    def delete_recipe(self):
        name = input("Enter the recipe name to delete: ").strip()
        if name in self.recipes:
            del self.recipes[name]
            print(f"Recipe '{name}' deleted successfully!")
        else:
            print("Recipe not found.")

    def save_to_file(self):
        with open("recipes.json", "w") as file:
            json.dump(self.recipes, file)
        print("Recipes saved to 'recipes.json'.")

    def load_from_file(self):
        try:
            with open("recipes.json", "r") as file:
                self.recipes = json.load(file)
            print("Recipes loaded from 'recipes.json'.")
        except FileNotFoundError:
            print("No saved recipes found.")

    def run(self):
        self.load_from_file()

        while True:
            print("\nRecipe App Menu")
            print("1. Add Recipe")
            print("2. View Recipes")
            print("3. Search Recipe")
            print("4. Delete Recipe")
            print("5. Save and Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_recipe()
            elif choice == "2":
                self.view_recipes()
            elif choice == "3":
                self.search_recipe()
            elif choice == "4":
                self.delete_recipe()
            elif choice == "5":
                self.save_to_file()
                print("Exiting Recipe App. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Run the app
if __name__ == "__main__":
    app = RecipeApp()
    app.run()
