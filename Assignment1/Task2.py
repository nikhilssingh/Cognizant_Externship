num1 = 10
num2 = 20
sum = num1 + num2 
diff = num1 - num2
prod = num1 * num2  
quot = num1 / num2

print("The sum of"+" "+str(num1)+" "+"and"+" "+str(num2)+" "+"is"+" "+str(sum))
print("The difference of"+" "+str(num1)+" "+"and"+" "+str(num2)+" "+"is"+" "+str(diff))
print("The product of"+" "+str(num1)+" "+"and"+" "+str(num2)+" "+"is"+" "+str(prod))
print("The quotient of"+" "+str(num1)+" "+"and"+" "+str(num2)+" "+"is"+" "+str(quot))

# The key is to explicitly convert the numbers to strings using str() before concatenating them with other strings.
# This ensures that the concatenation works correctly and avoids any type errors.