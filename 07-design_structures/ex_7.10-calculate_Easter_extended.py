# File:            ex_7.10-calculate_Easter_extended.py
# Date:            2019-12-19
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   The formula for Easter in the previous problem works for every year in the
#   range 1900-2099 except for 1954, 1981, 2049 and 2076. For these 4 year it
#   produces a date that is one week too late. Modify the above program to work
#   for the entrie range 1900-2099.

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def easterExtended(year):

    if not 1900 <= year <= 2099:
        print("Year is outside valid range 1900 - 2099.")
        return None

    a = year%19
    b = year%4
    c = year%7
    d = (19*a + 24)%30
    e = (2*b + 4*c + 6*d + 5)%7

    date = 22 + d + e

    if year in [1954, 1981, 2049, 2076]:
        date -= 7

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

    easterExtended(year)

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
