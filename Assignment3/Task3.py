str3 = str(input("Enter a word: "))
if(str3[::-1] == str3):
    print(f"Yes, \'{str3}\' is a palindrome!")
else:
    print(f"No, \'{str3}\' is not a palindrome!")
# The code above checks if the input string is a palindrome by comparing it with its reverse. If they are the same, it confirms that the string is a palindrome; otherwise, it states that it is not.

