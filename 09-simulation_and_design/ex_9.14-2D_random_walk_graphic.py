# File:            ex_9.14-2D_random_walk_graphic.py
# Date:            2019-12-29
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   Write a graphical program to trace a random walk (see previous two
#   problems) in two dimensions. In this simulation you should allow the step
#   to be taken in any direction. You can generate a random directions as an
#   angle of the x axis.
#
#       angle = random() * 2 * math.pi
#
#   The new x and y positions are then given by these formulas:
#
#       x = x + cos(angle)
#       y = y + sin(angle)
#
#   The program should take the number of steps as an input. Start your walker
#   at the center of a 100x100 grid and draw a line that traces the walk as it
#   progresses.

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from time import sleep
from random import random
from math import sqrt, pi as PI, cos, sin
from graphics import *

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def description():
    print("Graphic simulating of a 2D random walk.")
    print("The each step the walker walks 1 unit in a random direction")
    print()

#------------------------------------------------------------------------------
def getInputs():
    return eval(input("Enter the amount of steps desired: "))

#------------------------------------------------------------------------------
def createGraphicWindow(size):
    side_length = 800
    win = GraphWin("2D Random Walk", side_length, side_length)
    win.setCoords(-size, -size, size, size)
    return win

#------------------------------------------------------------------------------
def randomWalk2DGraphic(win, steps, pause):
    pos0 = Point(0, 0)
    for _ in range(steps):
        angle = 2*PI * random()
        pos1 = Point(
                pos0.getX() + cos(angle),
                pos0.getY() + sin(angle))
        Line(pos1, pos0).draw(win)
        pos0 = pos1
        win.update()
        #sleep(pause)

#------------------------------------------------------------------------------
def halt(win):
    win.getMouse()

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():
    description()
    steps = getInputs()
    pause = 5.0/steps # pause before each update
    window = createGraphicWindow(sqrt(steps))
    randomWalk2DGraphic(window, steps, pause)
    halt(window)

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
