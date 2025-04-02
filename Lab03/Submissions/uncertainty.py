# Author: Mayank Kumar Pokhriyal
# Date: 14th Feb 2025
# Description: This program implements a coordinate (position) guessing game where the user has 3 attempts to find the correct position of particle.

import random

# Set number of guesses
guesses = 3

# Generate random coordinates between 1 and 10
x_pos, y_pos = random.randint(1, 10), random.randint(1, 10)


# Loop until the user runs out of guesses
while guesses > 0:
    print(f"The particle is somewhere in this space! You have {guesses} chances to guess it.")

    # Get user input for x and y coordinates
    try:
        x_guess = int(input("What do you think its x coordinate is (1-10)? "))
        y_guess = int(input("What do you think its y coordinate is (1-10)? "))
    except ValueError:
        print("Please enter valid integers for the coordinates!")
        continue

    # Check if the guess is out of bounds
    if not (1 <= x_guess <= 10 and 1 <= y_guess <= 10):
        print(f"No good! ({x_guess},{y_guess}) is outside of the range!")
    elif x_guess == x_pos and y_guess == y_pos:
        print(f"Good guess! ({x_pos},{y_pos}) was the position!")
        break
    else:
        # Provide hints to the user for x and y positions
        if x_guess > x_pos:
            print("Bad luck! The particle's x position is less than your x position!")
        elif x_guess < x_pos:
            print("Bad luck! The particle's x position is greater than your x position!")

        if y_guess > y_pos:
            print("Bad luck! The particle's y position is less than your y position!")
        elif y_guess < y_pos:
            print("Bad luck! The particle's y position is greater than your y position!")

    # Decrement the number of guesses
    guesses -= 1

# If the user runs out of guesses, reveal the correct position
if guesses == 0:
    print(f"Oh no! You ran out of chances. ({x_pos},{y_pos}) was the particle's position!")