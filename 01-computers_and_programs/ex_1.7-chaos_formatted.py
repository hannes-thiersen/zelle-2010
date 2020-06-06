# File:          chaos_formatted-progex1.7.py
# Date:          2019-09-20
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 1.7
# Description:
#   Modify the `chaos` program so that it accepts two inputs and then prints a
#   table with two columns similar to the one shown in Section 1.8. (Note: You
#   will probably not be able to get the columns to line up as nicely as those
#   in the example. Chapter 5 discusses how to print numbers with a fixed
#   number of decimal places.

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter another number between 0 and 1: "))

    print(f"input {x:^10} {y:^10}")
    print("-"*26)

    for i in range(20):
        x = 3.9*x * (1 - x)
        y = 3.9*y * (1 - y)
        print(f"{' '*6}{x:^10.6f} {y:^10.6f}")

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
if __name__ == "__main__":

    main()
