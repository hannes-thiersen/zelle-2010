# File:          pi_series-progex3.15.py
# Date:          2019-09-26
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 3.15
# Description:
#   Write a program that approximates the value of pi by summing the terms of
#   the series: 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ... The program should
#   prompt the user for `n`, the number of terms to sum, and then ouput the sum
#   of the first `n` terms of this series. Have your program subtract the
#   approximation from the value of `math.pi` to see how accurate it is.

#-----------------------------------------------------------------------------
# IMPORTS
#-----------------------------------------------------------------------------
import math

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    print("Calculate the value of pi with a given amount of terms in a series")
    number = eval(input("How many terms of the series should be summed? "))

    pi_sum = 0
    for term in range(number):
        pi_sum += 4/(2*term + 1) * (-1)**term

    print("PI    =", pi_sum)
    print("error =", abs(pi_sum - math.pi) )


#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
