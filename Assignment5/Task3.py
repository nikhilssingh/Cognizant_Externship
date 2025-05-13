def make_sandwich(*ingredients):
    print(f"Making a sandwich with the following ingredients: ")
    for item in ingredients:
        print(f"- {item}")

ingredients = []
print("Enter the sandwich ingredients (one at a time)")
while True:
    ingredient = input("Ingredient: ")
    if ingredient.strip() == "":
        break
    ingredients.append(ingredient)
    
make_sandwich(*ingredients)
    
        
        
    