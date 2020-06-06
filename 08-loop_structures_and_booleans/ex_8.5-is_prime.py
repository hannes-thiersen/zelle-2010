# File:            ex_8.5-is_prime.py
# Date:            2019-12-20
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   A positive whole number n > 2 is prime if no number between 2 and sqrt(n)
#   (inclusive) evenly divides n. Write a program that accepts a vlaue of n as
#   input and determins if the vlaue is prime. If n is not prime, your program
#   should quit as soon as it finds a value that evenly divides n.

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from math import sqrt

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def getValue():
    return eval(input("Insert a whole number: "))

#------------------------------------------------------------------------------
def isPrime(num):
    if num < 2:
        return False

    root = int(sqrt(num))

    for factor in range(2,root + 1):
        if not num%factor:
            return False
    return True

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():
    number = getValue()
    if isPrime(number):
        print(f"{number} is prime.")
    else:
        print(f"{number} is not prime.")

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
