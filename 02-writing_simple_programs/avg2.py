# File:          avg2.py
# Date:          2019-09-21
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Example:       avg2.py
# Description:
#   A simple program to average two exam scores
#   Illustrates use of multiple input

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def main():
    print("This program computes the average of two exam scores.")

    score1, score2 = eval(input("Enter two scores separated by a comma: "))
    average = (score1 + score2) / 2

    print("The average of the scores is:", average)

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
