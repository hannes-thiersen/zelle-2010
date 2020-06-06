# File:            quiz_histogram-progex5.16.py
# Date:            2019-12-03
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   Write a program to draw a quiz score histogram. Your program should read
#   data from a file. Each line of the file contains a number in the range of
#   0-10. Your program must count the number of occurrences of each score and
#   then draw a vertical bar chart with a bar for each possible score (0-10)
#   with a height corresponding to the count of that score. Fore example, if 15
#   students got an 8, then the hight of the bar for 8 should be 15. Hint: use
#   a list that stores the count for each possible score.

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from graphics import *

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def main():

    with open("10quizscores.dat", "r") as infile:
        scores = infile.read()

    table = dict()
    for i in range(11):
        table [i] = scores.count(str(i))

    maxfreq = max(table.values())

    win = GraphWin("Quiz histogram", 600, 400)
    win.setCoords(0, -1.5, 11, maxfreq + 1)

    for score, freq in sorted(table.items()):
        Text(Point(score + .5, -.75), score).draw(win)
        if freq:
            Rectangle(
                    Point(score + .1, 0),
                    Point(score + .9, freq)
                    ).draw(win)

    input("Press any button to end")
    win.close()


#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
