# File:          pizza_price.py
# Date:          2019-09-26
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 3.2
# Description:
#   Write a program that calculates the cost per square inch of a circular
#   pizza given its diameter and price. The formula for area is:
#
#       A = pi * radius**2

#-----------------------------------------------------------------------------
# IMPORTS
#-----------------------------------------------------------------------------
import math

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    print("Calculate the cost per area for a circular pizza.")
    cost = eval(input("Enter pizza cost: "))
    diameter = eval(input("Enter pizza diameter: "))

    cpa = (math.pi * (diameter/2)**2 ) / cost

    print("Pizza cost per area: ", cpa)

#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
