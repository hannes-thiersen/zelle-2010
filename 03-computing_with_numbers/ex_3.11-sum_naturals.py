# File:          sum_naturals-progex3.11.py
# Date:          2019-09-26
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 3.11
# Description:
#   Write a program to find the sum of the first `n` natural numbers where the
#   value of `n` is provided by the user.

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    print("Calculate the sum of all naturals numbers up to a given number.")
    number = eval(input("Enter a natural number: "))

    total = number
    for i in range(number):
        total += i

    formula = (number+1)*number/2

    print("The sum up to", number, "is", total, "or", formula)


#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
