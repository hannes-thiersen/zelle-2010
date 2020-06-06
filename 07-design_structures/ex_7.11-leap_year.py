# File:            ex_7.11-leap_year.py
# Date:            2019-12-19
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def isLeapYear(year):
    if year%4 == 0:
        if year%100 == 0 and not year%400 == 0:
            return False
        return True
    return False

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():
    year = eval(input("Insert year: "))

    print(f"Is {year} a leap year? {isLeapYear(year)}")

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
