# File:            chaos_improved-progex5.11.py
# Date:            2019-10-23
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:        prog ex 5.11
# Description:
#   Write an improved version of the Chaos program from Chapter 1 that allows a
#   user to input tow initial values and the number of iterations and then
#   prints a nicely formatted table showing how the values change over time.
#   For example, if the starting values were `.25` and `.26` with 10
#   iterations, the table might look like this:
#
#       index    0.25        0.26
#       --------------------------
#         1    0.731250    0.750360
#         2    0.766441    0.730547
#         3    0.698135    0.767707
#         4    0.821896    0.695499
#         5    0.570894    0.825942
#         6    0.955399    0.560671
#         7    0.166187    0.960644
#         8    0.540418    0.147447
#         9    0.968629    0.490255
#        10    0.118509    0.974630

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter first number between 0 and 1 : "))
    y = eval(input("Enter second number between 0 and 1: "))
    n_iter = eval(input("Enter the number of iterations: "))

    print(f"index {x:^10.2f}  {y:^10.2f}")
    print("-"*26)

    for i in range(n_iter):
        x = 3.9*x * (1 - x)
        y = 3.9*y * (1 - y)
        print(f"{i+1:^5d} {x:^10.6f}  {y:^10.6f}")
    pass

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
