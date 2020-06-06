# File:          archer_target-progex4.2.py
# Date:          2019-09-28
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 4.2
# Description:
#   An archery target consists of a central circle of yellow surrounded by
#   concentric rings of red, blue, black and white. Each ring has the same
#   "width", which is the same as the radius of the yellow circle. Write a
#   program the draws such a target. Hint: Objects drawn later will appear on
#   top of objects drawn earlier.

#-----------------------------------------------------------------------------
# IMPORTS
#-----------------------------------------------------------------------------
from graphics import *

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    win = GraphWin("Archery Target", 400, 400)
    win.setCoords(0., 0., 10., 10.)
    colours = [ "white", "black", "blue", "red", "yellow", ]
    radius=5
    for colour in colours:
        circle = Circle(Point(5,5), radius)
        circle.setFill(colour)
        #circle.setOutline(colour)
        circle.draw(win)
        radius -= 1

    # pause window
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
