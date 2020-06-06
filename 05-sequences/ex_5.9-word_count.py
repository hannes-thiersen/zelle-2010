# File:            word_count-progex5.9.py
# Date:            2019-10-23
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:        prog ex 5.9
# Description:
#   Write a program that counts the number of words in a sentence entered by
#   the user.

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def main():
    print("Program counts the words in a sentence.")

    sentence = input("Please type a sentence: ")

    print("Word count: {}".format(len(sentence.split())))

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
