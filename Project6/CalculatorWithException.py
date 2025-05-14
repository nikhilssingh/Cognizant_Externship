import logging 

logging.basicConfig(
    filename="Project6/error_log.txt",
    level=logging.ERROR,
    format="%(levelname)s:%(asctime)s:%(message)s"
)

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

while True:
    print("\nWelcome to the Error-Free Calculator!")
    print("Please choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        option = int(input("Enter option (1-4): "))
        if option not in [1, 2, 3, 4]:
            raise ValueError("Invalid operation choice.")
    except ValueError as e:
        print(f"Error: {e} Please enter a number between 1 and 4.")
        logging.error(f"ValueError occurred: {e}")
        continue
    else:
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
        except ValueError as e:
            print("Error: Please enter valid numeric values.")
            logging.error(f"ValueError occurred: {e}")
            continue
        else:
            try:
                if option == 1:
                    result = addition(a, b)
                    print(f"Result: {a} + {b} = {result}")
                elif option == 2:
                    result = subtraction(a, b)
                    print(f"Result: {a} - {b} = {result}")
                elif option == 3:
                    result = multiplication(a, b)
                    print(f"Result: {a} * {b} = {result}")
                elif option == 4:
                    result = division(a, b)
                    print(f"Result: {a} ÷ {b} = {result}")
            except ZeroDivisionError as e:
                print("Error: Division by zero is not allowed.")
                logging.error(f"ZeroDivisionError occurred: {e}")
            else:
                print("Operation completed successfully.\n")
