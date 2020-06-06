# File:            ex_6.1-old_MacDonald.py
# Date:            2019-12-15
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:        ex 6.1
# Description:
#   Write a program to print the lyrics of the song "Old MacDonald". Your
#   program should print the lyrics for five differenct animals, similar to he
#   example verse below.
#
#       Old MacDonald has a farm, Ee-igh, Ee-igh, Oh!
#       And on that farm he has a cow, Ee-igh, Ee-igh, Oh!
#       With a moo, moo here and a moo, moo there.
#       Here a moo, there a moo, everwhere a moo, moo.
#       Old MacDonald has a farm, Ee-igh, Ee-igh, Oh!

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def macDonald():
    print("Old MacDonald has a farm, Ee-igh, Ee-igh, Oh!")

def song(animal, sound):
    macDonald()
    farmAnimal(animal, sound)
    macDonald()

def farmAnimal(animal, sound):
    print( f"""And on that farm he has a {animal}, Ee-igh, Ee-igh, Oh!
With a {sound}, {sound} here and a {sound}, {sound} there.
Here a {sound}, there a {sound}, everwhere a {sound}, {sound}.""")

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():

    print()
    song("cow", "moo")
    print()
    song("sheep", "bah")
    print()
    song("duck", "quack")
    print()
    song("dog", "woof")
    print()
    song("cat", "meow")
    print()

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
