# File:          ladder_height-progex3.10.py
# Date:          2019-09-26
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 3.10
# Description:
#   Write a program to determine the length of a ladder required to reach a
#   given height when leaned against a house. The height and angle of the
#   ladder are given as inputs. To compute length use:
#
#       length = height / sin(angle)
#
#   Note: The angle must be in radians. Prompt for an angle in degrees and use
#   this formula to convert:
#
#       radians = pi / 180 degrees

#-----------------------------------------------------------------------------
# IMPORTS
#-----------------------------------------------------------------------------
import math

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    print("Calculate ladder length for given height and angle.")
    height = eval(input("Enter required height: "))
    angle = eval(input("Enter leaning angle (in degrees): "))

    angle = angle * math.pi / 180
    length = height / math.sin(angle)

    print("The required ladder length is", length)

#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
