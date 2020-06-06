# File:            ex_8.7-goldbach_conjecture.py
# Date:            2019-12-20
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   The Goldbach conjecture asserts that every even number is the nus of two
#   prime numbers. Write a program that gets a number from the user, checks to
#   make sure that it is even, and then finds two prime numbers that add up to
#   the number.

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from math import sqrt

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def getValue():
    return eval(input("Insert any even number: "))

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
def findPrimes(num):
    if num < 2:
        return []
    else:
        primes = []

    for i in range(2,num+1):
        status = True
        for prime in primes:
            if i%prime == 0:
                status = False
                break
        if status:
            primes.append(i)

    return primes

#------------------------------------------------------------------------------
def checkEven(num):
    if num%2:
        print("Number not even. Using {num + 1} instead.")
        return num + 1
    return num

#------------------------------------------------------------------------------
def findPrimeSum(num):
    primes = findPrimes(num)

    for i in primes:
        for j in primes:
            if i + j == num:
                return [ i , j ]

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():
    number = getValue()
    number = checkEven(number)
    primes = findPrimeSum(number)
    print(primes)

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
