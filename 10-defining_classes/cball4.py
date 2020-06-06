# File:            cball4.py
# Date:            2020-03-20
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   Flight of a cannon ball showing the use of modules

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
    while cball.getY() >= 0.0:
        cball.update(time)
    print("\nDistance traveled: {:0.1f} meters.".format(cball.getX()))


#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
