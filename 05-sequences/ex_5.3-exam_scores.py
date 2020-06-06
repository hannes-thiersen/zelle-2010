# File:            exam_scores-progex5.3.py
# Date:            2019-10-19
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:        prog ex 5.3
# Description:
#   A certain CS professor give 100-point exams that are graded on the scale
#   90-100:A, 80-89:B, 70-79:C 60-69:D, <60:F. Write a program that accpets an
#   exam score as input and prints out the corresponding grade.

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def main():

    print("Program calculate the grade for an 100-point exam score.")

    passing_grades = [ 'D', 'C', 'B', 'A' ]

    while True:

        score = int(input("Insert the exam score (-1 to exit): "))

        if score < 0:
            break

        if score < 60:
            print("Grade: F")
        else:
            grade = (score - 60) // 10
            try:
                print(f"Grade: {passing_grades[grade]}")
            except:
                print(f"Grade: A")


#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
