# File:          ave_number-progex3.14.py
# Date:          2019-09-26
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 3.14
# Description:
#   Write a program that finds the average of a series of numbers entered by
#   the user. As in the previous problem, the program will first ask the user
#   how many numbers there are. Note: the average should always be a float,
#   even if the user inputs are all ints.

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    print("Calculate the average of entered numbers.")
    _ = eval(input("How many number should be averaged? "))
    numbers = eval(input("Enter all number separated by commas "))
    print("The average is", sum(numbers)/len(numbers) )

#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":
    main()


