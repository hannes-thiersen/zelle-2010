# File:            ex_8.8-greatest_common_divisor.py
# Date:            2019-12-20
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   The greatest common divisor (GCD) of two values can be computed using
#   Euclid's algorithm. Starting with the values m and n, we repeatedly apply
#   the formula: n,m - m, n%m until m is 0. At that point n is the GCD of the
#   original m and n. Write a program that finds the GCD of tow numbers using
#   this algorithm.

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def getValues():
    return eval(input("Insert two whole numbers [m, n]: "))

def GCD(a, b):
    while b != 0:
        a, b = b, a%b

    return a

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():

    m, n = getValues()
    gcd = GCD(m, n)
    print(f"The greatest common divisor of {m} and {n} is {gcd}")

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
