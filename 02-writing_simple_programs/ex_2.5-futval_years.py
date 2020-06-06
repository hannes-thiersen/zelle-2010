# File:          futval_years-progex2.5.py
# Date:          2019-09-22
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 2.5
# Description:
#   Modify the `futval.py` program (Section 2.7) so that the number of years
#   for the investment is also a user input. Make sure to change the final
#   message to reflect the correct number of years.

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    print("This program calculates the future value")
    print("of a n-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    term = eval(input("Enter the investment time in years: "))

    for i in range(term):
        principal = principal * (1 + apr)

    print("The value in", term, "years is:", principal)

#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
