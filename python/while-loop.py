"""
Working with Loops
"""

# Print a welcome message and game rules
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

# Import the 'random' module for generating a random number
import random

# Generate a random number between 1 and 10
number = random.randint(1, 10)

# Initialize a variable to track whether the guess is correct
isGuessRight = False

# Create a loop that continues until the guess is correct
while isGuessRight != True:
    # Ask the user for their guess
    guess = input("Guess a number between 1 and 10: ")

    # Check if the guessed number matches the random number
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
