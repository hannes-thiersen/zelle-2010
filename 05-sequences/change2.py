# File:            change2.py
# Date:            2019-10-14
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Example:         change2.py
# Description:
#   A program to calculate the value of some change in dollars. This version
#   represents the total cash in cents.

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def main():
    print("Change Counter\n")

    print("Please enter the count of each coin type.")
    quarters = eval(input("Quarters: "))
    dimes = eval(input("Dimes: "))
    nickels = eval(input("Nickels: "))
    pennies = eval(input("Pennies: "))

    total = 25*quarters + 10*dimes + 5*nickels + pennies

    print("The total value of your change is ${0}.{1:0>2}"
            .format(total//100, total%100))

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
