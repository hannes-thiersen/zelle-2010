# File:          triangle_area-progex3.9.py
# Date:          2019-09-26
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog 3.9
# Description:
#   Write a program to calculate the area of a triangle given the length of its
#   three sides a, b, and c using these formulas:
#
#       s = (a + b + c)/2
#
#       A = sqrt(s*(s-a)*(s-b)*(s-c))

#-----------------------------------------------------------------------------
# IMPORTS
#-----------------------------------------------------------------------------
import math

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    print("Calculate the area of a triangle.")
    a, b, c = eval(input("Enter triangle side lenghts comma separated: "))

    s = (a + b + c)/2
    A = math.sqrt(s*(s-a)*(s-b)*(s-c))

    print("The triangle area is", A)

#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
