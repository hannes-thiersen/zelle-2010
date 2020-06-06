# File:            dateconvertmod-progex5.1.py
# Date:            2019-10-15
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:        prog ex 5.1
# Description:
#   As discussed in the chapter, string formatting could be used to simplify
#   the `dateconvert2.py` program. Go back and redo this program making use of
#   the string-formatting method.

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def main():
    # get the day month and year
    day, month, year = eval(input("Enter day, month, and year numbers: "))

    date1 = str(month)+"/"+str(day)+"/"+str(year)
    date1 = "{:0>2d}/{:0>2d}/{:4d}".format(month, day, year)

    months = [
            "January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December",
            ]

    date2 = "{} {}, {}".format(months[month-1], day, year)

    print("The date is", date1, "or", date2)

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
