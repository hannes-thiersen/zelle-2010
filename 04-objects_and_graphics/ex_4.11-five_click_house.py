# File:          five_click_house-progex4.11.py
# Date:          2019-09-29
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 4.11
# Description:
#   You are to  write a program that allows the user to draw a simple house
#   using five mouse-clicks. The first two clicks will be the opposite corners
#   of the rectangular frame or the house. The third click will indicate the
#   center of the top edge of a rectangular door. The door should have a total
#   width that is 1/5 of the width of the house frame. The sides of the door
#   should extent from the corners of the top down to the bottom of the frame.
#   The fourth click will indicate the center of a square window. The window is
#   half as wide as the door. The last click will indicate the peak of the
#   roof. The edges of the roof will extend from the point at the peak to the
#   corner of the top edge of the house frame.

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

    instruct = Text(Point(400, 500),
                "Click the lower left corner in the frame of the house")
    instruct.draw(win)
    p1 = win.getMouse()
    p1.draw(win)

    instruct.setText("Click the upper right corner in the frame of the house")
    frame = Rectangle(p1, win.getMouse())
    p1.undraw()
    frame.draw(win)
    door_width = (frame.getP2().getX() - frame.getP1().getX())/5/2

    instruct.setText("Click the middle top of the door")
    p1 = win.getMouse()
    door = Rectangle(
            Point(
                p1.getX() - door_width,
                frame.getP1().getY()
                ),
            Point(
                p1.getX() + door_width,
                p1.getY(),
                )
            )
    door.draw(win)

    instruct.setText("Click the middle of the square window")
    p1 = win.getMouse()
    window = Rectangle(
            Point(
                p1.getX() - door_width/2,
                p1.getY() - door_width/2,
                ),
            Point(
                p1.getX() + door_width/2,
                p1.getY() + door_width/2,
                )
            )
    window.draw(win)

    instruct.setText("Click for the peak of the roof")
    p1 = win.getMouse()
    roof = Polygon(
                p1,
                frame.getP2(),
                Point(
                    frame.getP1().getX(),
                    frame.getP2().getY(),
                    )
            )
    roof.draw(win)

    instruct.undraw()

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
