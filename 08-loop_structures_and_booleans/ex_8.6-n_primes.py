# File:            ex_8.6-n_primes.py
# Date:            2019-12-20
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   Modify the previous program to find every prime number less than or equal
#   to n.

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
# Function isPrime in previous exercise not used here since it is inefficient
# to check for factors of each number up to N in this case.
# Here we have the benefit of saving known primes to an array. Given this, we
# only have to check the evaluated number against the known primes less than or
# equal to its root. If none of these primes can evenly divide the number it is
# itself a prime number and added to the list of primes.
def findPrimes(num):
    if num < 2:
        return []
    else:
        primes = []

    for i in range(2,num+1):
        status = True
        root = int(sqrt(i)) + 1
        primeslice = [ p for p in primes if p < root ]
        for prime in primeslice:
            if i%prime == 0:
                status = False
                break
        if status:
            primes.append(i)

    return primes

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():
    number = getValue()
    primes = findPrimes(number)
    print(primes)
    print(f"{len(primes)} found.")

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
