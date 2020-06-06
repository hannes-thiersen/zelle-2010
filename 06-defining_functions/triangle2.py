# File:            triangle2.py
# Date:            2019-12-15
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Example:         6.5.1 triangle2.py
# Description:
#   Refactor program that draws a triangle with functions.

#-----------------------------------------------------------------------------
# IMPORTS
#-----------------------------------------------------------------------------
import math
from graphics import *

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def square(x):
    return x*x

#-----------------------------------------------------------------------------
def distance(p1, p2):
    dist = math.sqrt(square(p2.getX() - p1.getX())
            + square(p2.getY() - p1.getY()))
    return dist

#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
def main():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    # Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # Use Polygon object to draw the triangle
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    # Calculate the perimeter of the triangle
    perim = distance(p1,p2) + distance(p3,p2) + distance(p1,p3)
    message.setText(f"The perimeter is : {perim:0.2f}")

    # Wait for another click to exit
    win.getMouse()
    win.close()

#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
