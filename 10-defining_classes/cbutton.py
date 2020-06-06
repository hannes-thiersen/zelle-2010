# File:            cbutton.py
# Date:            2020-03-26
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   Circular button object

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from graphics import *

#------------------------------------------------------------------------------
# CLASSES
#------------------------------------------------------------------------------
class CButton():

    """
    A button is a labeled circle in a window. It is activated or
    deactivated with the activate() and deactivate() methods. The clicked(p)
    method returns true if the button is active and p is inside it.
    """

    def __init__(self, win, center, radius, label):
        """
        Creates a rectangular button e.g.:
        qb = Button(myWin, centerPoint, width, height, 'Quit')
        """
        self.center = center
        self.radius = radius
        self.circ = Circle(center, radius)
        self.circ.setFill("lightgray")
        self.circ.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def activate(self):
        """Set this button to 'active'."""
        self.label.setFill("black")
        self.circ.setWidth(2)
        self.active = True

    def clicked(self, p):
        """ Returns true if button active and p i inside.  """
        dx = self.center.getX() - p.getX()
        dy = self.center.getY() - p.getY()
        return (self.active and dx**2 + dy**2 <= self.radius**2)

    def deactivate(self):
        """Set this button to 'inactive'."""
        self.label.setFill("darkgrey")
        self.circ.setWidth(1)
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
