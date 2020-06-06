# File:          drop_squares-progex4.1.py
# Date:          2019-09-28
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 4.1
# Description:
#   Alter the program from the last discussion question in the following ways:
#       (a) Make it draw squares instead of circles.
#       (b) Have each successive click draw an additional square on the screen
#           (rather than moving the existing one).
#       (c) Print a message on the window "Click again to quit" after the loop,
#           wait for a final click before closing the window.

#-----------------------------------------------------------------------------
# IMPORTS
#-----------------------------------------------------------------------------
from graphics import *

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    win = GraphWin("Square Drop", 400, 400)
    shape = Rectangle(Point(30, 30), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    c = shape.getCenter()
    for i in range(10):
        p = win.getMouse()
        dx = p.getX()
        dy = p.getY()
        rec = Rectangle(Point(dx - 20, dy - 20), Point(dx + 20, dy + 20))
        rec.setFill("red")
        rec.setOutline("red")
        rec.draw(win)

    Text(Point(200,200), "Click again to quit.").draw(win)
    win.getMouse()
    win.close()

#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
