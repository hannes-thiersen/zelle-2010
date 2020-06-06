# File:          convert_table-progex2.4.py
# Date:          2019-09-22
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 2.4
# Description:
#   Modify the `convert.py` program (Section 2.2) so that it computes and
#   prints a table of Celsius temperatures and the Fahrenheit equivalents
#   every 10 degrees from 0C to 100C.

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    print(" {} | {}".format("Celsius", "Fahrenheit"))
    print("-"*20)

    for celsius in range(0,110,10):
        fahrenheit = 9/5 * celsius + 32
        print("{:7.1f}  | {:6.1f}".format(celsius, fahrenheit))


#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()

