# File:          change.py
# Date:          2019-09-26
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Example:       change.py
# Description:
#   A program to calculate the value of some change in dollars.

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    print("Change Counter")
    print()
    print("Please enter the count to each coin type.")
    quarters = eval(input("Quaters: "))
    dimes = eval(input("Dimes: "))
    nickels = eval(input("Nickels: "))
    pennies = eval(input("Pennies: "))
    total = quarters*.25 + dimes*.10 + nickels*.05 + pennies*.01
    print()
    print("The total value of your change is", total)

#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
