# File:            msdie.py
# Date:            2019-12-31
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   Class definition for an n-sided die.

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from random import randrange

#------------------------------------------------------------------------------
# CLASSES
#------------------------------------------------------------------------------
class MSDie:

    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = randrang(1, self.sides + 1)

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():
    pass

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
