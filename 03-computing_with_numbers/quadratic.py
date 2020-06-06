# File:          quadratic.py
# Date:          2019-09-26
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Example:       quadratic.py
# Description:
#   A program that computes the real roots of a quadratic equation. Illustrates
#   use of the math library.
#   Note: this program crashes if the equation has no real roots.

#-----------------------------------------------------------------------------
# imports
#-----------------------------------------------------------------------------
import math

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    print("This program finds the real solutions to a quadratic")
    print()

    a, b, c = eval(input("Please enter the coefficents (a, b, c): "))

    discRoot = math.sqrt(b*b - 4*a*c)
    root1 = (-b + discRoot) / (2*a)
    root2 = (-b - discRoot) / (2*a)

    print()
    print("The solutions are:", root1, root2)

#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
