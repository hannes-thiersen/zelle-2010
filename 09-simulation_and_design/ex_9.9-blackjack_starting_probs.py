# File:            ex_9.9-blackjack_starting_probs.py
# Date:            2019-12-29
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   A blackjack dealer always starts with one card showing. It would be useful
#   for a player to know the dealer's bust probability (see previous problem)
#   for each possible starting value. Write a simulations program that runs
#   multiple hands of blackjack for each possible starting value. Write a
#   simulation program that runs multiple hands of blackjack for each value
#   (ace - 10) and estimates the probability that the dealer busts for each
#   starting value.

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from random import choice

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def description():
    print("Simulating the dealer in Blackjack (21).")
    print("Estimating the dealer's outcome probabilities for each starting \
value.")

#------------------------------------------------------------------------------
def getInput():
    ngames = input("Number of games to simulate: ") or "100"
    return eval(ngames)


#------------------------------------------------------------------------------
def simNGames(start, has_ace, games=100):
    blackjacks = 0
    busts = 0
    for _ in range(games):
        outcome = simBlackjack(start, has_ace)
        if outcome < 0:
            busts += 1
        elif outcome > 0:
            blackjacks += 1
    return busts, blackjacks

#------------------------------------------------------------------------------
def simBlackjack(start, has_ace):

    hand = start

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
def printSummary(outcomes, total):
    form = "{start:^5} | {busts:>7.1%} | {blackjacks:>7.1%}"
    header = "{start:^5} | {busts:^7} | {blackjacks:^7}" .format(
            start="Start", busts="Busts", blackjacks="Blackjacks")
    print(f"\n{header}")
    print("-"*len(header))

    for start in sorted(outcomes.keys()):
        busts, blackjacks = outcomes[start]
        print(form.format(
            start=start, busts=busts/total, blackjacks=blackjacks/total))
    print()

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():

    description()
    #total = getInput() -> input not needed
    total = 10**6
    outcomes = {}

    for start in range(2,12):
        if start == 11:
            has_ace = True
        else:
            has_ace = False

        busts, blackjacks = simNGames(start, has_ace, games=total)
        outcomes[start] = (busts, blackjacks)

    printSummary(outcomes, total)

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
