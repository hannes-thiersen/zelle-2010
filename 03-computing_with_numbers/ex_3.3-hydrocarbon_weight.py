# File:          hydrocarbon_weight-progex3.3.py
# Date:          2019-09-26
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 3.3
# Description:
#   Write a program that dtermines the molocular weight of a hydrocarbon based
#   on the number of hydrogen, carbon, and oxygen atoms. You should use the
#   following weights:
#
#       Atom    Weight (grams/mole)
#        H       1.0079
#        C       12.011
#        O       15.994

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    print("Calculate the molecular weight of a hydrocarbon.")
    hydrogen = eval(input("Enter the amount of hydrogen (H): "))
    carbon = eval(input("Enter the amount of carbon (C): "))
    oxygen = eval(input("Enter the amount of oxygen (O): "))

    mol_weight = hydrogen*1.0079 + carbon*12.011 + oxygen*15.994

    print("Hydrocarbon molecular weight: ", mol_weight)

#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
