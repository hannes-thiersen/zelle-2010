# File:            word_count-progex5.14.py
# Date:            2019-12-03
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   Word count. A common utility on Unix/Linux systems is a small programs
#   called "wc". This program analyzes a file to determine the number of lines,
#   words, and characters contained therein. Write your own version of wc. The
#   program should accept a file name as input and then print three numbers
#   showing the count of lines, words, and characters in the file.

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def main():

    inname = input("Input file: ")
    linecount = wordcount = charactercount = 0

    with open(inname, "r") as infile:
        for line in infile:
            linecount += 1
            words = line.split()
            wordcount+=len(words)
            for word in words:
                charactercount+=len(word)

    print(f"Line: {linecount}, Words: {wordcount}, Chars: {charactercount}")


#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
