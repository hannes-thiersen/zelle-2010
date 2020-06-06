# File:          chrismas_scene-progex4.4.py
# Date:          2019-09-28
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 4.4
# Description:
#   Write a program that draws a winter scene with a Chrismas tree and a
#   snowman.

#-----------------------------------------------------------------------------
# IMPORTS
#-----------------------------------------------------------------------------
from graphics import *

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():

    win = GraphWin("Chrismas Scene", 800, 600)
    win.setCoords(-40,-30, 40, 30)

    tree_ref = Point(-20, 15)
    snowman_ref = Point(20, 0)

    # tree
    tree_x = tree_ref.getX()
    tree_y = tree_ref.getY()
    # stump
    stump = Rectangle(Point(tree_x-3, tree_y-40), Point(tree_x+3, tree_y-30))
    stump.setFill("brown")
    stump.draw(win)
    # draw three similar triangles that increase in size
    increase = 3
    offset = 15
    for _ in range(2,-1,-1):
        top = Point(tree_x,tree_y + 10*increase - offset*_)
        bottoml = Point(tree_x - 5.5*increase, tree_y - offset*_)
        bottomr = Point(tree_x + 5.5*increase, tree_y - offset*_)
        triangle = [ top, bottoml, bottomr ]
        segment = Polygon(triangle)
        segment.setFill("green")
        segment.draw(win)

        increase-=1

    # snowman
    snow_x = snowman_ref.getX()
    snow_y = snowman_ref.getY()
    feet = Circle(Point(snow_x, snow_y - 8), 8)
    feet.setFill("white")
    feet.draw(win)
    body = Circle(Point(snow_x, snow_y + 2.5), 5.5)
    body.setFill("white")
    body.draw(win)
    head = Circle(Point(snow_x, snow_y + 10), 3)
    head.setFill("white")
    head.draw(win)

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
