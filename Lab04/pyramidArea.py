# Author: Your name
# Date: Today's date
# Description: A small description in your own words that describes what the program does.
# Any additional information required for the program to execute should also be provided.

# function definitions
def calcBaseArea(side):
    return side ** 2

# add your function definition for calcSideArea here

# add your function definition for prntSurfArea here

def main():
    side = float(input("Enter the side length of the base of the square pyramid in feet: "))

    height = float(input("Enter the height of the square pyramid in feet: "))

    base_area = calcBaseArea(side)
    print(f"Base surface area of the square pyramid is {base_area} square feet.")

    # add your function to calculate the side area and assign
    # the result to side_area, then print the result

    # add your function call to print the total surface area


if __name__ == "__main__":
    main()