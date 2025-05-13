import turtle

def factorial(n):
    if n==0 or n==1:
    # base case for 0 and 1
        return 1
    else:
        return n*factorial(n-1)

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def fractal_pattern(length):
    if length<10:
        return
    turtle.forward(length)
    turtle.left(30)
    fractal_pattern(length-15)
    turtle.right(60)
    fractal_pattern(length-15)
    turtle.left(30)
    turtle.backward(length)

while True:
    print("Menu of Recursive Functions:\n")
    print("1. Calculate the factorial of a number")
    print("2. Find the nth Fibonacci number")
    print("3. Draw a recursive fractal pattern")
    print("4. Exit")
    
    option = int(input("Choose an option by entering the option number(1-4): "))

    if option==1:
        n = int(input("Enter a number to find its factorial: "))
        print(f"The factorial of {n} is {factorial(n)}.\n")
    elif option==2:
        n = int(input("Enter the position of the Fibonacci number: "))
        print(f"The {n}th Fibonacci number is {fibonacci(n)}.\n")
    elif option==3:
        length = int(input("Enter the length of the fractal pattern tree: "))
        turtle.speed("fastest")
        turtle.left(90)
        turtle.penup()
        turtle.goto(0,-200)
        turtle.pendown()
        turtle.color("blue")
        fractal_pattern(length)
        turtle.done()
    elif option==4:
        print("Exiting Program.")
        break
    else:
        print("Invalid option. Please choose (1-4).\n")
    
    