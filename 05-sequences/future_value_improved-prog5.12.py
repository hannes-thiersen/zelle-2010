# File:            future_value_improved-prog5.12.py
# Date:            2019-10-23
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:        prog ex 5.12
# Description:
#   Write an improved version of the future value program from Chapter 2. Your
#   program will prompt the user for the amount of the investment, the
#   annualized interest rate, and the number of years of the investment. The
#   program will then output a nicely formatted table that tracks the value of
#   the investment year by year. Your output might look something like this:

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def main():

    print(
    "Program calculates the growth of an investments with annualized interest"
    )

    principal = eval(input("Enter principal amount: "))
    interest = eval(input("Enter interest rate (6% = 0.06): "))
    term = eval(input("Enter investment term in years: "))

    header = "Year  {:^9s}".format("Value")
    hline = len(header)*"-"
    print(f"{header}\n{hline}")

    # term +1 for final amount at end of year ( == start of next year)
    for i in range(term+1):
        balance = principal * ( 1 + interest ) ** i
        str_balance = f"${balance:.2f}"
        print(f"{i:^5d} {str_balance:>9s}")

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
