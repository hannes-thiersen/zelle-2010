# File:            ex_6.6-triangle3.py
# Date:            2019-12-15
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:        ex 6.6
# Description:
#   Write a function that computes the area of a triangle given the length of
#   its three sides as paramters (see Programming Exercise 9 from Chapter 3).
#   Use your function to augment `triangle2.py` so that it also displays the
#   area of the triangle.

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
def triarea(a, b, c):
    """Returns area of triangle area with side lengths a,b and c."""
    s = (a + b + c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

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
    a,b,c = distance(p1,p2) , distance(p3,p2) , distance(p1,p3)
    perim = a + b + c
    message.setText(f"The perimeter is: {perim:0.2f}")
    area_message = Text(Point(5, 9.5), f"The area is: {triarea(a,b,c):0.2f}")
    area_message.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()

#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
