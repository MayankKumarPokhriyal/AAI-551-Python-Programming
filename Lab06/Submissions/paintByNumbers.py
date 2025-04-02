# Author: Mayank Kumar Pokhriyal
# Date: 6th March 2025
# Description: Main program to generate ASCII art from a CSV file.

# Import helper functions from separate module
import pbnFunctions


def main():
    # Get valid filename using helper function
    filename = pbnFunctions.getFileName()

    # Process file using helper function
    pbnFunctions.processFile(filename)

    # Notify user of completion
    print("Your image can be found in painting.txt. Enjoy!")


if __name__ == "__main__":
    main()