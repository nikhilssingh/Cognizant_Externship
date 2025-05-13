name = input("Enter your name: ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def greet_user(name):
    print(f"Hello, {name}! Welcome aboard.")

greet_user(name)

def add_numbers(num1,num2):
    result = num1 + num2
    # not using variable name 'sum' as it can cause confusion
    return result

print(f"The sum of {num1} and {num2} is {add_numbers(num1,num2)}.")
