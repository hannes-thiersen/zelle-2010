# File:            ex_8.4-syracuse_sequence.py
# Date:            2019-12-20
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   The Syracuse (also called Collatz or Hailstone) sequence is generated by
#   starting with a natural number and repeatedly applying te following
#   function until reaching 1:
#
#       syr(x) =  / x/2      if x is even
#                 \ 3x + 1   if x is odd
#
#   For example, the Syracuse sequence starting with 5 is: 5, 16, 8, 4, 2, 1.
#   It is an open question in mathematics whether this sequence will always go
#   to 1 for every possible starting value.
#
#   Write a program that gets a starting value from the user and then prints
#   the Syracuse sequences for that starting value.

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def getStart():
    start = input("Insert starting number: ")
    while not start:
        start = input("Insert starting number: ")
    return eval(start)

#------------------------------------------------------------------------------
def syrSequence(number):
    while number != 1:
        print(f"{number}, ", end="")
        if number%2:
            number = number*3 + 1
        else:
            number//=2

    print(f"{number}.")

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():

    start = getStart()
    syrSequence(start)


#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
