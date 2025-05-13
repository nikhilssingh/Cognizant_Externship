def describe_pet(pet_name,animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")
    
while True:
    print("Enter your pet's information (or press 'Enter' to skip): ")
    pet_name = input("Pet's name: ")
    if pet_name.lower() == "":
        break
        # exit the loop if no pet name provided
    animal_type = input("Animal type (press 'Enter' for dog(default)): ")
    if animal_type.strip() == "":
        describe_pet(pet_name)
        # if no animal type provided, defaults to dog
    else:
        describe_pet(pet_name, animal_type)
    