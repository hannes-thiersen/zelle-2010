# File:          circle_intersect-progex4.7.py
# Date:          2019-09-29
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 4.7
# Description:
#   Circle Intersection. Write a program that computes the intersection of aa
#   circle with a horizontal line and displays the information textually and
#   graphically.
#
#   Input:
#       Radius of the circle and the y-intercept of the line.
#
#   Ouput:
#       Draw a circle centered at (0,0) with the given radius in a window with
#       coordinates running from -10,-10 to 10,10.
#       Draw a horizotal line across the window with the given y-intercept.
#       Draw the two point of intersection in red.
#       Print out the x values fo the points of intersection.
#
#   Formula:
#       x = +/- sqrt(r**2 - y**2)

#-----------------------------------------------------------------------------
# IMPORTS
#-----------------------------------------------------------------------------
from graphics import *
from math import sqrt

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():

    radius = eval(input("Enter a radius between 0 and 10: "))
    y = eval(input("Enter a y-value between -10 and 10: "))

    win = GraphWin("Circle Intersect", 800, 800)
    win.setCoords(-10,-10, 10,10)

    circle = Circle(Point(0,0), radius)
    circle.draw(win)
    line = Line(Point(-10, y), Point(10, y))
    line.draw(win)

    intersect = sqrt(radius**2 - y**2)

    print(f"Intersects at (+/- {intersect}, {y})")

    p1 = Point(intersect, y)
    p1.setFill("red")
    p1.draw(win)
    p2 = Point(- intersect, y)
    p2.setFill("red")
    p2.draw(win)





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
