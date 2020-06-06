# File:            ex_8.3-double_investment.py
# Date:            2019-12-20
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   Write a program that uses a while loop to determine how long it takes for
#   an investment to double at a given interest rate. The input will be an
#   annualized interest rate, and the output is the number of years it takes an
#   investment to double. Note: the amount of the initial investment does not
#   matter; you can use $1.

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from math import log

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def printIntro():
    print((
    f"Program calculates the time it takes an investment to double for a"
    f"given interest rate.\n"
    f"It is assumed that the rate is annual compounded monthly.\n"
        ))

#------------------------------------------------------------------------------
def getInterestRate():
    an_rate =  input("Insert interest annual rate [default = 0.1]: ") or ".1"
    return eval(an_rate)/12

#------------------------------------------------------------------------------
def doubleTime(rate):
    initial = balance = 1
    period = 0

    while balance < 2*initial:
        balance *= (1 + rate)
        period+=1

    return period

#------------------------------------------------------------------------------
def analyticTime(rate):
    return log(2) / log(1 + rate)

#------------------------------------------------------------------------------
def resultSummary(period1, period2):

    print(f"Investment will double in {period1} months.")
    print(f"Theoretically calculated: {period2:2.2f} months")

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():

    printIntro()
    rate = getInterestRate()
    period = doubleTime(rate)
    analytic_period = analyticTime(rate)
    resultSummary(period, analytic_period)

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
