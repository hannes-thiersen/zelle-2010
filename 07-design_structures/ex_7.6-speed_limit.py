# File:            ex_7.6-speed_limit.py
# Date:            2019-12-19
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   The speeding ticket fine policy in Podunksville is $50 plus $5 for each mph
#   over the limit plus a penalty of $200 for any speed over 90 mph. Write a
#   program that accepts a speed limit and a clocked speed and either prints a
#   message indicating the speed was legal or prints the amount of the fine, if
#   the speed is illegal.

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def speedtrap(limit, clocked):
    fine = 0
    if clocked < limit:
        print("Legal speed.")
        return None

    fine += 50 + (clocked - limit)*5
    if clocked > 90:
        fine += 200

    print(f"Illegal speed! Fine: ${fine:0.2f}")

    return None

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():

    try:
        limit, clocked = eval(
                input("Insert speed limit and clocked speed (30, 28): ")
                )
        speedtrap(limit, clocked)

    except SyntaxError:
        print("Input error. Values should be comma seperated.")
    except NameError:
        print("Input error. Input should be numbers.")
    except TypeError:
        print("Input error. Input needs 2 values.")


#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
