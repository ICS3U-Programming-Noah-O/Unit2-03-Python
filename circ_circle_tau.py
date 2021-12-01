#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Nov. 30, 2021
# This program calculates the area and perimeter of a circle with
# radius that is inputted by the user.


import constants


def main():
    # This function asks for the radius and then calculates
    # the area and perimeter.
    print("This program calculates the area and perimeter of a circle.")
    # Input
    radius = int(input("Enter radius of your circle: "))
    units = (input("Enter the units that you're using: "))

    # Process
    perimeter = constants.TAU * radius
    area = ((constants.TAU / 2) * radius ** 2)

    # Output
    print(" ")
    print("The area is {}".format(area) + "{}^2".format(units) +
          " and the perimeter is {}".format(perimeter) + "{}".format(units))


if __name__ == "__main__":
    main()
