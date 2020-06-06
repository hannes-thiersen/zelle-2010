# File:          chaos.py
# Date:          2019-09-20
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Example:       chapter 1: chaos.py
# Description:
#   A simple program illustrating chaotic behaviour.

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(20):
        x = 3.9*x * (1 - x)
        print(x)

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
if __name__ == "__main__":

    main()
