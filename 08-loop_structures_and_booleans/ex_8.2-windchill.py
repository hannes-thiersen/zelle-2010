# File:            ex_8.1-windchill.py
# Date:            2019-16.10
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   The National Weather Service computes the windchill index using the
#   following formula:
#
#       return 35.74 + 0.6215*T + (0.4275*T - 35.75)*(V**0.16)
#
#   Where T is the temperature in degrees Fahrenheit, and V is the wind speed
#   in miles per hour.

#   Write a program that prints a nicely formatted table of windchill values.
#   Rows should represent wind speed from 0 to 50 in 5 mph increments, and the
#   columns represent temperatures from -20 to 60 in 10-degree increments.
#   Note: The formula only applies for wind speeds in excess of 3 miles per
#   hour.

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def printIntro():
    print("""
Progam produces a table for windchill for a range temperatures and windspeeds.
""")
    print("Columns: Temperature in Fahrenheit")
    print("Rows: Wind speed in mph\n")

#------------------------------------------------------------------------------
def initializeRanges():
    return list(range(-20, 61, 10)), list(range(0, 51, 5))

#------------------------------------------------------------------------------
def printTableHeaders(temps):
    print(" "*7 + "|", end="")
    for temp in temps:
        print(f" {temp:6.1f}",end="")
    print()
    print("-"*7 + "+" + "-"*7*9)

#------------------------------------------------------------------------------
def printTableValues(temps, speeds):
    for speed in speeds:
        print(f"{speed:6.1f} |", end="")
        for temp in temps:
            wc = windchill(temp, speed)
            print(f" {wc:6.1f}", end="")
        print()

#------------------------------------------------------------------------------
def windchill(temp, speed):
    if not speed:
        return temp
    return 35.74 + 0.6215*temp + (0.4275*temp - 35.75)*(speed**0.16)

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():

    printIntro()
    temperatures, windspeeds = initializeRanges()
    printTableHeaders(temperatures)
    printTableValues(temperatures, windspeeds)

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
