str2 = " hello, python world! "
 
stripped_str = str2.strip()
print("String after stripping:", stripped_str)

capitalized_str = stripped_str.capitalize()
print("String after capitalizing:", capitalized_str)

replaced_str = capitalized_str.replace("world", "universe") 
print("String after replacing 'world' with 'universe':", replaced_str)

upper_str = replaced_str.upper()
print("String in uppercase:", upper_str)