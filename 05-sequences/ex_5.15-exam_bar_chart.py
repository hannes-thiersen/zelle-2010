# File:            exam_bar_chart-progex5.15.py
# Date:            2019-12-03
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   Write a program to plot a horizontal bar chart of student exam scores. Your
#   program should get input from a file. The first line of the file contains
#   the count of the number of students in the file, and each subsequent line
#   contains a student's last name followed by a score in the range 0 to 100.
#   Your program should draw a horizontal rectangle for each student where the
#   length of the bar represents the student's score. The bars should all line
#   up on their left-hand edges. Hint" use the number of students to determine
#   the size of the window and its coordinates. Bonus: label the bars at the
#   left end with the student name.

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from graphics import *

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def main():


    inname = input("Input file: ")
    with open(inname, "r") as infile:
        total = eval(infile.readline())
        grades = dict()
        for line in infile:
            name, score = line.split()
            grades[name] = eval(score)

    print(grades)

    # Create a graphics window with labels on left edge
    width, height = 320, 240
    ratio = width/height
    win = GraphWin("Student Exam Scores", width, height)
    win.setBackground("white")

    cw = total*ratio
    win.setCoords(0, 0, cw, total)
    barindent = .4*cw
    barmaxlen = .6*cw
    count = 0

    for student, grade in sorted(grades.items()):
        Text(
                Point(.2*cw, count + .5),
                student
                ).draw(win)
        Rectangle(
                Point(barindent, count + .1),
                Point(barindent + barmaxlen*grade/100, count + .9)
                ).draw(win)
        count+=1

    input("<Enter> to exit")
    win.close()


#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
