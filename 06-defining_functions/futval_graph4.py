# File:            futval_graph4.py
# Date:            2019-12-15
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Example:         6.6 futval_graph3.py
# Description:
#   Program calculates the balance of a savings account and plots the results.
#   Code was refactored to avoid repetition and make it more readable

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from graphics import *

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def createLabeledWindow():
    window = GraphWin("Investment Growth Chart", 320, 240)
    window.setBackground("white")
    window.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1, 0), " 0.0K").draw(window)
    Text(Point(-1, 2500), " 2.5K").draw(window)
    Text(Point(-1, 5000), " 5.0K").draw(window)
    Text(Point(-1, 7500), " 7.5K").draw(window)
    Text(Point(-1, 10000), "10.0K").draw(window)
    return window

#------------------------------------------------------------------------------
def drawBar(window, year, height):
    # Draw a bar in window for given year with fiven height
    bar = Rectangle(Point(year, 0), Point(year+1, height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(window)

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():
    # Introduction
    print("This program plots the growth of a 10-year investment.")

    # Get principal and interest rate
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annualized interest rate: "))

    win = createLabeledWindow()
    drawBar(win, 0, principal)
    for year in range(1,11):
        # calculate value for the next year
        principal = principal * (1 + apr)
        drawBar(win, year, principal)

    input("Press <Enter> to quit")
    win.close()

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
