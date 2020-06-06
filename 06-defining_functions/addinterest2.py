# File:            addinterest2.py
# Date:            2019-12-15
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Example:         6.5.2 addinterest2.py
# Description:
#   Demonstrating pass-by-value behavior and exceptions

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def addInterest(balance, rate):
    newBalance = balance * (1+rate)
    return newBalance

def test():
    amount = 1000
    rate = 0.05
    amount = addInterest(amount, rate)
    print(amount)

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():
    test()

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
