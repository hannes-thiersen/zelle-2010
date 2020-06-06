# File:            ex_10.4-three_button_monte.py
# Date:            2020-03-21
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   Extend the program from the previous problem by allowing the player to play
#   multiple rounds and displaying the number of wins and losses. Add a "Quit"
#   button for ending the game.
#
#   Previous problem:
#   -----------------
#   Write a program to play "Three Button Monte." Your program should draw
#   three buttons labeled "Door 1", "Door 2" and "Door 3" in a window and
#   randomly select one of the buttons (without telling the user which one is
#   selected). The program then prompts the user to click on one of the
#   buttons. A click on the special button is a win, and a click on one of the
#   other two is a loss. You should tell the user whether they won or lost, and
#   in the case of a loss, which was the corect button. Your program should be
#   entriely graphical; that is, all prompts and messages should be displayed
#   in the graphics window.

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from button import Button
from graphics import GraphWin, Point, Text
from random import choice

#------------------------------------------------------------------------------
# CLASSES
#------------------------------------------------------------------------------
class Game():

    def __init__(self, win):
        """
        Create three doors (Button's) with and make one the special door to
        find.
        """
        self.infobox = Text(Point(6, 9), "Find the special door...")
        self.infobox.draw(win)
        self.wincount = Text(Point(13, 9), "Wins: 0/0")
        self.wincount.draw(win)
        self.doors = [
                Button(win, Point( 3.0, 5), 3, 5, "Door 1"),
                Button(win, Point( 7.5, 5), 3, 5, "Door 2"),
                Button(win, Point(12.0, 5), 3, 5, "Door 3"), ]
        self.activateDoors()
        self.special = choice(self.doors)
        self.wins = 0
        self.rounds = 0

    def activateDoors(self):
        """ Activate game doors. """
        for door in self.doors:
            door.activate()

    def deactivateDoors(self):
        """ Activate game doors. """
        for door in self.doors:
            door.deactivate()

    def doorClicked(self, click):
        """ Return True if door was clicked and False otherwise.  """
        hit = False
        for door in self.doors:
            hit = hit or door.clicked(click)
        return hit

    def doorPicked(self, click):
        """
        Return True if door was picked or False otherwise. Also implement win
        condition if special door was picked and lose condition if otherwise.
        """
        if self.special.clicked(click):
            self.win()
            return True
        elif self.doorClicked(click):
            self.lose()
            return True
        else:
            return False

    def lose(self):
        """ Implement when right door was chosen. """
        self.deactivateDoors()
        self.special.activate()
        self.rounds += 1
        self.infobox.setText("Oof! Sorry, wrong door.")
        self.updateWincount()

    def reset(self):
        """ Reset the doors and choose a new special door.  """
        self.activateDoors()
        self.special = choice(self.doors)
        self.infobox.setText("Find the special door...")

    def result(self):
        """ Return the result of the game.  """
        return self.win

    def updateWincount(self):
        """ Update wincount text box. """
        self.wincount.setText(f"Wins: {self.wins}/{self.rounds}")

    def win(self):
        """ Implement when right door was chosen. """
        self.deactivateDoors()
        self.special.activate()
        self.rounds += 1
        self.wins += 1
        self.infobox.setText("Winner!!")
        self.updateWincount()

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():

    # create application window
    win = GraphWin("Three Door Monte", 600, 400)
    win.setCoords(0, 0, 15, 10)
    win.setBackground("darkgrey")

    # create game
    doorMonte = Game(win)

    # create replay and quit button
    quitbutton = Button(win, Point(11.25, 1), 3, 1.5, "Quit")
    quitbutton.activate()
    replay = Button(win, Point(3.75, 1), 3, 1.5, "Replay")

    # event loop
    click = win.getMouse()
    while not quitbutton.clicked(click):
        if doorMonte.doorPicked(click):
            replay.activate()
        elif replay.clicked(click):
            doorMonte.reset()
        click = win.getMouse()

    win.close()

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
