# File:            ex_6.4-summations.py
# Date:            2019-12-16
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:        ex 6.4
# Description:
#   Write definitions for the following two functions:
#
#       `sumN(n)` returns the sum of the first n natural numbers.
#
#       `sumNCubes(n) returns the sum of the cubes of the first n natural
#       numbers.

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def sumN(n):
    return int((n + 1)*n/2)

#------------------------------------------------------------------------------
def sumNCubes(n):
    cubesum = 0
    for i in range(1, n+1):
        cubesum += i**3
    return cubesum

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():
    number = eval(input("Natural number: "))
    print(f"Sum of 1 to {number}: {sumN(number)}")
    print(f"Sum of the cubes of 1 to {number}: {sumNCubes(number)}")

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
