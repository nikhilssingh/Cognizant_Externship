n = int(input("Enter a number for which factorial should be calculated: "))

def factorial(n):
    if n==0 or n==1:
    # base case for 0 and 1
        return 1
    else:
        return n*factorial(n-1)

print(factorial(n))
        
