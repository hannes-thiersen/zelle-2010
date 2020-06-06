# File:          sum_numbers-progex3.13.py
#
# Date:          2019-09-26
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 3.13
# Description:
#   Write a program to sum a series of numbers entered by the user. The
#   program should first prompt the user for how many numbers are to be summed.
#   It should then input each of the numbers and print the total sum.

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    print("Calculate the sum of entered numbers.")
    _ = eval(input("How many number should be summed? "))
    numbers = eval(input("Enter all number separated by commas "))
    print("The sum is", sum(numbers))

#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
