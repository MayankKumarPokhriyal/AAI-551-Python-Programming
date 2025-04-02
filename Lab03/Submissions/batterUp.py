# Author: Mayank Kumar Pokhriyal
# Date: 14th Feb 2025
# Description: This program simulates a baseball hit and determines the outcome based on a random distance.

import random

# Generate a random distance between 0 and 450 feet
distance = random.randint(0, 450)

# Determine the outcome based on the distance
if distance > 400:
    print(f"The ball flew {distance} feet and the batter scored a home run! That's one point for our team!")
elif 135 <= distance <= 400:
    print(f"The ball flew {distance} feet and the batter made it to third base!")
elif 10 <= distance <= 134:
    print(f"The ball flew {distance} feet and the batter made it to second base!")
elif 1 <= distance <= 9:
    print(f"The ball flew {distance} feet because the batter bunted, and made it to first base!")
else:
    print("The batter has made a strike! Oh no!")