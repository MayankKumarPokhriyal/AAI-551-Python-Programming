# Author: Mayank Kumar Pokhriyal
# Date: 27th Feb 2025
# Description: This program simulates an 8x8 grid of cosmic ray muon detectors (CRMDs),
#              identifies the highest and lowest capture rates, and displays the results.


import random

DIMENSION = 8

# Initialize the 8x8 grid with zeros
grid = [[0 for _ in range(DIMENSION)] for _ in range(DIMENSION)]

# Fill the grid with random values between 0 and 500 inclusive
for i in range(DIMENSION):
    for j in range(DIMENSION):
        grid[i][j] = random.randint(0, 500)

# Variables to track the highest and lowest capture rates and their positions
max_rate = -1
min_rate = 501
max_x, max_y = 0, 0
min_x, min_y = 0, 0

# Iterate through the grid to find the highest and lowest values
for i in range(DIMENSION):
    for j in range(DIMENSION):
        current = grid[i][j]
        if current > max_rate:
            max_rate = current
            max_x, max_y = i, j
        if current < min_rate:
            min_rate = current
            min_x, min_y = i, j

# Output the results with human-readable coordinates (1-based)
print(f"The highest capture rate was {max_rate} at location {max_x + 1},{max_y + 1}.")
print(f"The lowest capture rate was {min_rate} at location {min_x + 1},{min_y + 1}.")
print("The map looks like the following:")
for row in grid:
    # Format each number to 3-character width for alignment
    print(' '.join(f"{num:3}" for num in row))