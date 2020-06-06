# File:            printfile.py
# Date:            2019-10-14
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Example:         printfile.py
# Description:
#   Prints a file to the screen.

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def main():
    fname = input("Enter filename: ")
    infile = open(fname, "r")
    data = infile.read()
    print(data)

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
