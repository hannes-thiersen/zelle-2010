# File:          futval_guinput-progex4.6.py
# Date:          2019-09-29
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 4.6
# Description:
#   Modify the graphical future value program so that the input (principal and
#   apr) also are done in a graphical fahion using `Entry` objects.

#-----------------------------------------------------------------------------
# IMPORTS
#-----------------------------------------------------------------------------
from graphics import *

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    # Introduction
    print("This program plots the growth of a 10-year investment.")

    # Create a graphics window
    win = GraphWin("Investment Growth Chart", 800, 800)
    win.setBackground("white")
    win.setCoords(0,0,4,4)

    # Draw input messages and boxes
    message1 = Text(Point(1,3), "Principal:")
    message1.draw(win)
    message2 = Text(Point(1,2), "APR:")
    message2.draw(win)

    # Get principal and interest rate
    amount = Entry(Point(2,3), 10)
    amount.setText("0.0")
    amount.draw(win)
    rate = Entry(Point(2,2), 10)
    rate.setText("0.0")
    rate.draw(win)

    button = Text(Point(1,1), "Calculate")
    button.draw(win)
    rect = Rectangle(Point(.5,.5), Point(1.5,1.5))
    rect.draw(win)
    win.getMouse()

    principal = eval(amount.getText())
    apr = eval(rate.getText())

    # undraw the current objects
    message1.undraw()
    message2.undraw()
    amount.undraw()
    rate.undraw()
    button.undraw()
    rect.undraw()

    # Create labels on left edge
    win.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1, 0), " 0.0K").draw(win)
    Text(Point(-1, 2500), " 2.5K").draw(win)
    Text(Point(-1, 5000), " 5.0K").draw(win)
    Text(Point(-1, 7500), " 7.5K").draw(win)
    Text(Point(-1, 10000), "10.0K").draw(win)

    # Draw bar for initial principal
    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # Draw bars for successive years
    for year in range(1,11):
        # calculate value for the next year
        principal = principal * (1 + apr)
        # draw bar for this value
        xll = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(year, 0), Point(year + 1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    input("Press <Enter> to quit")
    win.close()

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
