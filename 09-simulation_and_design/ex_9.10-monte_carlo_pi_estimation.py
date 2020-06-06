# File:            ex_9.10-monte_carlo_pi_estimation.py
# Date:            2019-12-29
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:

#   Monte Carlo techniques can be used to estimate the value of pi. Suppose you
#   have a round dart board that just fits inside of a square cabinet. If you
#   throw darts randomly, the proportion that hit the dart board vs. those that
#   hit the cabinet (in the corners not covered by the board) will be
#   determined by the relative area of the dart board and the cabinet. If n is
#   the total number of darts randomly thrown (that land within the confines of
#   the cabinet), and h is the number that hit the board, it is easy to show
#   that:
#
#           pi ~ 4(h/n)
#
#   Write a program that accepts the number of darts as an input and then
#   performs a simulation to estimate pi. Hint: you can use 2*random() -1 to
#   generate x and y coordinates of a random point inside a 2x2 square centered
#   at (0,0). The point lies inside the inscribed circle if x**2 + y**2 <= 1.

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from random import random

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def description():
    print("Estimating pi with Monte Carlo techniques.")
    print("Dart board in square cabinet")

#------------------------------------------------------------------------------
def getInputs():
    return eval(input("Insert the amount of darts: "))

#------------------------------------------------------------------------------
def simDarts(ndarts):
    """
    Simulating only a quarter of a circle with area: pi*r**2/4. The area of the
    square is then r**2.

    Thus the result is pi/4 = hits/total => pi = 4*hits/total
    """
    hits = 0

    for _ in range(ndarts):
        x, y = random(), random()
        if x**2 + y**2 <= 1:
            hits += 1

    return 4*hits/ndarts

#------------------------------------------------------------------------------
def printResult(estimate):
    print(f"Estimation for pi: {estimate:6.4f}")

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():
    description()
    ndarts = getInputs()
    pi_estimate = simDarts(ndarts)
    printResult(pi_estimate)

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
