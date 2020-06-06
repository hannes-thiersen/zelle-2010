# File:          fibonacci_sequence-progex3.16.py
# Date:          2019-09-26
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 3.16
# Description:
#   A Fibonacci sequence is a sequence of numbers where each successive number
#   is the sum of the previous 2. The classic Fibonacci sequence begins:
#   1, 1, 2, 3, 5, 8, 13, ... . Write a program that computes the `n`th
#   Fibonacci number where `n` is a value input by the user For example `n`=6,
#   then the result is 8.

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    print("Calculate the `n`th Fibonacci number.")
    number = eval(input("Insert the number for `n`: "))

    a, b = 1, 1

    for _ in range(number-2):
        a, b = b, b + a

    print(f"Fibonacci({number}) =", b)


#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
