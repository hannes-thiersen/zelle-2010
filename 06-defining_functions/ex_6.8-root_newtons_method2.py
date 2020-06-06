# File:            ex_6.8-root_newtons_method2.py
# Date:            2019-12-16
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:        ex 6.8
# Description:
#   Solve Programming Exercise 17 from Chapter 3 using a functions
#   `nextGuess(guess, x)` that returns the next guess.

#-----------------------------------------------------------------------------
# IMPORTS
#-----------------------------------------------------------------------------
import math

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def nextGuess(guess, x):
    return (guess + x/guess)/2

#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
def main():
    print("Calculate the root of a number using Newton's method.")
    square = eval(input("Enter the number you want the root of: "))
    iterations = eval(input("Enter the number of method iterations: "))

    guess = square/2

    for _ in range(iterations):
        guess = nextGuess(guess, square)

    print("Guess:", guess)
    print("Root :", math.sqrt(square))

#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
