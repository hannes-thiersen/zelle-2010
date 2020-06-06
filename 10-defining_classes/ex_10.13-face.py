# File:            ex_10.13-face.py
# Date:            2020-04-28
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:        10.13
# Description:
#   Here is a simple class that draws a (grim) face in a graphics window:
#
#   Add methods to this class that cause the face to change expression. For
#   example you might add methods such as smile, wink, frown, flinch, etc. Your
#   class should implement at least three such methods.
#
#   Use your class to write a program that draws a face and provides the user
#   with buttons to change the facial expression.

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from graphics import *

#------------------------------------------------------------------------------
# CLASSES
#------------------------------------------------------------------------------
class Face():

    def __init__(self, window, center, size):
        eyeSize = 0.15 * size
        eyeOff = size / 3.
        mouthSize = 0.8 * size
        mouthOff = size / 2.
        self.head = Circle(center, size)
        self.head.draw(window)
        self.leftEye = Circle(center, eyeSize)
        self.leftEye.move(-eyeOff, -eyeOff)
        self.rightEye = Circle(center, eyeSize)
        self.rightEye.move(eyeOff, -eyeOff)
        self.leftEye.draw(window)
        self.rightEye.draw(window)
        p1 = center.clone()
        p1.move(-mouthSize/2, mouthOff)
        p2 = center.clone()
        p2.move(mouthSize/2, mouthOff)
        self.mouth = Line(p1,p2)
        self.mouth.draw(window)

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():

    win = GraphWin("Facial expressions")
    win.setCoords(10,10,0,0)
    smiley = Face(win, Point(5,5), 4)

    win.getMouse()
    win.close()

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
