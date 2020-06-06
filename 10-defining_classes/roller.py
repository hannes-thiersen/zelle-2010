# File:            roller.py
# Date:            2020-03-20
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   Graphics program to roll a pair of dice. Uses custom widgets Button and
#   DieView

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from button import Button
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
    die1 = DieView(win, Point(3,7), 2)
    die2 = DieView(win, Point(7,7), 2)
    rollButton = Button(win, Point(5,4.5), 6, 1, "Roll Dice")
    rollButton.activate()
    quitButton = Button(win, Point(5,1), 2, 1, "Quit")

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
