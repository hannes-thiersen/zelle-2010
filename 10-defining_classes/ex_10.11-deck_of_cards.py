# File:            ex_10.11-deck_of_cards.py
# Date:            2020-04-27
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:        10.11
# Description:
#   Implement a class to represent a plying card. Your class hould have the
#   following methods:
#
#   __init__(self, rank, suit) rank is an int in the range 1-13 indicating the
#       ranks Ace-King, and suit is a singel character 'd', 'c', 'h' or 's'
#       indicating the suit (diamonds, clubs, hearts, spades). Create the
#       corresponding card.
#
#   getRank(self) Returns the rank of the card.
#
#   getSuite(self) Returns the suit of the card.
#
#   BJValue(self) Returns the Blackjack value of a card. Ace counts as 1, face
#   cards count as 10.
#
#   __str__(self) Returns a string that names the card. For example, "Ace of
#       Spades".
#
#   Notice: A method named __str__ is special in Python. If asked to convert an
#   object into a string, Python uses this method, if it's present. For
#   example,
#
#   c = Card(1,'s')
#   print c
#
#   will print "Ace of Spades"
#
#   Test your card class with a program that print out n randomly generated
#   cards and the associated Blackjack value where n is a number supplied by
#   the user.

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from random import choice, randint

#------------------------------------------------------------------------------
# CLASSES
#------------------------------------------------------------------------------
class Card():

    specials = {
            1: "Ace",
            11: "Jack",
            12: "Queen",
            13: "King",
            'c': "Clubs",
            'd': "Diamonds",
            'h': "Hearts",
            's': "Spades",
            }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        rank = self.specials(self.rank)
        if rank:
            return rank
        else:
            return self.rank

    def getSuite(self):
        return self.specials.get(self.suit)

    def BJValue(self):
        if self.rank < 10:
            return self.rank
        else:
            return 10

    def __str__(self):
        rank = self.specials.get(self.rank)
        if not rank:
            rank = self.rank

        return f"{rank} of {self.getSuite()}"

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():
    template = " {:17} | {:^9}"
    headers = template.format("Card", "BJ value")
    print(headers)
    print("-"*len(headers))
    for _ in range(20):
        card = Card(randint(1,13), choice(['c', 'd', 'h', 's']))
        print(template.format(str(card), card.BJValue()))

if __name__ == '__main__':
    main()
