num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

while True:
    try:
        num1 = float(num1)
        num2 = float(num2)
        result=num1/num2
    except ZeroDivisionError:
        print("The divisor cannot be 0!")
    except ValueError:
        print("Please enter valid numbers!")
    else:
        print(f"The result is {result}.")
        break
    finally:
        print("This block always executes.")
        break