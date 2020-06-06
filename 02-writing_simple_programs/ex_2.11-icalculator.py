# File:          icalculator-progex2.11.py
# Date:          2019-09-23
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 2.11
# Description:
#   Write an interactive Python calculator program. The program should allow
#   the user to type a mathematical expression, and then print the value of
#   the expression. Include a loop so that the user can perform many
#   calculations (say, up to 100). Note: To quit early, the user can make the
#   program crash by typing a bad expression or simply closing the window that
#   the calculator program is running in. You'll learn better ways of
#   terminating interactive programs in later chapters.

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    print("Basic calculator program.")
    print("Insert a mathematical expression at the prompt.")
    for _ in range(100):
        result = eval(input("exp = "))
        print("exp =", result)

#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
