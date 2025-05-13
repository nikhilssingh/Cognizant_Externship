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
        # if no ingredient provided, exits the loop
    ingredients.append(ingredient)
    # each ingredient appended to the list 
make_sandwich(*ingredients)
    
        
        
    