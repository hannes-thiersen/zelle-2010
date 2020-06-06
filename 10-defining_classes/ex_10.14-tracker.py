# File:            ex_10.14-tracker.py
# Date:            2020-06-04
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:        10.14
# Description:
#   Create a Tracker class that displays a circle in a graphics window to show
#   the current location of an object. Here is a quick specification of the
#   class:
#
#   class Tracker():
#
#       def __init__(self, window, objToTrack):
#           """
#           window is a graphWin and objToTrack is an object whose position is
#           to # be shown in the window. objToTrack is an object that has
#           getX() and getY() methods that reposrt its current position.
#
#           Creates a Tracker object and draws a circle in window at the
#           current position of objToTrack.
#           """
#
#       def update():
#           """
#           Moves the circle in the window to the current position of the
#           object being tracked.
#           """
#
#   Use your new Tracker class in conjunction withth Projectile class to write
#   a program that graphically depicts the flight of a cannonball.

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from graphics import *
from projectile import Projectile
from time import sleep

#------------------------------------------------------------------------------
# CLASSES
#------------------------------------------------------------------------------
class Tracker():

    def __init__(self, window, objToTrack):
        """
        window is a graphWin and objToTrack is an object whose position is
        to # be shown in the window. objToTrack is an object that has
        getX() and getY() methods that reposrt its current position.

        Creates a Tracker object and draws a circle in window at the
        current position of objToTrack.
        """
        self.window = window
        self.objToTrack = objToTrack
        self.circle = Circle(
                Point(
                    self.objToTrack.getX(),
                    self.objToTrack.getY()),
                radius=10.0)
        self.circle.draw(self.window)


    def update(self):
        """
        Moves the circle in the window to the current position of the
        object being tracked.
        """
        self.circle.move(
                self.objToTrack.getX(),
                self.objToTrack.getY())

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

    # Setting up the cannonball
    #angle, vel, h0, time = getInputs()
    angle, vel, h0, time = 45.0, 25.0, 2.0, 0.5
    cball = Projectile(angle, vel, h0)

    # Setting up the window
    wind = GraphWin("Cannonball Animation", width=1000, height=800)
    wind.setCoords(0, 0, 300, 240)
    sprite = Tracker(wind, cball)

    wind.getMouse()

    while cball.getY() >= 0.0:
        cball.update(time)
        sleep(time)
        sprite.update()

    wind.getMouse()

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
