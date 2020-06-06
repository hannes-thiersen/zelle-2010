# File:            happy.py
# Date:            2019-12-15
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Example:         6.2 happy.py
# Description:
#   Program prints the lyrics for "Happy Birthday".

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def happy():
    print("Happy Birthday to you!")

def sing(person):
    happy()
    happy()
    print(f"Happy Birthday, dear {person}.")
    happy()

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():
    sing("Fred")
    print()
    sing("Lucy")
    print()
    sing("Elmer")

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
