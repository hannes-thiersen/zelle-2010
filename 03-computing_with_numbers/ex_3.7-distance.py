# File:          distance-progex3.7.py
# Date:          2019-09-26
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 3.7
# Description:
#   Write a program that accepts two points (see previous problem) and
#   determines the distance between them.

#-----------------------------------------------------------------------------
# IMORTS
#-----------------------------------------------------------------------------
import math

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    print("Calculate the distance between two points.")
    x1, y1 = eval(input("Enter first coordinate -> x, y : "))
    x2, y2 = eval(input("Enter second coordinate -> x, y : "))

    distance = math.sqrt( (x1 - x2)**2 + (y1 - y2)**2 )

    print("The distance between the points are:", distance)

#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
