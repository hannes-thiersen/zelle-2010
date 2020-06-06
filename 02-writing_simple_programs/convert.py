# File:          convert.py
# Date:          2019-09-20
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Example:       convert.py
# Description:
#   A program to convert Celcius temps to Fahrenheit

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def main():
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is" , fahrenheit, "degrees Fahrenheit.")

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
if __name__ == "__main__":

    main()
