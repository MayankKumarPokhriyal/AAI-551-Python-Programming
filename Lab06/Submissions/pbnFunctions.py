# Author: Mayank Kumar Pokhriyal
# Date: 6th March 2025
# Description: Helper functions for converting numbers to ASCII art.

import os


def getFileName():
    """Get and validate a filename from the user."""
    while True:
        filename = input("Please input file you wish to have painted: ")
        if os.path.exists(filename):
            return filename  # Valid file found
        print(f"{filename} does not exist!", end=' ')  # Reprompt


def convertLine(line):
    """Convert a comma-separated number string to symbols."""
    # Symbol mapping dictionary
    symbols = {
        '1': ' ',  # Space
        '2': ',',  # Comma
        '3': '_',  # Underscore
        '4': '(',  # Left parenthesis
        '5': 'O',  # Capital O
        '6': ')',  # Right parenthesis
        '7': '-',  # Hyphen
        '8': '"'  # Double quote
    }

    # Process each number in the line
    cleaned_line = line.strip()  # Remove whitespace/newlines
    numbers = cleaned_line.split(',')  # Split into list
    return ''.join([symbols.get(num, '?') for num in numbers])  # Build symbol string


def processFile(filename):
    """Process input file and generate ASCII art output."""
    # Open both files using context managers
    with open(filename, 'r') as infile, open('painting.txt', 'w') as outfile:
        # Process each line of input
        for line in infile:
            converted = convertLine(line)  # Convert numbers to symbols
            outfile.write(converted + '\n')  # Write to output file