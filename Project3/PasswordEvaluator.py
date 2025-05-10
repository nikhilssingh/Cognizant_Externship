password = str(input("Enter a password: "))
contains_upper = any(char.isupper() for char in password)
contains_lower = any(char.islower() for char in password)
contains_digit = any(char.isdigit() for char in password)
contains_special = any(char in "@#$" for char in password)

def format_missing_items(missing):
    if len(missing) == 1:
        return missing[0]
    elif len(missing) == 2:
        return f"{missing[0]} and {missing[1]}"
    else:
        return f"{', '.join(missing[:-1])}, and {missing[-1]}"
    
def score(password):
    score = 0
    if len(password) >= 8:
        score += 2
    if any(char.isupper() for char in password):
        score += 2
    if any(char.islower() for char in password):
        score += 2
    if any(char.isdigit() for char in password):
        score += 2
    if any(char in "@#$" for char in password):
        score += 2
    return score

def score_label(score):
    if score < 4:
        return "Weak"
    elif score < 8:
        return "Moderate"
    else:
        return "Strong"

if len(password) < 8:
    print("Your password needs to be at least 8 characters long.")
else:
    missing = []
    if not contains_upper:
        missing.append("one uppercase letter")
    if not contains_lower:
        missing.append("one lowercase letter")
    if not contains_digit:
        missing.append("one digit")
    if not contains_special:
        missing.append("one special character (@, #, $)")
        
    if missing: 
        print(f"Your password needs at least {format_missing_items(missing)}.")   
    else:
        print("Your password is strong!")
        
    password_score = score(password)
    print(f"Your password score is {password_score} out of 10.")
    print(f"Password strength: {score_label(password_score)}")

# The code above checks the strength of a password based on certain criteria: length, presence of uppercase and lowercase letters, digits, and special characters. It provides feedback on what is missing if the password does not meet the requirements.
