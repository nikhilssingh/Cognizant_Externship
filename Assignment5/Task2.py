def describe_pet(pet_name,animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")
    
while True:
    print("Enter your pet's information (or press 'Enter' to skip): ")
    pet_name = input("Pet's name: ")
    if pet_name.lower() == "":
        break
    
    animal_type = input("Animal type (press 'Enter' for dog(default)): ")
    if animal_type.strip() == "":
        describe_pet(pet_name)
    else:
        describe_pet(pet_name, animal_type)
    