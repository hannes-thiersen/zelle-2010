# File:          futval_compound-progex2.7.py
# Date:          2019-09-22
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 2.7
# Description:
#   As an alternative to APR, the interest acrued on an account is often
#   described in terms of a nominal rate nad the number of compounding
#   periods. For example, if the interest rate is 3% and the interest is
#   compounded quarterly, the account actually earns 3/4% interest over every
#   3 months.
#
#   Modify the `futval.py` program to use this method of everting the interst
#   rate. the program should prompt the user for the yearly rate (`rate`) and
#   the number of time that interest is compounded each year (`periods`). To
#   compute the value in 10 years, the program will loop `10 * periods` times
#   and accrue `rate/period` interest on each iteration.

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal = eval(input("Enter the initial principal: "))
    rate = eval(input("Enter the interest rate: "))
    periods = eval(input("Enter the anual amount of compound periods: "))

    for i in range(10 * periods):
        principal = principal * (1 + rate/periods)

    print("The value in 10 years is:", principal)

#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
