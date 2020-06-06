# File:          convert_k2m-progex2.9.py
# Date:          2019-09-23
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 2.9
# Description:
#   Write a program that converts distaces measured in kilometers to miles.
#   One kilometer is approximately 0.62 miles.
#   1 mile = 1.609 km

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    print("Program converts kilometers to miles.")
    kilometers = eval(input("Insert distance in kilometers: "))
    miles = kilometers / 1.609
    print("The distance is", miles, "miles.")

#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
