# Author: Mayank Kumar Pokhriyal
# Date: 21st Feb 2025
# Description: Calculates the surface area of a square pyramid.

import math

def calcBaseArea(side):
    """Calculate the base area of the square pyramid.
    :param side: Side length of the base.
    :type side: float
    :return: Base area.
    """
    return side ** 2

def calcSideArea(side, height):
    """Calculate the total side area of the square pyramid.
    :param side: Side length of the base.
    :type side: float
    :param height: Height of the pyramid.
    :type height: float
    :return: Total side area.
    """
    return 2 * side * math.sqrt((side ** 2) / 4 + height ** 2)

def prntSurfArea(base_area, side_area):
    """Print the total surface area.
    :param base_area: Base area of the pyramid.
    :type base_area: float
    :param side_area: Total side area of the pyramid.
    :type side_area: float
    :return: None
    """
    total = base_area + side_area
    print(f"The total surface area of the square pyramid is {total} square feet.")

def main():
    side = float(input("Enter the side length of the base of the square pyramid in feet: "))
    height = float(input("Enter the height of the square pyramid in feet: "))
    base_area = calcBaseArea(side)
    print(f"Base surface area of the square pyramid is {base_area} square feet.")
    side_area = calcSideArea(side, height)
    print(f"Total surface area of all four sides of the square pyramid is {side_area} square feet.")
    prntSurfArea(base_area, side_area)

if __name__ == "__main__":
    main()