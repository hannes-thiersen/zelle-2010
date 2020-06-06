# File:          chaos_algebra-progex1.6.py
# Date:          2019-09-20
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 1.6
# Description:
#   The calculation performed in the `chaos` program can be written in a
#   number of ways that are algebraically equivalent. Write a version of the
#   program for each of the following ways of doing the computation. Have your
#   modified programs print out 100 iterations of the function and compare
#   the results when run on the same input.
#
#       (a) 3.9 * x * (1 - x)
#       (b) 3.9 * (x - x*x)
#       (c) 3.9*x - 3.9*x*x
#
#   Explain the results of this experiment. Hint: Remember that numbers are not
#   exactly represented on a computer.
#
# Explanation:
#   The evaluation of each part of the different algebraic expressions
#   represent different number values. Since numbers cannot be represented
#   exactly each of these numbers are off by some small amount which is
#   different for each value. Since the chaotic function is extremely sensitive
#   to such small changes we can conclude that the small differences from the
#   exact numbers creates the significant difference:

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def chaos1(x):
    """Algebraic expression 1."""
    return 3.9*x * (1 - x)

#------------------------------------------------------------------------------
def chaos2(x):
    """Algebraic expression 2."""
    return 3.9 * (x - x*x)

#------------------------------------------------------------------------------
def chaos3(x):
    """Algebraic expression 3."""
    return 3.9*x - 3.9*x*x

#------------------------------------------------------------------------------
def main():
    print("This program illustrates a chaotic function")
    original = eval(input("Enter a number between 0 and 1: "))

    x = original
    for i in range(100):
        x = chaos1(x)
    print(x)

    x = original
    for i in range(100):
        x = chaos2(x)
    print(x)

    x = original
    for i in range(100):
        x = chaos3(x)
    print(x)

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
if __name__ == "__main__":

    main()
