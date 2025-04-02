# Author: Mayank Kumar Pokhriyal
# Date: 14th Feb 2025
# Description: This program calculates the sum of all odd numbers between two randomly generated numbers.

import random

# Generate two random numbers: first between 1-10, second between 11-20
num1 = random.randint(1, 10)
num2 = random.randint(11, 20)

# Ensure num1 is smaller than second_num
if num1 > num2:
    num1 = num2
    num2 = num1

# Adjust range to start from the next odd number if first_num is even
if num1 % 2 == 0:
    num1 += 1

# Calculate the sum of odd numbers in the range
odd_sum = 0
for num in range(num1, num2 + 1, 2):
    odd_sum += num
# Display results
print(f"The first random number was {num1}, the second random number was {num2}, and the sum is {odd_sum}.")