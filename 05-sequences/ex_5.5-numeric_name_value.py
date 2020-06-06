# File:            numeric_name_value-progex5.5.py
# Date:            2019-10-19
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:        prog ex 5.5
# Description:
#   Numerologist claim to be able to determine a person's character traits
#   based on the "numeric value" of a name. The value of a name is determined
#   by summing up the values of the letters of the name where "a" is 1, "b" is
#   2, "c" is 3 etc., up to "z" being 26. For example, the name "Zelle" would
#   have the value 26 + 5 + 12 + 12 + 5 = 60 (which happens to be a very
#   auspicious number, by the way). Write a progam that calculates the umberic
#   value of a singe name provided as input.

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def main():
    print("Program calculates the numeric value of a name.")

    name = input("Enter a name: ")

    numeric = 0
    for letter in name:
        numeric += ord(letter.lower()) - 96

    print(f"Numerice value: {numeric}")


#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
