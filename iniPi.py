#iniPi
#import pygame, sys, os
#Pygame

import random

#Title window
versionTitle = "AlarmPi Ver. 0.1"

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
GREY =  (112, 128, 144)
GREYDARK = (47, 79, 79)
YELLOW = (255, 255, 0)

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

#alarm
#alarm2Display="06:00"
flAlarm = 0
alarmOn = 0
alarmOff = 0
alHour = 6
alMin = 0
alMon = 1
alTue = 1
alWed = 1
alThu = 1
alFri = 1
alSat = 0
alSun = 0

#timer
timerSc = 10
timerStart = 0

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
#type menu/Action
typeAct = 0

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

#scan 
startSc = 0

#screen saver snow
snFlake = 0
snowOnTime = 0
widthRect = 0
heigthRect = 0
snow_list = []

#list bluetooth

#position & size
#pos = (  x,   y,   width, high)
#get screen size
# def getPosSize(pos,scrW,scrH):
# 	switch (pos){
# 		case 1: return (0,0,scrW/8,scrH/4);
# 				break;
# 		case 2: return (0,scrH/4,scrW/8,scrH/4);
# 				break;
# 		case 3: return (0,scrH/2,scrW/8,scrH/4);
# 				break;
# 		case 4: return (0,(scrH/4)*3,scrW/8,scrH/4);
# 				break;
# 		case 5: return (scrW/8,0,scrW/2 - scrW/8,scrH/2);
# 				break;
# 		case 6: return (scrW/8,scrH/2,scrW/2 - scrW/8,scrH/2);
# 				break;
# 		case 7: return (scrW/2,0,scrW/2 - scrW/8,scrH/2);
# 				break;
# 		case 8: return (scrW/2,scrH/2,scrW/2 - scrW/8,scrH/2);
# 				break;
# 		case 9: return (scrW-scrW/8,0,scrW/8,scrH/4);
# 				break;
# 		case 10: return (scrW-scrW/8,scrH/4,scrW/8,scrH/2);
# 				break;
# 		case 11: return (scrW-scrW/8,(scrH/4)*3,scrW/8,scrH/4);
# 				break;
# 	}