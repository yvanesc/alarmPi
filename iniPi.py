#iniPi
#import pygame, sys, os
#Pygame
# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
GREY =  (112, 128, 144)
GREYDARK = (47, 79, 79)

# ini font
font_color = (BLACK)
font = None
font_size = 30
font_sizeSm = 25
font_sizeL = 35
font_sizeXl = 40
font_sizeXXl = 45
font_sizeB = 90
font_sizeA = 70

#move
angleRot = 0

#menu
timerMenu=30
posMenu =20
spaceMenu = 60
posCur = 20

#button state
dayNight = 0
reverse = 0
# frame
marge = 8
# position Y for button
posButX = posButDw = 220
posButTri = 150
posButRect = 75
posButO = posButUp = 2

# button
clkX = clkRect = clkTri = clkUp = clkDown = 0 

# screen 2.2 inch 320x240
# split screen with 20x60 pixel
# use for icon 32x32 2 blocks (40x60)
scrWidth = 320
scrWidthB = 640
scrHeigth = 240
scrHeigthB = 480

""" position for icon 32x32
icOPosX = icRectPosX = icTriPosX = icXPosX = 2
icOPosY = icUpPosY = 5
icRectPosY = 70
icTriPosY = 150
icXPosY = icDownPosY = 205
icDownPosX = icUpPosX = 280
"""

# position 4 icon 16x16

icOPosX = icRectPosX = icTriPosX = icXPosX = 2
icOPosY = icUpPosY = 5
icRectPosY = 70
icTriPosY = 150
icXPosY = icDownPosY = 205
icDownPosX = icUpPosX = 300 #280 

# path 4 icon 32x32
pathStart="/home/pi/alarmPi/ic32/"
# end of filename
pathEnd="-4x.png"

# path 4 icon 16x16
ic16PathS ="/home/pi/alarmPi/ic16/"
# end of filename
ic16PathE="-2x.png"

ic32PathS ="/home/pi/alarmPi/ic32/"
ic32PathE="-4x.png"
ic32PathR ="/home/pi/alarmPi/ic32rev/"
#pygame
#fontSel=pygame.font.SysFont(font, font_size)
