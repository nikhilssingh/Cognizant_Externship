num1 = int(input("Enter a number for which factorial should be calculated: "))
num2 = int(input("Enter a number for which fibonacci should be calculated: "))

def factorial(num1):
    if num1==0 or num1==1:
    # base case for 0 and 1
        return 1
    else:
        return num1*factorial(num1-1)

print(f"The factorial of {num1} is {factorial(num1)}.")
        
def fibonacci(num2):
    if num2==0:
        return 0
    elif num2==1:
        return 1
    else:
        return fibonacci(num2-1) + fibonacci(num2-2)
    
print(f"The fibonacci of {num2} is {fibonacci(num2)}.")