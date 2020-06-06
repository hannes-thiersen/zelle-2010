# File:          convert_intro-progex2.1.py
# Date:          2019-09-20
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 2.1
# Description:
#   A user-friendly program should print an introduction that tells the user
#   what the program does. Modify the `convert.py` program (Section 2.2) to
#   print an introduction.

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def main():
    print("This program converts temperatures in Celsius to Fahrenheit.")
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is" , fahrenheit, "degrees Fahrenheit.")

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
if __name__ == "__main__":

    main()
