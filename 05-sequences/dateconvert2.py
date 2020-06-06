# File:            dateconvert2.py
# Date:            2019-10-14
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Example:         dateconvert2.py
# Description:
#   Converts day month and year numbers into two date formats.

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def main():
    # get the day month and year
    day, month, year = eval(input("Enter day, month, and year numbers:"))

    date1 = str(month)+"/"+str(day)+"/"+str(year)

    months = [
            "January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December",
            ]

    monthStr = months[month-1]

    date2 = monthStr +" "+ str(day) +" , "+ str(year)

    print("The date is", date1, "or", date2)

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
