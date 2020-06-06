# File:            ex_6.7-fibonacci_sequence2.py
# Date:            2019-12-16
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:        ex 6.7
# Description:
#   Write a function to compute the nth Fibonacci number. Use your function to
#   solve Programming Exercise 16 from Chapter 3.

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def fibonacci(N):
    a = b = 1

    if N in [1,2]:
        return 1

    for _ in range(N-2):
        a, b = b, a + b

    return b

#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
def main():
    print("Calculate the `n`th Fibonacci number.")
    number = eval(input("Insert the number for `n`: "))

    print(f"Fibonacci({number}) =", fibonacci(number))

#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
