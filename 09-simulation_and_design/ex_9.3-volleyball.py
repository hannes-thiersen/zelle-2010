# File:            ex_9.3-volleyball.py
# Date:            2019-12-27
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   Design and implement a simulation of the game of volleyball. Normal
#   volleyball is played like racquetball, in that a team can only score points
#   when it is serving. Games are played to 15, but must be won by at least two
#   points.

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from random import random

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def printIntro():
    print("\n".join([
        "Simulation of one game of volleyball given the probabilities of",
        "team A and B to score a point when serving. Team A always serves",
        "first. The game is won by scoring at least 15 points with a winning",
        "margin of 2 points."
        ]))

#------------------------------------------------------------------------------
def getInputs():
    probA = eval(input("Probability for team A to score on a serve: "))
    probB = eval(input("Probability for team B to score on a serve: "))
    return probA, probB

#------------------------------------------------------------------------------
def simGame(probA, probB):
    scoreA = scoreB = 0
    serve = "A"

    while not gameOver(scoreA, scoreB):
        if serve == "A":
            if random() < probA:
                scoreA += 1
            else:
                serve = "B"
        else:
            if random() < probB:
                scoreB += 1
            else:
                serve = "A"

    return scoreA, scoreB

#------------------------------------------------------------------------------
def gameOver(a, b):
    return (a>=15 or b>=15) and ( abs(a-b) >= 2)

#------------------------------------------------------------------------------
def printSummary(scoreA, scoreB):
    if scoreA > scoreB:
        winner = "A"
    else:
        winner = "B"
    print(f"Final score: A {scoreA} - {scoreB} B")
    print(f"Team {winner} wins")

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():
    printIntro()
    teamAprob, teamBprob = getInputs()
    teamAscore, teamBscore = simGame(teamAprob, teamBprob)
    printSummary(teamAscore, teamBscore)

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
