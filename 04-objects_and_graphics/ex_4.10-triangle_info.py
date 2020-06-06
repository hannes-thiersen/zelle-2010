# File:          triangle_info-progex4.10.py
# Date:          2019-09-29
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 4.10
# Description:
#   Same as the previous problem, but with three clicks for the vertices of a
#   triangle.
#
#   Formulas:
#       For perimeter , see length from line problem.
#       `area = sqrt(s*(s-a)(s-b)(s-c))` where `a`, `b` and `c` are the lengths
#       of the sides and `s = (a+b+c)/2`

#-----------------------------------------------------------------------------
# imports
#-----------------------------------------------------------------------------
from math import sqrt
from graphics import *
#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    win = GraphWin("Rectangle Information", 800, 600)
    win.setCoords(0,0, 800,600)

    instruct = Text(Point(400, 300), "Click three points on screen")
    instruct.draw(win)

    p1 = win.getMouse()
    p1.draw(win)

    p2 = win.getMouse()
    p2.draw(win)

    p3 = win.getMouse()
    p1.undraw()
    p2.undraw()

    instruct.undraw()

    Polygon([p1, p2, p3]).draw(win)

    side_a = sqrt((p1.getX() - p2.getX())**2 + (p1.getY() - p2.getY())**2)
    side_b = sqrt((p3.getX() - p2.getX())**2 + (p3.getY() - p2.getY())**2)
    side_c = sqrt((p1.getX() - p3.getX())**2 + (p1.getY() - p3.getY())**2)

    s = (side_a + side_b + side_c)/2

    print("Triangle area:", sqrt(s*(s-side_a)*(s-side_b)*(s-side_c)))
    print("Triangle perimeter:", 2*s)

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
