# File:            rball.py
# Date:            2019-12-22
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   Simulation of racquet ball rallys.

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from random import random

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def printIntro():
    print(
            "\n".join([
        f"This program simulates a game of racquetball between two",
        f"players called 'A' and 'B'. The abilities of each player is",
        f"indicated by a probability (a number between 0 and 1) that",
        f"the player wins the point when serving. Player A always has",
        f"the first serve.",
        ]))

#------------------------------------------------------------------------------
def getInputs():
    # Returns the three simulation parameters
    a = eval(input("What is the prob. player A wins a serve? "))
    b = eval(input("What is the prob. player B wins a serve? "))
    n = eval(input("How many games to simulate? "))
    return a, b, n

#------------------------------------------------------------------------------
def simNGames(n, probA, probB):
    # Simulates n games of racquetball between players whose abilities are
    # represented by the probability of winning a serve.
    # Returns number of wins for A and B
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB

#------------------------------------------------------------------------------
def simOneGame(probA, probB):
    # Simulates one game of racquetball between players whose abilities are
    # represented by the probability of winning a serve.
    # Returns final scores for A and B
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB

#------------------------------------------------------------------------------
def gameOver(a, b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, False otherwise.
    return a==15 or b==15

#------------------------------------------------------------------------------
def printSummary(winsA, winsB):
    # Prints a summary of wins for each player.
    n = winsA + winsB
    print("\nGames simulated:", n)
    print(f"Wins for A: {winsA} ({winsA/n:0.1%})")
    print(f"Wins for B: {winsB} ({winsB/n:0.1%})")

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n ,probA, probB)
    printSummary(winsA, winsB)

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
