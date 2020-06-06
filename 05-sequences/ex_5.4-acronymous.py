# File:            acronymous-progex5.4.py
# Date:            2019-10-19
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:        prog ex 5.4
# Description:
#   An acronm is a word formed by taking the first letters of the words in a
#   phrase and making a word from them. For example, RAM is an acronym for
#   "random access memory." Write a program that allows the user to type in a
#   phrase and then outputs the acronym for that phrase. Note: the acronym
#   should be all uppercase, even if the words in the phrase are not
#   capitalized.

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def main():
    print("Program takes a phrase and turns it into an acronym.")

    phrase = input("Insert a phrase: ")

    phrase = phrase.split()

    acronym = [ letter[0].upper() for letter in phrase ]

    print("Acronym: {}".format("".join(acronym)))


#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
