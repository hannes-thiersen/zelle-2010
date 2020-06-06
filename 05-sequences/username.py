# File:          username.py
# Date:          2019-09-29
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Example:       username.py
# Description:
#   Simple string processing program to generate usernames.

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    print("This program generates computer usernames.\n")

    # get user's first and last names
    first = input("Please enter first name (all lowercase): ")
    last = input("Please enter last name (all lowercase): ")

    # concatenate first initial with 7 chars of thte last name.
    uname = first[0] + last[:7]

    # output the username
    print("Your username is:", uname)

#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
