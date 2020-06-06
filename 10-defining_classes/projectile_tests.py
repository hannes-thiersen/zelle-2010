# File:            projectile_tests.py
# Date:            2020-06-04
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   Testing projectile for problems by graphing the trajectories.

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from math import sin, cos, sqrt, pi, radians
from matplotlib import pyplot as plt
from projectile import Projectile

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
class Trajectory():

    def __init__(self, angle, vel, h0, gravity=-9.8):
        self.x0 = 0.0
        self.y0 = h0
        self.vx0 = vel * cos(radians(angle))
        self.vy0 = vel * sin(radians(angle))
        self.gravity = gravity

    def traveltime(self, y=None):
        """ Calculates the trajectory time to a certain value of y. """

        if y:
            square = self.vy0**2 - 4*self.gravity*(self.y0 - y)
            if square > 1:
                tmin = (-v - sqrt(square)) / (4*gravity)
                tmax = (-v + sqrt(square)) / (4*gravity)

            return [ tmin, tmax ]

        return None

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def fire(angle, vel, h0, time):

    cball = Projectile(angle, vel, h0)

    xcoords = [0.]
    ycoords = [h0]

    while cball.getY() >= 0.0:
        cball.update(time)
        xcoords.append(cball.getX())
        ycoords.append(cball.getY())

    plt.plot(xcoords, ycoords, marker=".", label=time/vel)

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():

    # Initial conditions
    angle, vel, h0 = 45.0, 25.0, 2.0

    path = Trajectory(angle, vel, h0)
    print(path.traveltime(y=0.))

    # Time intervals to test
    time = [ t*.1 for t in range(1,6) ]

    plt.figure("Trajectories")

    for deltat in time:
        fire(angle, vel, h0, deltat)

    plt.legend()
    plt.tight_layout()
    plt.show()

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
