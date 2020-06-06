# File:            ex_7.1-overtime.py
# Date:            2019-12-19
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   Many compoanies pay time-and-a-half for any hours worked above 40 in a
#   given week. Write a program to input the number of hours worked and the
#   hourly rate and calculate the total wages.

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def payment(hours, rate):
    if hours > 40:
        return rate*(1.5 * hours - 20)
        #return 40 * rate + (hours - 40)*rate*1.5
    else:
        return hours*rate

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():

    rate = eval(input("Hourly rate: "))
    hours = eval(input("Hours worked: "))

    wage = payment(hours, rate)

    print(f"Wage: ${wage:0.2f}")

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
