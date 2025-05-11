my_info = {"name": "Nikhil", "age": 21, "city": "Allen"}
my_info.update({"favorite color": "blue"})
my_info.update({"city": "Dallas"})

keys_str = ", ".join(my_info.keys())
values_str = ", ".join(str(x) for x in (my_info.values()))
print(f"Keys: {keys_str}")
print(f"Values: {values_str}")