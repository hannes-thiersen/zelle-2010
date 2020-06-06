# File:            ex_7.9-calculate_Easter.py
# Date:            2019-12-19
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   A formula for computing Easter in the years 1982 - 2048, inclusive, is as
#   follows: let a = year%19, b = year%4, c=year%7, d = (19a + 24)%30, e = (2b
#   + 4c + 6d + 5)%7, respectively. Write a program that inputs a year,
#   verifies that it is in the proper range, and then prints out the date of
#   Easter that year.

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def easter(year):

    if not 1982 <= year <= 2048:
        print("Year is outside valid range 1982 - 2048.")
        return None

    a = year%19
    b = year%4
    c = year%7
    d = (19*a + 24)%30
    e = (2*b + 4*c + 6*d + 5)%7

    date = 22 + d + e

    if date < 31:
        print(f"{date} March {year}")
    else:
        print(f"{date-31} April {year}")

    return None

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():
    year = eval(input("Insert year: "))

    easter(year)

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
