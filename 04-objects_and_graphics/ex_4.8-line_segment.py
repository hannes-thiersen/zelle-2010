# File:          line_segment-progex4.8.py
# Date:          2019-09-29
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 4.8
# Description:
#   Line Segment Information
#   This program allows the user to draw a line segment and then displays some
#   graphical and textual intermation about the line segment.
#
#   Input:
#       Two mouse clicks for end points of the line segment.
#
#   Output:
#       Draw the midpoint of the segment in cyan.
#       Draw the line.
#       Print the length and the slope of the line.
#
#   Formulas:
#       dx = x2 - x1
#       dy = y2 - y1
#       slope = dy/dx
#       length = sqrt(dx**2 + dy**2)

#-----------------------------------------------------------------------------
# IMPORTS
#-----------------------------------------------------------------------------
from math import sqrt
from graphics import *

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    win = GraphWin("Line Segment", 800, 600)
    win.setCoords(0,0, 800, 600)

    instruct = Text(Point(400, 300), "Click two points on screen")
    instruct.draw(win)

    p1 = win.getMouse()
    p1.draw(win)

    p2 = win.getMouse()
    p2.draw(win)

    instruct.undraw()

    Line(p1,p2).draw(win)

    dx = p2.getX() - p1.getX()
    dy = p2.getY() - p1.getY()

    length = sqrt(dx**2 + dy**2)
    print("Line length:", length)
    slope = dy/dx
    print("Line slope:", slope)

    pmid = Circle(Point(p1.getX() + dx/2, p1.getY() + dy/2), 5)
    pmid.setFill("cyan")
    pmid.draw(win)

    try:
        while True:
            win.getMouse()
    except GraphicsError:
        print("", end="")

#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
