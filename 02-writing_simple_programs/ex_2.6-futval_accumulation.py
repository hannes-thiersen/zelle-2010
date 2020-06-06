# File:          futval_accumulation-progex2.6.py
# Date:          2019-09-22
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 2.6
# Description:
#   Suppose you have an investment plan where you invest a certain fixed
#   amount every year. Modify `futval.py` to compute the total accumulation of
#   your investment. The inputs to the program will be the amount to invest
#   each year, the interest rate, and the number of years for the investment.

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    print("This program calculates the future value")
    print("of a n-year investment with a anual capital addition.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    term = eval(input("Enter the investment time in years: "))
    cap = eval(input("Enter the anual capital investment: "))

    for i in range(term):
        principal = principal * (1 + apr) + cap

    print("The value in", term, "years is:", principal)

#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
