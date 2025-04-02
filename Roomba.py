# Author: Mayank Kumar Pokhriyal
# Date: 14th Feb 2025
# Description: This program finds and clean dirt a random position in a room 10 X 10

import random

# Initialize Roomba's starting position
x, y = 0, 0
print("Roomba starts cleaning.")

# Randomly place the dirt, ensuring it's not at (0,0)
dirt_x, dirt_y = random.randint(0, 9), random.randint(0, 9)
while dirt_x == 0 and dirt_y == 0:
    dirt_x, dirt_y = random.randint(0, 9), random.randint(0, 9)

# Movement direction: start by moving right
direction = 'right'

# Main cleaning loop
while True:
    # Output current position
    print(f"Roomba is at ({x}, {y})")

    # Check if dirt is found
    if x == dirt_x and y == dirt_y:
        print(f"Dirt cleaned at ({x}, {y}).")
        break

    # Move based on direction
    if direction == 'right':
        x += 1
        if x == 10:  # Hit the right wall
            x -= 1
            y += 1
            direction = 'left'
    else:
        x -= 1
        if x == -1:  # Hit the left wall
            x += 1
            y += 1
            direction = 'right'

    # Ensure Roomba stays within the grid
    if y == 10:
        y -= 1
        break  # Entire grid covered, exit loop

# Return to docking station
print("Returning to docking station.")
while x > 0 or y > 0:
    if x > 0:
        x -= 1
    if y > 0:
        y -= 1
    print(f"Roomba is at ({x}, {y})")

print("Roomba has returned to the docking station.")