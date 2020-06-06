# File:            ex_9.13-2D_random_walk.py
# Date:            2019-12-29
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   Suppose you are doing a random walk (see previous problem) on the blocks of
#   a city street. At each "step" you choose to walk one bock (at random)
#   either forward, backward, left or right. In n steps, how far do you expect
#   to be from your starting point? Write a program to help answer this
#   question.

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from random import random
from math import sqrt

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def description():
    print("Simulating 2D random walks and obtaining average displacement.")

#------------------------------------------------------------------------------
def getInputs():
    return eval(input("Enter the amount of steps desired: "))

#------------------------------------------------------------------------------
def simRandomWalks(steps):
    nsims = 10**5
    dispx, dispy = 0, 0
    dist_sum = 0

    for _ in range(nsims):
        x, y = randomWalk2D(steps)
        dispx += x
        dispy += y
        dist_sum += distance(x, y)

    return dispx/nsims, dispy/nsims, dist_sum/nsims

#------------------------------------------------------------------------------
def distance(x, y):
    return sqrt(x**2 + y**2)

#------------------------------------------------------------------------------
def randomWalk2D(steps):
    x = 0
    y = 0
    for _ in range(steps):
        flip = random()
        if flip < .25:
            x += 1
        elif flip < .5:
            x -= 1
        elif flip < .75:
            y += 1
        else:
            y -= 1
    return x, y

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():
    description()
    steps = getInputs()
    ave_dispx, ave_dispy, ave_distance = simRandomWalks(steps)
    print(f"Average displacement after {steps} steps: {ave_dispx:4.2f}, {ave_dispy:4.2f}")
    print(f"Average distance after {steps} steps: {ave_distance:4.2f}")

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
