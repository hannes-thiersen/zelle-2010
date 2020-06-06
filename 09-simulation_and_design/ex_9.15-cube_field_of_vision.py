# File:            ex_9.15-cube_field_of_vision.py
# Date:            2019-12-29
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   (Advanced) Here is a puzzle problem that can be solved with either some
#   fancy analytic geometry (calculus) or a (relatively) simple simulation.
#
#   Suppose you are located at the exact center of a cube. If you could look
#   all around you in every direction, each wall of the cube would occupy 1/6
#   of your field of vision. Suppose you move toward one of the walls so that
#   you are now half-way between it and the center of the cube. What fraction
#   of your field of vision is now taken up by the closest wall? Hint: use
#   Monte Carlo simulation that repeatedly "looks" in a random direction and
#   counts how many times it sees the wall.

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from random import random
from math import pi, cos, sin

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def description():
    print("Monte Carlo simulation to calculate the field of vision of the")
    print("closet side of a cube when located half-way between that side")
    print("and the center of the cube.\n")

#------------------------------------------------------------------------------
def randomDirectionSim(samples):
    hits = 0
    for _ in range(samples):
        vx, vy, vz = randomDirection()
        if nearestFace(vx, vy, vz):
            hits += 1
    return hits

#------------------------------------------------------------------------------
def randomDirection():
        theta = 2*pi * random()
        phi = pi * random()
        return cos(theta)*sin(phi), sin(theta)*sin(phi), cos(phi)

#------------------------------------------------------------------------------
def nearestFace(vx, vy, vz):
    # cube coordinates:
    #   x = [-0.5, 1.5]
    #   y = [-1.0, 1.0]
    #   z = [-1.0, 1.0]
    xnearest = -0.5
    ymin, ymax = -1.0, 1.0
    zmin, zmax = -1.0, 1.0
    k = xnearest/vx
    if k > 0 and (ymin <= k*vy <= ymax or zmin <= k*vz <= zmax):
        return True
    return False

#------------------------------------------------------------------------------
def summary(hits, samples):
    print(f"Nearest face estimated field of view: {hits/samples:7.5}")

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():
    description()
    samples = eval(input("Insert the amount of samples: ") or "10**5")
    hits = randomDirectionSim(samples)
    summary(hits, samples)

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
