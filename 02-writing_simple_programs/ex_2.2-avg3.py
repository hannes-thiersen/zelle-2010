# File:          avg3-progex2.2.py
# Date:          2019-09-21
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 1.2
# Description:
#   Modify the `avg2.py` program (Section 2.5.3) to find the average of three
#   exam scores.

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def main():
    print("This program computes the average of three exam scores.")

    scores = eval(input("Enter three scores separated by a comma: "))
    average = sum(scores) / 3

    print("The average of the scores is:", average)

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
