# File:            ex_8.13-linear_regression.py
# Date:            2019-12-20
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   Write a program that graphically plots a regression line, that is, the line
#   with best fit through a collection of points. First ask the user to
#   specify the data points by clicking on them in a graphics window. To find
#   the end of input, place a small rectangle labeled "Done" in the lower left
#   corner of the window; the program will stop gathering points when the user
#   clicks inside that rectangle.
#
#   The regression line is the line with the following equation:
#
#       y = y_bar + m(x - x_bar)
#
#   where
#
#       m = [sum(x_i*y_i) - n*x_bar*y_bar] / [sum(x_i**2)- n*x_bar**2]
#
#   x_bar is the mean of the x-values, y_bar is the mean of the y-values, and n
#   is the number of points.
#
#   As the user clicks on point, the program should draw then in the graphics
#   window and keep track of the count of input values and the running sum of
#   x, y, x**2 and xy. When the user clicks inside the "Done" rectangle, the
#   program then computes value of y (using the equation above) corresponding
#   to the x values at the left and right edges of the window. After the line
#   is drawn, the program will pause for another mouse click before closing the
#   window and quitting

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from graphics import *

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def drawWindow():
    width = 800
    height = 600
    win = GraphWin("Data Canvas", width, height)
    return win

#------------------------------------------------------------------------------
def clickPoints(window):

    llcorner = Point(710, 540)
    urcorner = Point(790, 590)
    button = Rectangle(llcorner, urcorner)
    button.draw(window)

    text = Text(button.getCenter(),"Done")
    text.draw(window)

    points = []
    click = window.getMouse()

    while not clickedDone(click, llcorner, urcorner):
        click.draw(window)
        points.append(click)
        click = window.getMouse()

    return points

#------------------------------------------------------------------------------
def clickedDone(position, lowerleft, upperright):

    if (
            lowerleft.getX() < position.getX() < upperright.getX() and
            lowerleft.getY() < position.getY() < upperright.getY()
            ):
        return True
    return False

#------------------------------------------------------------------------------
def drawRegression(win, points):

    m, c = calculateLine(points)
    p0 = Point(0, c)
    pn = Point(800, m*800 + c)
    bestfit = Line(p0, pn)
    bestfit.draw(win)
    return None

#------------------------------------------------------------------------------
def calculateLine(points):
    x = []
    y = []
    xy = []
    x2 = []
    amount = len(points)
    for point in points:
        px, py = point.getX(), point.getY()

        x.append(px)
        y.append(py)
        x2.append(px**2)
        xy.append(px*py)

    x_ave = sum(x)/amount
    y_ave = sum(y)/amount
    x2_ave = sum(x2)/amount

    slope = (sum(xy) - amount*x_ave*y_ave) / (sum(x2) - amount*x_ave**2)
    constant = y_ave - slope*x_ave

    return slope, constant

#------------------------------------------------------------------------------
def haltQuit(win):
    Text(Point(800/2, 590), "Click to exit").draw(win)
    confirm = win.getMouse()
    win.close()
    return None

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():

    window = drawWindow()
    points = clickPoints(window)
    drawRegression(window, points)
    haltQuit(window)

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
