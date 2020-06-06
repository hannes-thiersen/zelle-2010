# File:            ex_9.4-volleyball_rallies.py
# Date:            2019-12-27
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   Most sanctioned volleyball is now played using rally scoring. In this
#   system, the tema taht wins a rally is awareded a point, even if they were
#   not the serving team. Games are played to a score of 25. Design and
#   implement a simulation of volleyball using rally scoring.

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
        "margin of 2 points. Scoring is based on won rallies in this case and",
        "not winning a rally while serving"
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
                scoreB += 1
        else:
            if random() < probB:
                scoreB += 1
            else:
                serve = "A"
                scoreA += 1

    return scoreA, scoreB

#------------------------------------------------------------------------------
def gameOver(a, b):
    return (a>=25 or b>=25) and ( abs(a-b) >= 2)

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
