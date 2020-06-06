# File:          convert5-progex2.3.py
# Date:          2019-09-20
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 1.3
# Description:
#   Modify the `convert.py` program (Section 2.2) with a loop so that it
#   executes 5 times before quitting (i.e., it converts 5 temperatures in a
#   row).

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def main():
    print("Convert temperatures in Celsius to Fahrenheit.")
    temps = eval(input("Enter 5 Celsius temps separated by commas: "))
    for celsius in temps:
        fahrenheit = 9/5 * celsius + 32
        print(celsius, "Celsius =" , fahrenheit, "Fahrenheit")

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
if __name__ == "__main__":

    main()
