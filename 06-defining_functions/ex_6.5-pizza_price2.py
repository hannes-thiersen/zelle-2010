# File:            ex_6.5-pizza_price2.py
# Date:            2019-12-16
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:        ex 6.5 (ex 3.2)
# Description:
#   Redo Programming Exercise 2 from Chapter 3. Use two functions -- one to
#   compute the area of a pizza, and one to compute cost per square inch.

#-----------------------------------------------------------------------------
# IMPORTS
#-----------------------------------------------------------------------------
import math

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def area(radius):
    return math.pi * radius**2

def costPerArea(area, cost):
    return cost/area

#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
def main():
    print("Calculate the cost per area for a circular pizza.")
    cost = eval(input("Enter pizza cost: "))
    diameter = eval(input("Enter pizza diameter: "))

    cpa = costPerArea(area(diameter/2), cost)

    print("Pizza cost per area: ", cpa)

#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
