# File:          lightning_distance-progex3.4.py
# Date:          2019-09-26
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 3.4
# Description:
#   Writ a program that determines the distance to a lightning strike based on
#   the time elapsed between the flash and the sound of thunder. The speed of
#   sound is approximately 1100ft/sec and 1 mile is 5280 ft.
#
#       sos = 335.28 meter/sec

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    print("Calculate the distance to a lightning strike.")
    time_delta = eval(input("Insert the time between the light and sound: "))
    distance = time_delta * 335.28
    print("The approximate distance to the lightning strike:", distance)

#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
