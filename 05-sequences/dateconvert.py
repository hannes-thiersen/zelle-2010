# File:            dateconvert.py
# Date:            2019-10-14
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Example:         dateconvert.py
# Description:
#   Converts a date in form "mm/dd/yyyy" to "month day, year"

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def main():
    # get the date
    dateStr = input("Enter a date (mm/dd/yyyy): ")

    # split into components
    monthStr, dayStr, yearStr = dateStr.split("/")

    # convert monthStr to the month name
    months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December",
            ]
    monthStr = months[int(monthStr) -1]

    # output result in month day, year format
    print("The converted date is:", monthStr, dayStr+",", yearStr)

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
