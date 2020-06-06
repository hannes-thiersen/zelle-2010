# File:            ex_9.12-1D_random_walk.py
# Date:            2019-12-29
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   A random walk is a particular kind of probabilistic simulation that models
#   certain statistical systems such as the Brownian motion of molecules. You
#   can think of a one-dimensional random walk in terms of coin flipping.
#   Suppose you are standing on a very long straight sidewalk that extends both
#   in front of and behind you. You flip a coin. If it comes up heads, you take
#   a step forward; tails means to take a step backward.
#
#   Suppose you take a random walk on n steps. On average, how many steps away
#   from the starting pint will you end up? Write a program to help you
#   investigate this question.

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from random import random

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def description():
    print("Simulating 1D random walks and obtaining average displacement.")

#------------------------------------------------------------------------------
def getInputs():
    return eval(input("Enter the amount of steps desired: "))

#------------------------------------------------------------------------------
def simRandomWalks(steps):
    nsims = 100000
    disp_sum = 0
    dist_sum = 0

    for _ in range(nsims):
        displacement = randomWalk(steps)
        disp_sum += displacement
        dist_sum += abs(displacement)

    return disp_sum/nsims, dist_sum/nsims

#------------------------------------------------------------------------------
def randomWalk(steps):
    dis = 0
    for _ in range(steps):
        if random() < .5:
            dis += 1
        else:
            dis -= 1
    return dis

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():
    description()
    steps = getInputs()
    ave_displacement, ave_distance = simRandomWalks(steps)
    print(f"Average displacement after {steps} steps: {ave_displacement:4.2f}")
    print(f"Average distance after {steps} steps: {ave_distance:4.2f}")

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
