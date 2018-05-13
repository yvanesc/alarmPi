import pygame
import iniPi
import math, sys
import timePi
import ipPi
import rssPi

from pygame.locals import *
from datetime import datetime

from iniPi import *

pygame.init()
myFont = pygame.font.SysFont(iniPi.font, iniPi.font_size) #"monospace", 15)

icO=pygame.image.load(ic16PathS+ "power-standby" +ic16PathE)
icRect=pygame.image.load(ic16PathS+ "volume-high" +ic16PathE)
icTri=pygame.image.load(ic16PathS+ "menu" +ic16PathE)
icX=pygame.image.load(ic16PathS+ "contrast" +ic16PathE)
icUp=pygame.image.load(ic16PathS+ "lightbulb" +ic16PathE)
icDown=pygame.image.load(ic16PathS+ "cog" +ic16PathE)
rayFace =pygame.image.load("/home/pi/pjtSmScr/icon/raymond.png")
picsPath ="/home/pi/alarmPi/pics/"
simps=pygame.image.load(picsPath+"meSimps.png")
miaou=pygame.image.load(picsPath+"miaou.jpg")
noo=pygame.image.load(picsPath+"nope.png")
sleep=pygame.image.load(picsPath+"sleep.jpg")
wake=pygame.image.load(picsPath+"wake.jpg")

size = 180 #200 #224.0

def roint(num):
    return int(round(num))

# page default all button 0
def n00000(DISPLAY):
        #DISPLAYSURF.blit(splashScr, (0, 0))
	#pygame.display.update()
        #time.sleep(30)
        
    DISPLAY.fill(WHITE)
    for hour in range(12):
        cos = math.cos(math.radians(360.0 / 12 * hour))
        sin = math.sin(math.radians(360.0 / 12 * hour))
        x_h_0 = roint(size/2 + size/15*cos*4)
        y_h_0 = roint(size/2 + size/15*sin*4)
        x_h_1 = roint(size/2 + size/3*cos)
        y_h_1 = roint(size/2 + size/3*sin)
        pygame.draw.line(DISPLAY, RED,[x_h_0,y_h_0],[x_h_1,y_h_1],3)
        
    for minute in range(60):
        cos = math.cos(math.radians(360.0 / 60 * minute))
        sin = math.sin(math.radians(360.0 / 60 * minute))
        x_m_0 = roint(size/2 +size/13*cos*4)
        y_m_0 = roint(size/2 + size/13*sin*4)
        x_m_1 = roint(size/2 + size/3*cos)
        y_m_1 = roint(size/2 + size/3*sin)
        pygame.draw.line(DISPLAY, RED,[x_m_0 ,y_m_0],[x_m_1 ,y_m_1],2)

    second = float(datetime.now().second)
    minute = float(datetime.now().minute)
    hour = float(datetime.now().hour)
    hourNum = str(datetime.now().hour)
    minuteNum = str(datetime.now().minute)
    # Second
    angle = 6 * second - 90
    x = size/2 + 9*size/30 * math.cos(math.radians(angle))
    y = size/2 + 9*size/30 * math.sin(math.radians(angle))
    pygame.draw.line(DISPLAY, BLACK,[size/2,size/2],[x, y],3)
    # Minute Hand
    angle = 6 * minute + second/10 - 90
    x = size/2 + 8*size/30 * math.cos(math.radians(angle))
    y = size/2 + 8*size/30 * math.sin(math.radians(angle))
    pygame.draw.line(DISPLAY, BLACK,[size/2,size/2],[x, y],5)
    # Second Hand
    angle = 30 * (hour%12) + 5*minute/10 - 90
    x = size/2 + 6*size/30 * math.cos(math.radians(angle))
    y = size/2 + 6*size/30 * math.sin(math.radians(angle))
    pygame.draw.line(DISPLAY, BLACK,[size/2,size/2],[x, y],10)

    # The Clock
    pygame.draw.circle(DISPLAY, RED, (roint(size/2), roint(size/2)),roint(size/3), 3)        

    DISPLAY.blit(icO, (icOPosX, icOPosY))
    DISPLAY.blit(icRect, (icRectPosX, icRectPosY))
    DISPLAY.blit(icTri, (icTriPosX, icTriPosY))
    DISPLAY.blit(icX, (icXPosX, icXPosY))
    DISPLAY.blit(icDown, (icDownPosX, icDownPosY))
    DISPLAY.blit(icUp, (icUpPosX, icUpPosY))
    if int(minuteNum)<10:
        minuteNum= "0" + str(minuteNum)
    label = myFont.render(hourNum+":"+minuteNum, True, BLACK)
    DISPLAY.blit(label, (66,5))
    label1 = myFont.render(timePi.dayOfWeek, True, BLACK)
    DISPLAY.blit(label1, (160,5))
    label2 = myFont.render(timePi.nowMonth, True, BLACK)
    DISPLAY.blit(label2, (160,25))
    label3 = myFont.render(timePi.nbMonth, True, BLACK)
    DISPLAY.blit(label3, (160,45))
    label4 = myFont.render(timePi.nowYear, True, BLACK)
    DISPLAY.blit(label4, (160,65))
    label6 = myFont.render("Wlan :", True, BLACK)
    DISPLAY.blit(label6, (160,90))
    wlan2find = ipPi.getIp(b"wlan0")
    label5 = myFont.render(wlan2find, True, BLACK)
    DISPLAY.blit(label5, (160,110))
    chkNet = ipPi.checkNet()
    label7 = myFont.render(chkNet, True, BLACK)
    DISPLAY.blit(label7, (160,130))
    label8 = myFont.render("News :", True, BLACK)
    DISPLAY.blit(label8, (160,150))
    label9 = myFont.render(rssPi.newsUpdate(0), True, BLACK)
    DISPLAY.blit(label9, (20,170))
    label10 = myFont.render(rssPi.newsUpdate(1), True, BLACK)
    DISPLAY.blit(label10, (20,190))
    label11 = myFont.render(rssPi.newsUpdate(2), True, BLACK)
    DISPLAY.blit(label11, (20,210))
    pygame.display.flip()
