# File:            cball1.py
# Date:            2019-12-31
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   Projectile simulation; No design techniques.

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from math import sin, cos, radians

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():
    angle = eval(input("Enter the launce angle (in degrees): "))
    vel = eval(input("Enter the initial velocity (in meters/sec): "))
    h0 = eval(input("Enter the initial height (in meters): "))
    time = eval(input(
        "Enter the time interval between position calculations: "))

    # convert angle to radians
    theta = radians(angle)

    # set the initial position and velocities in x and y directions
    xpos = 0
    ypos = h0
    xvel = vel * cos(theta)
    yvel = vel * sin(theta)

    # loop until the ball hits the ground
    while ypos >= 0.0:
        # calculate position and velocity in time seconds
        xpos = xpos + time*xvel
        yvel1 = yvel - time*9.8
        ypos = ypos + time*(yvel1 + yvel)/2.0
        yvel = yvel1

    print("\nDistance traveled: {:0.1f} meters.".format(xpos))

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
