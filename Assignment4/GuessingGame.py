import random
number_to_guess = random.randint(1, 100)
count = 0
guess = None

while guess!=number_to_guess:
    if count<10:
        guess = int(input("Guess a number between 1 and 100: "))
        count += 1
        if guess<number_to_guess:
            print("Too low! Try again.")
        elif guess>number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {count} attempts!")
            break
    else:
        print("Game over! Better luck next time.")
        break
# The code above implements a simple guessing game where the user has to guess a randomly generated number between 1 and 100. It provides feedback on whether the guess is too high or too low until the correct number is guessed.
