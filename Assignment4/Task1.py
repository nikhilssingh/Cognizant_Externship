fav_fruits = ['strawberry', 'banana', 'mango', 'kiwi', 'grapes']
print(f"Original list of favorite fruits: {fav_fruits}")
fav_fruits.append('lychee')
print(f"After adding a fruit: {fav_fruits}")
fav_fruits.remove('mango')
print(f"After removing a fruit: {fav_fruits}")
fav_fruits = fav_fruits[::-1]
print(f"Reversed list: {fav_fruits}")

# The code above demonstrates how to manipulate a list of favorite fruits by adding a new fruit, removing an existing one, and reversing the order of the list. It prints the list at each step to show the changes made.