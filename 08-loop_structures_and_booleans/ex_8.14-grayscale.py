# File:            ex_8.14-grayscale.py
# Date:            2019-12-20
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Version:         0.1
# Description:
#   Write a program that converts a color image to grayscale. The user supplies
#   the name of a file containing a GIF or PPM image, and the program loads the
#   image and displays the file. At the click of the mouse, the program
#   converts the image and displays the file. At the click of the mouse, the
#   program converts the image to grayscale. The user is then prompted for a
#   filename to store the grayscale image in.
#
#   You will probably want to go back and review the Image object from the
#   graphics library (Section 4.8.4). The basic idea for converting the image
#   is to go through it pixel by pixel and convert each one from color to an
#   appropriate shade of gray. A gray pixel created by setting its red, green
#   and blue components to have that same brightness. So, color_rgb(0, 0, 0) is
#   black, color_rgb(255, 255, 255) is white, and color_rgb(127, 127, 127) is a
#   gray "halfway" between. You should use a weighted average of the original
#   RGB values to determine the brightness of the gray. Here is the pseudocode
#   for the grayscale algorithm:
#
#   for each row in the image:
#       for each column in the image:
#           r, g, b = get pixel information for current row and column
#           brightness = int(round(0.299r + 0.587g + 0.114b))
#           set pixel to color_rgb(brightness, brightness, brightness)
#       update the image # to see progress row by row
#
#   Note: the pixel operations in the Image class are rather slow, so you will
#   want to use relatively small images (not 12 megapixels) to test your
#   program.

#------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------
from graphics import *
from time import sleep

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
            r, g, b = grayscale(*image.getPixel(j, i))
            image.setPixel(j, i, color_rgb(r, g, b))
        window.update()

#------------------------------------------------------------------------------
def grayscale(r, g, b):
    brightness = int(round(0.299*r + 0.587*g + 0.114*b))
    return brightness, brightness, brightness

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
def main():

    image, width, height = getImage()
    window = showImage(image, width, height)
    prompt(
            window,
            Point(width//2, height//2),
            message="Click to convert to grayscale",
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
