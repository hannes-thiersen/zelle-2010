# File:            ex_10.10-solidcube.py
# Date:            2020-04-27
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:        10.10
# Description:
#   Same as the previous problem, but for a cube. The constructor should accept
#   the length of a side as a parameter.

#------------------------------------------------------------------------------
# CLASSES
#------------------------------------------------------------------------------
class SolidCube():

    def __init__(self, side):
        self.side = side

    def getSideLength(self) :
        return self.side

    def surfaceArea(self):
        return 6 * self.side**2

    def volume(self):
        return self.side**3

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():
    print("Calculate the surface area and volume of a cube.")
    cube = SolidCube(eval(input("Enter the side length: ")))
    print("The surface area is:" , cube.surfaceArea())
    print("The volume is:" , cube.volume())

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
