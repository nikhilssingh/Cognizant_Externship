while True:
    try:
        num = float(input("Enter a number: "))
        result = 100/num
    except ZeroDivisionError:
        print("Oops! You cannot divide by zero.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    else:
        print(f"100 divided by {num} is {result}.")
        break