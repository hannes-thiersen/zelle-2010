# File:            ex_10.9-solidsphere.py
# Date:            2020-04-27
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:        10.9
# Description:
#   Wriet a class to represent the geometric solid sphere. Your class should
#   implement the following methods:
#
#   __init__(self, radius) Creates a sphere having given radius.
#
#   geRadius(self) Returns the radius of this sphere.
#
#   surfaceArea(self) Returns the surface area of the sphere.
#
#   volume(self) Returns the volume of the sphere.
#
#   Use your new class to solve programming exercise 1 from chapter 3.


#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from math import pi as PI

#------------------------------------------------------------------------------
# CLASSES
#------------------------------------------------------------------------------
class SolidSphere():

    def __init__(self, radius):
        self.radius = radius

    def getRadius(self) :
        return self.radius

    def surfaceArea(self):
        return 4 * PI * self.radius**2

    def volume(self):
        return 4/3 * PI * self.radius**3

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():
    print("Calculate the surface area and volume of a sphere.")
    sphere = SolidSphere(eval(input("Enter the radius: ")))
    print("The surface area is:" , sphere.surfaceArea())
    print("The volume is:" , sphere.volume())

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
