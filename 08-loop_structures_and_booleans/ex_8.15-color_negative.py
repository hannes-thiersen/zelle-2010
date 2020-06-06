# File:            ex_8.15-color_negative.py
# Date:            2019-12-20
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   Write a program to convert an image to its color negative. The general form
#   of the program will be similar to that of the previous problem. The
#   negative of a pixel is formed by subtracting each color value from 255. So
#   the new pixel colr is colr_rgb(255-r, 255-g, 255-b)

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from graphics import *

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def getImage():
    #imagefile = input("Insert filename to convert: ")
    imagefile = "fear-of-love.gif"
    image = Image(Point(0,0), imagefile)
    return image, image.getWidth(), image.getHeight(),

#------------------------------------------------------------------------------
def showImage(image, width, height):

    win = GraphWin("Convert to grayscale", width, height )
    image.move(width//2, height//2)
    image.draw(win)
    return win

#------------------------------------------------------------------------------
def prompt(window, anchor, message="prompt"):
    textprompt = Text(anchor, message)
    textprompt.draw(window)
    click = window.getMouse()
    textprompt.undraw()

#------------------------------------------------------------------------------
def convert(window, image):

    rows = image.getHeight()
    columns = image.getWidth()

    for i in range(rows):
        for j in range(columns):
            #r, g, b = image.getPixel(j, i)
            r, g, b = colorNegative(*image.getPixel(j, i))
            image.setPixel(j, i, color_rgb(r, g, b))
        window.update()

#------------------------------------------------------------------------------
def colorNegative(r,g,b):
    return 255 - r, 255 - g, 255 - b

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():

    image, width, height = getImage()
    window = showImage(image, width, height)
    prompt(
            window,
            Point(width//2, height//2),
            message="Click to convert to color negative",
            )
    convert(window, image)
    prompt(
            window,
            Point(width//2, height//2),
            message="Click to exit",
            )

#------------------------------------------------------------------------------
if __name__ == '__main__':

    main()
