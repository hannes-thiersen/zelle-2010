# File:            blackjack.py
# Date:            2019-12-29
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   Blackjack (twenty-one) is a casino game played with cards. The goal of the
#   game is to draw cards that total as close to 21 points as possible without
#   going over. All face cards count as 10 points, aces count as 1 or 11, and
#   all other cards count their numeric value.
#
#   The game is played against a dealer. The player tries to get closer to 21
#   (without going over) than the dealer. If the dealer busts (goes over 21),
#   the player automatically wins (provided the player had not already busted).
#   The dealer must always take cards according to a fixed set of rules. The
#   dealer takes cards until he or she achieves a total of at least 17. If the
#   dealer's hand contains an ace, it will be counted as 11 when that results
#   in a total between 17 and 21 inclusive; otherwise, the ace is counted as 1.
#
#   Write a program that simulates multiple games of blackjack and estimates
#   the probability that the dealer will bust. Hints: treat the deck of cards
#   as infinite (casinos use a "shoe" containing many decks). You do not need
#   to keep track of the cards in the hand, just the total so far (treating an
#   ace as 1) and a bool variable `hasAce` that tells whether or not the hand
#   contains an ace. A hand containing an ace should have 10 points added to
#   the total exactly when doing so would produce a stopping total (something
#   between 17 and 21 inclusive).

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from random import choice

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def description():
    print("Simulating the dealer in Blackjack (21).")

#------------------------------------------------------------------------------
def getInput():
    ngames = input("Number of games to simulate: ") or "100"
    return eval(ngames)


#------------------------------------------------------------------------------
def simNGames(games=100):
    blackjacks = 0
    busts = 0
    for i in range(games):
        outcome = simBlackjack()
        if outcome < 0:
            busts += 1
        elif outcome > 0:
            blackjacks += 1
    return busts, blackjacks

#------------------------------------------------------------------------------
def simBlackjack():

    hand = 0
    has_ace = False

    while hand < 17:
        hand, has_ace = hit(hand, has_ace)

    if hand > 21:
        return -1
    elif hand == 21:
        return 1
    return 0

#------------------------------------------------------------------------------
def hit(hand, has_ace):

    card = choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])
    hand += card

    if has_ace and hand > 21:
        hand -= 10
        has_ace = False
    elif card == 1 and not has_ace:
        if hand + 10 <= 21:
            hand += 10
            has_ace = True

    return hand, has_ace

#------------------------------------------------------------------------------
def printSummary(busts, blackjacks, total):
    print((
        f"Dealer busted {busts} and blackjacked {blackjacks} out of {total} games."
        f"\nBust rate: {busts/total:.1%}"
        f"\nBlackjack rate: {blackjacks/total:.1%}"
        ))

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():

    description()
    total = getInput()
    busts, blackjacks = simNGames(games=total)
    printSummary(busts, blackjacks, total)

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
