class Recipe:
    def __init__(self,recipe_name,ingredients,time,instructions):
        self.recipe_name=recipe_name
        self.ingredients=ingredients
        self.time=time
        self.instructions=instructions
    def printt(self):
        print(f"Name: {self.recipe_name}")
        print(f"Ingredients: {self.ingredients}")
        print(f"Cooding Time: {self.time}")
        print(f"Instructions: {self.instructions}")

ask_recipe_name=input("Enter recipe name:\n")
ask_ingredients=input("Enter ingredients:\n")
ask_time=input("Enter cooking time:\n")
ask_instructions=input("Enter cooking instructions:\n")

print("Welcome to Recipe Collection")#رسالة ترحيب
food1=Recipe(ask_recipe_name,ask_ingredients,ask_time,ask_instructions)
print("Displaying recipe........")
food1.printt()