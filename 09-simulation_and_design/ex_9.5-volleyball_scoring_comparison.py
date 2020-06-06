# File:            ex_9.4-volleyball_scoring_comparison.py
# Date:            2019-12-28
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   Design and implement a system that compares regular volleyball games to
#   those using rally scoring. Your program should be able to investigate
#   whether rally scoring magnifies, reduces, or has no effect on the relative
#   advantage enjoyed by the better team.
#
#   The rally scoring system is very much similar to the classic scoring, but
#   does consistently slightly reduce the advantage of the better team.

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from random import random

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def printIntro():
    print("\n".join([
        "Comparison of two scoring systems for volleyball by simulation.",
        "Probabilities for team A and B to score when serving are given",
        "as input.",
        "Team A serves first in odd numbered games and team B in even",
        "numbered games. Classic games are won by score at least 15 points",
        "while rally games require at least 25. Both scoring systems require",
        "a winning margin of 2 points to win."
        ]))

#------------------------------------------------------------------------------
def getInputs():
    probA = eval(input("Probability for team A to score on a serve: "))
    probB = eval(input("Probability for team B to score on a serve: "))
    games = eval(input("Number of games to simulate: "))
    return probA, probB, games

#------------------------------------------------------------------------------
def simClassicGame(probA, probB, serve="A"):
    scoreA = scoreB = 0

    while not gameOverClassic(scoreA, scoreB):
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
def gameOverClassic(a, b):
    return (a>=15 or b>=15) and ( abs(a-b) >= 2)

#------------------------------------------------------------------------------
def printSummary(probA, probB, classicA, classicB, rallyA, rallyB):
    total = classicA + classicB
    form = "{:>16}: {:^7.1%} {:^7.1%}"
    print("{:>16}  {:^7} {:^7}".format("", "A", "B"))
    print(form.format("Prob on serve", probA, probB))
    print(form.format("Classic win rate", classicA/total, classicB/total))
    print(form.format("Rally win rate", rallyA/total, rallyB/total))

#------------------------------------------------------------------------------
def simRallyGame(probA, probB, serve="A"):
    scoreA = scoreB = 0

    while not gameOverRally(scoreA, scoreB):
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
def simNGames(probA, probB, games=10, scoring="classic"):

    if scoring == "classic":
        simGame = simClassicGame
    elif scoring == "rally":
        simGame = simRallyGame
    else:
        raise ValueError("Invalid scoring given.")

    winsA = winsB = 0

    for i in range(games):

        if i%2:
            serve = "A"
        else:
            serve = "B"

        scoreA, scoreB = simGame(probA, probB, serve=serve)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1

    return winsA, winsB

#------------------------------------------------------------------------------
def gameOverRally(a, b):
    return (a>=25 or b>=25) and ( abs(a-b) >= 2)

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():
    print()
    printIntro()

    print()
    teamAprob, teamBprob, games = getInputs()

    print()
    classic_winsA, classic_winsB = simNGames(
            teamAprob, teamBprob, games=games, scoring="classic")
    rally_winsA, rally_winsB = simNGames(
            teamAprob, teamBprob, games=games, scoring="rally")
    printSummary(
            teamAprob, teamBprob,
            classic_winsA, classic_winsB,
            rally_winsA, rally_winsB)
    print()

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
