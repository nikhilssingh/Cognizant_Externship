age = int(input("How old are you? "))
x = str(18 - age)
if age >= 18:
    print("Congratulations! You are eligible to vote. Go make a difference!")
elif age < 0:
    print("Age cannot be negative! Enter a valid age.")
else:
    print("Oops! You’re not eligible yet. But hey, only"+" "+x+" "+"more years to go!")
# The code above checks if the input age is 18 or older to determine voting eligibility. It also checks for negative age input and provides appropriate messages.