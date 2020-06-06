# File:          face-progex4.3.py
# Date:          2019-09-28
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 4.3
# Description:
#   Write a program that draws some sort of face.

#-----------------------------------------------------------------------------
# IMPORTS
#-----------------------------------------------------------------------------
from graphics import *

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():

    win = GraphWin("Face", 500, 500)
    win.setCoords(0,0, 500, 500)
    face = Circle(Point(250, 250), 240)
    face.setWidth(2)
    face.setFill("white")
    face.draw(win)


    left_eye = Circle(Point(150, 350), 30)
    left_eye.setWidth(2)
    left_eye.setFill("white")
    left_eye.draw(win)
    right_eye = Circle(Point(350, 350), 30)
    right_eye.setWidth(2)
    right_eye.setFill("white")
    right_eye.draw(win)

    smile = Oval(Point(100, 100), Point(400, 200))
    smile.setWidth(2)
    cover = Rectangle(Point(100, 140), Point(400, 200))
    cover.setFill("white")
    cover.setOutline("white")
    smile.draw(win)
    cover.draw(win)

    # pause
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
