# File:            ex_10.7-roller.py
# Date:            2020-03-26
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   Write a modified Button class that creates circular buttons. Call your
#   class CButton and implement the exact same methods that are in the existing
#   Button class. Your constructor should take the center of the button and its
#   radius as normal parameters. Place your class in a module called
#   cbutton.py. Test your class by modifying roller.py to use your buttons.

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from cbutton import CButton
from dieview import DieView
from graphics import GraphWin, Point
from random import randrange

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():

    # create the application window
    win = GraphWin("Dice Roller")
    win.setCoords(0,0,10,10)
    win.setBackground("green2")

    # draw the interface widgets
    die1 = DieView(win, Point(3,7), 3)
    die2 = DieView(win, Point(7,7), 3)
    rollButton = CButton(win, Point(3,3), 1.9, "Roll Dice")
    rollButton.activate()
    quitButton = CButton(win, Point(7,3), 1.9, "Quit")

    # event loop
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            value1 = randrange(1, 7)
            die1.setValue(value1)
            value2 = randrange(1, 7)
            die2.setValue(value2)
            quitButton.activate()
        pt = win.getMouse()

    # close up shop
    win.close()

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
