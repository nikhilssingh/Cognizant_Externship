tuple1 = ('Interstellar', 'Solo', 'Jack Reacher : Die Trying')
print(f"Favorite things: {tuple1}")

try:
# Attempting to change an element in a tuple
    tuple1[1] = 'The Social Network'
    print(f"Updated tuple: {tuple1}")
except TypeError as e:
    print("Oops! Tuples cannot be changed.")

length = len(tuple1)
print(f"Length of the tuple: {length}")