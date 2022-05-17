#!/usr/bin/env python3

# Created by: Miguel Santacruz
# Created on: May 2022
# This program finds the volume of a cylinder

import math


def volume(r, h):
    v = math.pi * r**2 * h
    return v


def main():
    # this program calculates volume of a cylinder

    # input
    radius_string = input("The radius is (mm): ")
    height_string = input("The height is (mm): ")

    # process
    try:
        radius = float(radius_string)
        height = float(height_string)
        if radius < 0 or height < 0:
            print("Invalid input")
        else:
            solution = volume(r=radius, h=height)
            print(
                "The volume of a cylinder with a radius of {0}mm and height of {1}mm is {2:.2f}mm³".format(
                    radius, height, solution
                )
            )
    except Exception:
        print("This is not valid input")


if __name__ == "__main__":
    main()
