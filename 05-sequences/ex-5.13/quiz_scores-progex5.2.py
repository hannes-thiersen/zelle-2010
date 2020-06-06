# File:            quiz_scores-progex5.2.py
# Date:            2019-10-15
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:        prog ex 5.2
# Description:
#   A certain CS professor gives 5-point quizzes that are graded on the scale
#   5-A, 4-B, 3-C, 2-D, 1-F, 0-F. Write a program that accepts a quiz score as
#   an input and prints out the corresponding grade.

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def main():

    grades = [ "F", "F", "D", "C", "B", "A" ]

    in_name = input("File containing scores: ")
    out_name = input("Output file: ")

    outstring = "Score,Grade\n"

    with open(in_name, "r") as infile:
        for line in infile:
            outstring += f"{eval(line)},{grades[eval(line)]}\n"

    with open(out_name, "w") as outfile:
        outfile.write(outstring)


#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
