# File:          month2.py
# Date:          2019-09-29
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Example:       month2.py
# Description:
#   A program to print the month abbreviation, given its number.

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():

    # months is a list used as a lookup table
    months = [ "Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    n = eval(input("Enter a month number (1-12): "))

    print("The month abbreviation is", months[n-1] + ".")


#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
