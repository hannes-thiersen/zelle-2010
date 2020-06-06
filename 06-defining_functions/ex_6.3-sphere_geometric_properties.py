# File:            ex_6.3-sphere_geometric_properties.py
# Date:            2019-12-15
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:         ex 6.3
# Description:
#   Write definitions for these functions:
#
#       `sphereArea(radius)` Returns the surface area of a sphere having the
#       given radius
#
#       `sphereVolume(radius)` Returns the volume of a sphere having the
#       given radius.
#
#   Use your functions to solve Programming Exercise 1 from Chapter 3.

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
import math

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def sphereArea(radius):
    return 4*math.pi*radius**2

def sphereVolume(radius):
    return 4/3*math.pi*radius**3

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():
    radius = eval(input("Sphere radius: "))
    print(f"Sphere surface area = {sphereArea(radius)}")
    print(f"Sphere volume = {sphereVolume(radius)}")

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
