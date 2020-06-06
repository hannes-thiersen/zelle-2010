# File:          numbers2text2.py
# Date:          2019-09-29
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Example:       numbers2text2.py
# Description:
#   A program to convert a sequence of Unicode number into a string of text.
#   Efficient version using a list accumulator.

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    print("This program converts a sequence of Unicode numbers into")
    print("the string of text that it represents.\n")

    # Get the message to encode
    inString = input("Please enter the Unicode-encoded message: ")

    # Loop through each substring and build Unicode message
    for numStr in inString.split():
        codeNum = eval(numStr)              # convert digits to a number
        chars.append(chr(codeNum))          # accumulate new character

    message = "".join(chars)
    print("\nThe decode message is:", message)

#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
