# File:          convert_i2c-progex2.10.py
# Date:          2019-09-23
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 2.10
# Description:
#   Write a program to perform a unit conversion of your own choosing. Make
#   sure that the program prints an introduction that explains what it does.
#
#   Convert inches to centimeters: 1" = 2.54 cm

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    print("Program converts inches to centimeters.")
    inches = eval(input("Insert the distance in inches: "))
    centimeter = inches * 2.54
    print("Distance is", centimeter, "cemtimeter")

#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
