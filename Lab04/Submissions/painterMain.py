# Author: Mayank Kumar Pokhriyal
# Date: 21st Feb 2025
# Description: Main file ASCII Art Printer with Customizable Borders.

from painterFuncs import *

def main():
    """Main program controller"""
    choice, border = intro()

    if choice == 1:
        sailingShip(border)
    elif choice == 2:
        sleepingCat(border)
    elif choice == 3:
        fish(border)
    elif choice == 4:
        rabbit(border)
    else:
        blank(border)
        print("\nError: Invalid selection! Art not found.")
        exit(-1)

    print("We hope you enjoy your art!")


if __name__ == "__main__":
    main()