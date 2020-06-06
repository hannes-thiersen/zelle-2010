# File:            numeric_full_name-progex5.6.py
# Date:            2019-10-19
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:        prog ex 5.6
# Description:
#   Exapnd your solution to the previous problem to allow the calulation of a
#   complete name such as "John Marvin Zelle" or "John Jacob Jingleheimer
#   Smith." The total value is just the sum of the numeric values of all the
#   names.

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def main():
    print("Program calculates the numeric value of a full name.")

    name = input("Enter a full name: ").split()

    numeric = 0
    for part in name:
        for letter in part:
            numeric += ord(letter.lower()) - 96

    print(f"Numerice value: {numeric}")

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
