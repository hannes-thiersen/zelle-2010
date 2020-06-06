# File:            roller.py
# Date:            2020-03-20
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   Graphics program to roll a pair of dice. Uses custom widgets Button and
#   DieView
#   Exercise 1.8:
#   Modify the DieView class from the chapter by adding a method that allows
#   the color of the pips to be specified.
#
#   setColor(self, color) changes the color of the pips to color.
#
#   Hints: You can change the color by changing the value of the instance
#   variable foreground, but you also need to redraw the die after doing this.
#   Modify setValue so that it remembers th value of the die in tan instance
#   variable. The setColor can call setValue and pass the stored value to
#   redraw the die. You can test your new class with the roller.py program.
#   Hive the dice change to a random color after each roll (you can generate a
#   random color with the color_rgb function).

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from button import Button
from dieview import DieView
from graphics import GraphWin, Point, color_rgb
from random import randrange

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():

    # create the application window
    win = GraphWin("Dice Roller")
    win.setCoords(0,0,10,10)
    win.setBackground("gray")

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
            # re-rolling value and pip color of die1
            value1 = randrange(1, 7)
            color = color_rgb(randrange(0,256), randrange(0,256), randrange(0,256))
            die1.setValue(value1)
            die1.setColor(color)
            # re-rolling value and pip color of die2
            value2 = randrange(1, 7)
            color = color_rgb(randrange(0,256), randrange(0,256), randrange(0,256))
            die2.setValue(value2)
            die2.setColor(color)
            quitButton.activate()
        pt = win.getMouse()

    # close up shop
    win.close()

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
