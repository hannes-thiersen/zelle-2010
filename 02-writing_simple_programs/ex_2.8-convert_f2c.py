# File:          convert_f2c-progex2.8.py
# Date:          2019-09-23
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 2.8
# Description:
#   Writ a program that converts temperatures from Fahrenheit to Celsius.

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = 5/9 * (fahrenheit - 32)
    print("The temperature is" , celsius, "degrees Celsius.")

#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
