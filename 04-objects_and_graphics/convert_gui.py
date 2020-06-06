# File:          convert_gui.py
# Date:          2019-09-28
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Example:       convert_gui.py
# Description:
#   Graphical interface for temperature conversion.

#-----------------------------------------------------------------------------
# imports
#-----------------------------------------------------------------------------
from graphics import *

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    win = GraphWin("Celsius Converter", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    # Draw the interface
    Text(Point(1,3), "Celsius Tempreature:").draw(win)
    Text(Point(1,1), "Fahrenheit Tempreature:").draw(win)
    intext = Entry(Point(2,3), 5)
    intext.setText("0.0")
    intext.draw(win)
    output = Text(Point(2,1), "")
    output.draw(win)
    button = Text(Point(1.5, 2.0), "Convert It")
    button.draw(win)
    Rectangle(Point(1, 1.5), Point(2, 2.5)).draw(win)

    # wait for a mouse click
    win.getMouse()

    # convert input
    celsius = eval(intext.getText())
    fahrenheit = 9/5 * celsius + 32

    # display output and change button
    output.setText(fahrenheit)
    button.setText("Quit")

    # wait for click and then quit
    win.getMouse()
    win.close()

#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
