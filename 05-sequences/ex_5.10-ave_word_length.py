# File:            ave_word_length-progex5.10.py
# Date:            2019-10-23
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:        prog ex 5.10
# Description:
#   Write a program that calculates the average word length in a sentence
#   entered by the user.

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def main():
    print("Program calculates the average length of a word in a sentence.")

    sentence = input("Please type a sentence: ").split()

    total_len = 0

    for word in sentence:
        total_len += len(word)

    print("Average word length: {:.1f} characters"
            .format(total_len/len(sentence)))



#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
