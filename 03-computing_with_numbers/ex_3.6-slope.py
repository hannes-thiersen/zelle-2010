# File:          slope-progex3.6.py
# Date:          2019-09-26
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 3.6
# Description:
#   Two points in a plane are specified using the coordinates (x1, y1) and (x2,
#   y2). Write a program that calculates the slope of a line through two
#   (non-horizontal) points entered by the user.
#
#       slope = ( y2 - y1 ) / ( x2 - x1 )

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    print("Calculate the slope between two non-horizontal points.")
    x1, y1 = eval(input("Enter first coordinate -> x, y : "))
    x2, y2 = eval(input("Enter second coordinate -> x, y : "))

    slope = ( y2 - y1 ) / ( x2 - x1 )

    print("The slope is", slope)

#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
