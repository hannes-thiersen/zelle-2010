# File:            ex_7.17-bouncing_circle.py
# Date:            2019-12-19
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   Write a program to animate a circle bouncing around a window. The basic
#   idea is to start the circle somwhere in the interior of the window. Use
#   variable `dx` and `dy` (both initialised to 1) to control the movement of
#   the circle. Use a large counted loop (say 1e4 iterations), and each time
#   through the loop move the circle using `dx` and `dy`. When the x-value of
#   the center of the circle gets too high (it hist the edge), change dx to -1.
#   When it gets to low, change `dx` back to 1. Use a similar approach for
#   `dy`.
#
#   Note: Your animation will probably run too fast. You can slow it down by
#   using `sleep` function from the `time` library module.

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from graphics import *
from time import sleep

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():

    width = 800
    height = 600
    win = GraphWin("Bouncing Ball", width, height)

    circle_radius = 40

    cx = 400
    dx = 1
    cy = 300
    dy = 1

    circle = Circle(Point(cx, cy), circle_radius)
    circle.setFill("red")
    circle.draw(win)

    for _ in range(10000):
        sleep(0.001)
        cx += dx
        cy += dy

        if cx == width - circle_radius or cx == circle_radius:
            dx *= -1
        if cy == height - circle_radius or cy == circle_radius:
            dy *= -1

        circle.move(dx, dy)

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
