# File:            button.py
# Date:            2020-03-20
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   Button object

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from graphics import *

#------------------------------------------------------------------------------
# CLASSES
#------------------------------------------------------------------------------
class Button():

    """
    A button is a labeled rectangle in a window. It is activated or deactivated
    with the activate() and deactivate() methods. The clicked(p) method returns
    true if the button is active and p is inside it.
    """

    def __init__(self, win, center, width, height, label):
        """
        Creates a rectangular button e.g.:
        qb = Button(myWin, centerPoint, width, height, 'Quit')
        """
        w,h = width/2., height/2.
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill("lightgray")
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def activate(self):
        """Set this button to 'active'."""
        self.label.setFill("black")
        self.rect.setWidth(2)
        self.active = True

    def clicked(self, p):
        """ Returns true if button active and p i inside.  """
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax )

    def deactivate(self):
        """Set this button to 'inactive'."""
        self.label.setFill("darkgrey")
        self.rect.setWidth(1)
        self.active = False

    def getLabel(self):
        """ Returns the label string of this button.  """
        return self.label.getText()

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def main():
    pass

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
