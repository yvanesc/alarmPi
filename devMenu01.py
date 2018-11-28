import time
import RPi.GPIO as GPIO
import pygame, sys, os
import iniPi
import sqlPi
import ipPi
import timePi
import subprocess
import git
import datetime
import subprocess

from pygame.locals import *
from iniPi import * 
from git import Repo

repo = Repo("/home/pi/alarmPi")
assert not repo.bare

os.putenv('SDL_FBDEV', '/dev/fb1')

#init menu
timerMenu=30
posMenu =50
spaceMenu = 30
infoTxt = ["Prd", "Dev", "Git pull", "Exit"]
posCur = 50

pygame.init()
# 2 put in iniPi
icO=pygame.image.load(ic16PathS+ "power-standby" +ic16PathE)
icX=pygame.image.load(ic16PathS+ "check" +ic16PathE)
icUp=pygame.image.load(ic16PathS+ "caret-top" +ic16PathE)
icDown=pygame.image.load(ic16PathS+ "caret-bottom" +ic16PathE)

DISPLAYSURF = pygame.display.set_mode((scrWidth, scrHeigth))

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(27,GPIO.OUT)

fontSelL=pygame.font.SysFont(iniPi.font, iniPi.font_sizeXXl)

#GPIO.output(27,GPIO.HIGH)
pygame.mouse.set_visible(False)

#pygame.display.update()
#time.sleep(3)
clock = pygame.time.Clock()

while True:
        os.system('clear')
        DISPLAYSURF.fill(iniPi.WHITE)
        time2Display = datetime.datetime.now().strftime("%H:%M")
        hour2Display = int(datetime.datetime.now().strftime("%H"))        
        date2Display = datetime.datetime.now().strftime("%d")        
        
        #timerMenuShow = timerMenu   
        timer2Display = fontSelL.render("Timer : %2d"%  (timerMenu) , True, iniPi.BLACK)  
        for nbrMenu2Dis in range (0, 4):
                disInfoTxt = fontSelL.render(infoTxt[nbrMenu2Dis], True, iniPi.BLACK)
                nb2dis= posMenu +spaceMenu * nbrMenu2Dis                
                DISPLAYSURF.blit(disInfoTxt, (64,  nb2dis))         
        
        #screen        
        pygame.draw.rect(DISPLAYSURF, iniPi.RED, (32,posCur,256,30), 3)
        DISPLAYSURF.blit(icO, (icOPosX, icOPosY))
        DISPLAYSURF.blit(icX, (icXPosX, icXPosY))
        DISPLAYSURF.blit(icDown, (icDownPosX, icDownPosY))
        DISPLAYSURF.blit(icUp, (icUpPosX, icUpPosY))
        #DISPLAYSURF.blit(timer2Display, (64, 210))        
                
        pygame.display.update()
        clock.tick(60)  # Limit the frame rate to 60 FPS.

        if (not GPIO.input(5)):
                # X
                #clkX+=1
                if posCur == 50:
                        os.execl('/home/pi/alarmPi/runProd.sh', '')
                if posCur == 80:
                        os.execl('/home/pi/alarmPi/runDev.sh', '')
                if posCur == 110:
                        g = git.Git('/home/pi/alarmPi')
                        g.pull('origin','master')
                
                        # restart python soft to update change
                        os.execl('/home/pi/alarmPi/runme.sh', '')
                if posCur == 140:
                        pygame.quit()                 

        if (not GPIO.input(23)):
                # pygame
                # O
                O.quit()
                sys.exit()
            
        if (not GPIO.input(4)):
                #VOL LOW
                #clkDown+=1
                if posCur < (50 + 30*(len(infoTxt))):
                        posCur+=30
                
        if (not GPIO.input(17)):
                #VOL HIGH
                #clkUp
                if posCur > 50:
                        posCur-=30                
                
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()    

        #timerMenu = timerMenu - 0.1
        #if (timerMenu < 0):
        #        pygame.quit()
        time.sleep(0.1)