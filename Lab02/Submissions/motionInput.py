# Author: Mayank Kumar Pokhriyal
# Date: 6th Feb 2025
# Description: This program calculates velocity, average velocity,
# and displacement for an object in motion based on user-input time

# Constants
acceleration = 5.25
initialVelocity = 8.25


# Get user input for time
time = float(input("Please enter the elapsed time: "))

# Calculations
velocity = initialVelocity + acceleration * time
averageVelocity = initialVelocity + 0.5 * acceleration * time
displacement = initialVelocity * time + 0.5 * acceleration * (time ** 2)

# Output results with Blank line after time and aligned "=" signs
'''max string size is 16 characters (average velocity) so we will give 17 spaces
   using f"{'label':<17}". This ensures all "=" signs start at the 18th column'''
print(f"time = {time}\n")                              # Blank line after time
print(f"{'velocity':<17}= {velocity}")                 # Align "=" at position 18
print(f"{'average velocity':<17}= {averageVelocity}")  # Align "=" at position 18
print(f"{'displacement':<17}= {displacement}")         # Align "=" at position 18