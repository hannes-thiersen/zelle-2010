# File:            ex_10.12-draw_cards.py
# Date:            2020-04-27
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:        10.12
# Description:
#   Extend your card class from the previous problem wit ha draw(self, win,
#   center) method that displays the card in a graphics window. Use your
#   extended class to create and display a hand of five random cards. Hint: the
#   easiest way to do this is to search the internet for a free set of card
#   images and use the Image object in the graphics library to display them.

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from button import Button
from graphics import GraphWin, Point, Image
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
        self.image = None

    def __str__(self):
        rank = self.specials.get(self.rank, self.rank)
        if not rank:
            rank = self.rank
        return f"{rank} of {self.getSuite()}"

    def BJValue(self):
        if self.rank < 10:
            return self.rank
        else:
            return 10

    def draw(self, win, center):
        if not self.image:
            rank = str(self.specials.get(self.rank, self.rank))[0].upper()
            if self.rank == 10:
                rank = str(10)
            suite = self.suit.upper()
            self.image = Image(center, f"cards_pics/{rank + suite}.png")
        self.image.draw(win)

    def getRank(self):
        rank = self.specials(self.rank)
        if rank:
            return rank
        else:
            return self.rank

    def getSuite(self):
        return self.specials.get(self.suit)

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():

    # create the application window
    win = GraphWin("Drawn Cards", width=1500, height=600)
    win.setCoords(0,0,10,3.)
    win.setBackground("gray")

    redrawbutton = Button(win, Point(3., 0.3), 1., .3, "Redraw")
    quitbutton = Button(win, Point(7., 0.3), 1., .3, "Quit")
    redrawbutton.activate()
    quitbutton.activate()

    # TODO: refactor this code that is repeated in the execution loop
    template = " {:17} | {:^9}"
    headers = template.format("Card", "BJ value")
    print(headers)
    print("-"*len(headers))
    for pos in range(5):
        card = Card(randint(1,13), choice(['c', 'd', 'h', 's']))
        print(template.format(str(card), card.BJValue()))
        card.draw(win, Point(1.+ pos*2, 1.8))
    print()

    click = win.getMouse()
    while not quitbutton.clicked(click):
        if redrawbutton.clicked(click):
            print(headers)
            print("-"*len(headers))
            for pos in range(5):
                card = Card(randint(1,13), choice(['c', 'd', 'h', 's']))
                print(template.format(str(card), card.BJValue()))
                card.draw(win, Point(1.+ pos*2, 1.8))
            print()
        click = win.getMouse()

    win.close()

if __name__ == '__main__':
    main()
