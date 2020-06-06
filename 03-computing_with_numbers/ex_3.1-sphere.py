# File:          sphere-progex3.1.py
# Date:          2019-09-26
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 3.1
# Description:
#   Write a program to calculate the volume and surface area of a sphere from
#   its radius, given as input. Here are some formulas that might be useful:
#
#       V = 4/3 * pi * radius**3
#       A = 4 * pi * radius**2

#-----------------------------------------------------------------------------
# IMPORTS
#-----------------------------------------------------------------------------
import math

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    print("Calculate the surface area and volume of a sphere.")
    radius = eval(input("Enter the radius: "))

    print("The surface area is:" , 4 * math.pi * radius**2 )
    print("The volume is:" , 4/3 * math.pi * radius**3 )

#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
