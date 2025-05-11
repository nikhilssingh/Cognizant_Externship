inventory = {}

def add_item(item_name, quantity, price):
    if item_name in inventory:
        inventory[item_name] = (inventory[item_name][0] + quantity, price)
        # update quantity if item already exists 
    else:
        inventory[item_name] = (quantity, price)
    print(f"Added {quantity} of {item_name} at ${price:.2f} each.")
    display_inventory()
    
def remove_item(item_name, quantity):
    if item_name in inventory:
        current_quantity, price = inventory[item_name]
        # get current quantity and price
        if current_quantity >= quantity:
            # check if enough quantity to remove
            inventory[item_name] = (current_quantity - quantity, price)
            print(f"Removed {quantity} of {item_name}.")
            if inventory[item_name][0] == 0:
                del inventory[item_name] # delete if quantity is zero
        else:
            print(f"Not enough {item_name} in inventory to remove {quantity}.")
    else:
        print(f"{item_name} not found in inventory.")
    display_inventory()

def update_price(item_name, new_price):
    if item_name in inventory:
        current_quantity, _ = inventory[item_name]
        inventory[item_name] = (current_quantity, new_price)
        # update price
        print(f"Updated price of {item_name} to ${new_price:.2f}.")
    else:
        print(f"{item_name} not found in inventory.")
    display_inventory()
    
def total_value():
    total = 0
    for item, (quantity, price) in inventory.items():
        total += quantity * price
        # calculate total value
    return total

def display_inventory():
    print("Current inventory:")
    for item, (quantity, price) in inventory.items():
        # display each item with its quantity and price
        print(f"{item}: {quantity} units at ${price:.2f} each")
    print(f"Total value of inventory: ${total_value():.2f}")
    
print("Welcome to the Inventory Manager!")
while True:
    print("\nOptions:")
    print("1. Add item")
    print("2. Remove item")
    print("3. Update price")
    print("4. Display inventory")
    print("5. Exit")
    # prompt user for action
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        add_item(item_name, quantity, price)
    elif choice == '2':
        item_name = input("Enter item name to remove: ")
        quantity = int(input("Enter quantity to remove: "))
        remove_item(item_name, quantity)
    elif choice == '3':
        item_name = input("Enter item name to update price: ")
        new_price = float(input("Enter new price: "))
        update_price(item_name, new_price)
    elif choice == '4':
        display_inventory()
    elif choice == '5':
        print("Exiting Inventory Manager.")
        break
    else:
        print("Invalid choice. Please try again.")
        