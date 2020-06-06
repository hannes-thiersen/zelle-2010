# File:            cball2.py
# Date:            2019-12-31
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   Projectile simulation; Top-down design

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from math import sin, cos, radians

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def getInputs():
    a = eval(input("Enter the launce angle (in degrees): "))
    v = eval(input("Enter the initial velocity (in meters/sec): "))
    h = eval(input("Enter the initial height (in meters): "))
    t = eval(input( "Enter the time interval between position calculations: "))
    return a, v, h, t

#------------------------------------------------------------------------------
def getXYComponents(vel, angle):
    theta = radians(angle)
    xvel = vel * cos(theta)
    yvel = vel * sin(theta)
    return xvel, yvel

#------------------------------------------------------------------------------
def updateCannonBall(time, xpos, ypos, xvel, yvel):
    xpos = xpos + time*xvel
    yvel1 = yvel - time*9.8
    ypos = ypos + time*(yvel1 + yvel)/2.0
    yvel = yvel1
    return xpos, ypos, xvel, yvel

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():

    angle, vel, h0, time = getInputs()
    xpos, ypos = 0, h0
    xvel, yvel = getXYComponents(vel, angle)
    while ypos >= 0.0:
        xpos, ypos, xvel, yvel = updateCannonBall(
                time, xpos, ypos, xvel, yvel)
    print("\nDistance traveled: {:0.1f} meters.".format(xpos))

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
