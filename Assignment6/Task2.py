l1 = ["Porsche", "Lamborghini", "Ferrari", "Audi"]
try:
    print(l1[4])
    # IndexError as index 4 element does not exist in the list
except IndexError:
    print("Enter a valid index of the list only.") 

d1 = {"Name":"Nikhil", "Age":21, "City":"Allen", "Sport":"Basketball"}
try:
    print(d1["Hobby"])
    # KeyError as key 'Hobby' does not exist in the dictionary
except KeyError:
    print("Enter a valid key of the dictionary only.")

try:
    result = d1["Name"]+d1["Age"]
    # TypeError as string is being added to integer
except TypeError:
    print("Only the same types can be added.")
else:
    print(result)