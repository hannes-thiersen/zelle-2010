# File:            cball3.py
# Date:            2019-12-31
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   Projectile simulation; Object-oriented design

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from math import sin, cos, radians

#------------------------------------------------------------------------------
# CLASSES
#------------------------------------------------------------------------------
class Projectile:

    def __init__(self, angle, velocity, height):
        self.xpos = 0.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def update(self, time):
        self.xpos = self.xpos + time*self.xvel
        self.yvel1 = self.yvel - time*9.8
        self.ypos = self.ypos + time*(self.yvel1 + self.yvel)/2.0
        self.yvel = self.yvel1

    def getX(self):
        return self.xpos

    def getY(self):
        return self.ypos

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
