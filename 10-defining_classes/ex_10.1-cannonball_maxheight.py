# File:            ex_10.1-cannonball_maxheight.py
# Date:            2020-03-21
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:        10.1
# Description:
#   Modify the cannonball from the chapter so that it also calculates the
#   maximum height achieved by the cannonball

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from projectile import Projectile

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
# MAIN
#------------------------------------------------------------------------------
def main():
    angle, vel, h0, time = getInputs()
    cball = Projectile(angle, vel, h0)
    maxheight = h0
    while cball.getY() >= 0.0:
        cball.update(time)
        if cball.getY() > maxheight:
            maxheight = cball.getY()
    print("\nDistance traveled: {:0.1f} meters.".format(cball.getX()))
    print("Maximum height: {:0.1f} meters.".format(maxheight))

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
