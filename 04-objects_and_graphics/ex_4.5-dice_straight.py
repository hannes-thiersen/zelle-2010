# File:          dice_straight-progex4.5.py
# Date:          2019-09-28
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 4.5
# Description:
#   Write a program that draws 5 dice on the screen depicting a straight (1, 2,
#   3, 4, 5) or (2, 3, 4, 5, 6)

#-----------------------------------------------------------------------------
# IMPORTS
#-----------------------------------------------------------------------------
from graphics import *

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():

    win = GraphWin("Dice Straight", 600, 600)
    win.setCoords(-.5,-.5,2.5,2.5)

    # first dice
    dice1 = Rectangle(Point(0,-.5), Point(1,.5))
    dice1.setFill("white")
    center = dice1.getCenter()
    dice1.draw(win)

    one = Circle(Point(center.getX() + 0, center.getY() + 0), .2/3)
    one.setFill("black")
    one.draw(win)

    #second dice
    dice2 = Rectangle(Point(0,.5), Point(1,1.5))
    dice2.setFill("white")
    center = dice2.getCenter()
    dice2.draw(win)

    two = Circle(Point(center.getX() - 1/3, center.getY() - 1/3), .2/3)
    two.setFill("black")
    two.draw(win)

    three = Circle(Point(center.getX() + 1/3, center.getY() + 1/3), .2/3)
    three.setFill("black")
    three.draw(win)

    # third dice
    dice3 = Rectangle(Point(0,1.5), Point(1,2.5))
    dice3.setFill("white")
    center = dice3.getCenter()
    dice3.draw(win)

    one = Circle(Point(center.getX() + 0, center.getY() + 0), .2/3)
    one.setFill("black")
    one.draw(win)

    two = Circle(Point(center.getX() - 1/3, center.getY() - 1/3), .2/3)
    two.setFill("black")
    two.draw(win)

    three = Circle(Point(center.getX() + 1/3, center.getY() + 1/3), .2/3)
    three.setFill("black")
    three.draw(win)

    # fourth dice
    dice4 = Rectangle(Point(1,-.5), Point(2,.5))
    dice4.setFill("white")
    center = dice4.getCenter()
    dice4.draw(win)

    two = Circle(Point(center.getX() - 1/3, center.getY() - 1/3), .2/3)
    two.setFill("black")
    two.draw(win)

    three = Circle(Point(center.getX() + 1/3, center.getY() + 1/3), .2/3)
    three.setFill("black")
    three.draw(win)

    four = Circle(Point(center.getX() + 1/3, center.getY() - 1/3), .2/3)
    four.setFill("black")
    four.draw(win)

    five = Circle(Point(center.getX() - 1/3, center.getY() + 1/3), .2/3)
    five.setFill("black")
    five.draw(win)

    # fifth dice
    dice5 = Rectangle(Point(1,.5), Point(2,1.5))
    dice5.setFill("white")
    center = dice5.getCenter()
    dice5.draw(win)

    one = Circle(Point(center.getX() + 0, center.getY() + 0), .2/3)
    one.setFill("black")
    one.draw(win)

    two = Circle(Point(center.getX() - 1/3, center.getY() - 1/3), .2/3)
    two.setFill("black")
    two.draw(win)

    three = Circle(Point(center.getX() + 1/3, center.getY() + 1/3), .2/3)
    three.setFill("black")
    three.draw(win)

    four = Circle(Point(center.getX() + 1/3, center.getY() - 1/3), .2/3)
    four.setFill("black")
    four.draw(win)

    five = Circle(Point(center.getX() - 1/3, center.getY() + 1/3), .2/3)
    five.setFill("black")
    five.draw(win)

    # BONUS
    # sixth dice
    dice6 = Rectangle(Point(1,1.5), Point(2,2.5))
    dice6.setFill("white")
    center = dice6.getCenter()
    dice6.draw(win)

    two = Circle(Point(center.getX() - 1/3, center.getY() - 1/3), .2/3)
    two.setFill("black")
    two.draw(win)

    three = Circle(Point(center.getX() + 1/3, center.getY() + 1/3), .2/3)
    three.setFill("black")
    three.draw(win)

    four = Circle(Point(center.getX() + 1/3, center.getY() - 1/3), .2/3)
    four.setFill("black")
    four.draw(win)

    five = Circle(Point(center.getX() - 1/3, center.getY() + 1/3), .2/3)
    five.setFill("black")
    five.draw(win)

    six1 = Circle(Point(center.getX() - 1/3, center.getY()), .2/3)
    six1.setFill("black")
    six1.draw(win)

    six2 = Circle(Point(center.getX() + 1/3, center.getY()), .2/3)
    six2.setFill("black")
    six2.draw(win)

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
