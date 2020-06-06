# File:            ex_9.7-craps.py
# Date:            2019-12-28
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   Craps is a dice game played at many casinos. A player rolls a pair of
#   normal six-side dice. If the initial roll is 2, 3, or 12, the player loses.
#   If the roll is 7 or 11, the player wins. Any other initial roll causes the
#   player to "roll for point". That is, the player keeps rolling the dice
#   until either rolling a 7 or re-rolling the value of the initial roll. If
#   the player re-rolls the initial value before rolling a 7 it's a win.
#   Rolling a 7 first is a loss.
#
#   Write a program to simulate multiple games of craps and estimate the
#   probability that the player wins. For example, if the player wins 249 out
#   of 500 games, then the estimated probability of winning is 249/500 = .498.

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from random import randint

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def printIntro():
    print("\n".join([
        "",
        "Simulating 10000 games of craps (dice game in casinos).",
        "",
        ]))

#------------------------------------------------------------------------------
def initialRoll():
    roll = randint(2, 12)
    reroll = 0

    if roll in [7, 11]:
        #gameWon(roll)
        reroll += 1
    elif roll in [2, 3, 12]:
        #gameLost(roll)
        reroll -= 1
    else:
        #print(f"Initial roll: {roll}")
        reroll = 0

    return roll, reroll

#------------------------------------------------------------------------------
def rollForPoint(initial):
    win_lose = 0
    reroll = randint(2,12)
    while not gameOver(initial, reroll):
        reroll = randint(2,12)

    if initial == reroll:
        #gameWon(reroll)
        win_lose += 1
    else:
        #gameLost(reroll)
        win_lose -= 1

    return win_lose

#------------------------------------------------------------------------------
def gameOver(roll, reroll):
    if reroll == 7 or roll == reroll:
        return True
    #print(f"{reroll:>2d}  Again!")
    return False

#------------------------------------------------------------------------------
def gameWon(roll):
    print(f"{roll:>2d}  Congratulations, Win!")

#------------------------------------------------------------------------------
def gameLost(roll):
    print(f"{roll:>2d}  Sorry, Bust!")

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():
    printIntro()
    wins = 0
    total = 10**5
    for i in range(total):
        initial, outcome = initialRoll()
        if outcome == 0:
            outcome = rollForPoint(initial)
        if outcome == 1:
            wins += 1

    print(f"Win rate: {wins/total:3.1%}")

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
