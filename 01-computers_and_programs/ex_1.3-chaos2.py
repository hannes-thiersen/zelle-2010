# File:          chaos2-progex1.3.py
# Date:          2019-09-20
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 1.3
# Description:
#   Modify the `chaos` program using 2.0 in place of 3.9 as the multiplier in
#   the logistic function. Your modified line of code should look like this:
#
#       `x = 2.0*x * (1-x)`
#
#   Run the program for various input values and compare the results to those
#   obtained from the the original program. Write a short paragraph describing
#   any differences that you notice in the behaviour of the two versions.

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 2.0*x * (1 - x)
        print(x)

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
if __name__ == "__main__":

    main()
