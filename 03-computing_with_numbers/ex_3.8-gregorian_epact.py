# File:          gregorian_epact-progex3.8.py
# Date:          2019-09-26
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 3.8
# Description:
#   The Gregorian epact is the number of days betwween 1 January and the
#   previous new moon. This value is used to figure out the date of Easter. It
#   is calculated by these formulas (using int arithmetic):
#
#       C = year//100
#
#       epact = (8 + C//4 - C + (8C + 13)//25 + 11(year%19)) % 30
#
#   Write a program that prompts the user for a 4-digit year and then outputs
#   the value of the epact.

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    print("Calculate the epact of a given year.")
    year = eval(input("Enter the year: "))
    c = year//100

    epact = (8 + c//4 - c + (8*c + 13)//25 + 11*(year%19))%30
    print("The value of the epact: ", epact)


#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
