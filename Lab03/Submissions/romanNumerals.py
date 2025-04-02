# Author: Mayank Kumar Pokhriyal
# Date: 14th Feb 2025
# Description: This program converts a number (1-9) into its corresponding Roman number using Unicode values.

# user input
num = int(input("Please enter a number between 1 and 9 to convert to a roman numeral: "))

# Dictionary for mapping numbers to Roman numbers
roman_dict = {1: "\u2160", 2: "\u2161", 3: "\u2162", 4: "\u2163", 5: "\u2164", 6: "\u2165", 7: "\u2166", 8: "\u2167", 9: "\u2168"}

# Check if the number is within range and display the corresponding Roman number
if 1 <= num <= 9:
    print(f"Your roman numeral is: {roman_dict[num]}")
else:
    print(f"{num} is outside the allowed range of 1-9.")