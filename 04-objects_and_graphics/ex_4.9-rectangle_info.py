# File:          rectangle_info-progex4.9.py
# Date:          2019-09-29
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 4.9
# Description:
#   Rectangle Information.
#   This program displays information about a rectangle drawn by the user.
#
#   Input:
#       Two mouse clicks for the opposite corners of a rectangle.
#
#   Output:
#       Draw the rectangle.
#       Print the perimeter and area of the rectangle.
#
#   Formulas:
#       area = length * width
#       perimeter = 2* (length + width)

#-----------------------------------------------------------------------------
# IMPORTS
#-----------------------------------------------------------------------------
from graphics import *

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    win = GraphWin("Rectangle Information", 800, 600)
    win.setCoords(0,0, 800,600)

    instruct = Text(Point(400, 300), "Click two points on screen")
    instruct.draw(win)

    p1 = win.getMouse()
    p1.draw(win)

    p2 = win.getMouse()
    p1.undraw()

    instruct.undraw()

    Rectangle(p1, p2).draw(win)

    length = p2.getX() - p1.getX()
    width = p2.getY() - p1.getY()

    print("Rectangle area:", length*width)
    print("Rectangle perimeter:", 2*(length + width))

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
