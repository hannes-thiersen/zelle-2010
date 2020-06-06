# File:          factorial.py
# Date:          2019-09-26
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Example:       factorial.py
# Description:
#   Program to compute the factorial of a number
#   Illustrates for loop with an accumulator

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    n = eval(input("Please enter a whole number: "))
    fact = 1
    for factor in range(n, 1, -1):
        fact = fact * factor
    print("The factorial of", n, "is", fact)

#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
