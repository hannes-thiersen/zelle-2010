# File:          futval.py
# Date:          2019-09-21
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Example:       futval.py
# Description:
#   A program to compute the value of an investment carried 10 years into the
#   future.

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))

    for i in range(10):
        principal = principal * (1 + apr)

    print("The value in 10 years is:", principal)

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
if __name__ == "__main__":

    main()
