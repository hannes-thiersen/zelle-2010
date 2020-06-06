# File:            addinterest3.py
# Date:            2019-12-15
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Example:         6.5.2 addinterest3.py
# Description:
#   Demonstrating pass-by-value behavior and exceptions

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def addInterest(balances, rate):
    for i in range(len(balances)):
        balances[i] = balances[i] * (1+rate)

def test():
    amounts = [1000, 2200, 800, 360]
    rate = 0.05
    addInterest(amounts, rate)
    print(amounts)

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():
    test()

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
