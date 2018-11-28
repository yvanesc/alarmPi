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
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27,GPIO.OUT)

fontSel=pygame.font.SysFont(iniPi.font, iniPi.font_size)
fontSelHalf=pygame.font.SysFont(iniPi.font, iniPi.font_sizeSm)
fontSelL=pygame.font.SysFont(iniPi.font, iniPi.font_sizeXXl)

GPIO.output(27,GPIO.HIGH)
pygame.mouse.set_visible(False)

pygame.display.update()
time.sleep(3)
clock = pygame.time.Clock()
while True:
        os.system('clear')
        DISPLAYSURF.fill(iniPi.WHITE)
        time2Display = datetime.datetime.now().strftime("%H:%M")
        hour2Display = int(datetime.datetime.now().strftime("%H"))        
        date2Display = datetime.datetime.now().strftime("%d")
        menuTxtO= fontSelXl.render("Prd", True, iniPi.BLACK)      
        infoTxt2 = fontSelXl.render("Dev", True, iniPi.BLACK)          
        infoTxt3 = fontSelXl.render("Git pull", True, iniPi.BLACK)      
        infoTxt4 = fontSelXl.render("Exit", True, iniPi.BLACK)      
                 
        
        #screen
        DISPLAYSURF.blit(icO, (icOPosX, icOPosY))
        DISPLAYSURF.blit(icX, (icXPosX, icXPosY))
        DISPLAYSURF.blit(icDown, (icDownPosX, icDownPosY))
        DISPLAYSURF.blit(icUp, (icUpPosX, icUpPosY))        
                
        DISPLAYSURF.blit(menuTxtO, (32, 80))
        DISPLAYSURF.blit(infoTxt2, (32, 140))
        DISPLAYSURF.blit(infoTxt3, (32, 160))
        DISPLAYSURF.blit(infoTxt4, (32, 180))
        

        pygame.display.update()
        clock.tick(60)  # Limit the frame rate to 60 FPS.

        if (not GPIO.input(5)):
                # X
                #clkX+=1
                pygame.quit()               
            
        if (not GPIO.input(23)):
                # pygame
                # O
                O.quit()
                sys.exit()
            
        if (not GPIO.input(4)):
                #VOL LOW
                #clkDown+=1
                pygame.mixer.music.load('/home/pi/alarmPi/sound/cartoon002.wav')
                pygame.mixer.music.play(0)                
                #autoMntUsbT01.run_command()
        if (not GPIO.input(17)):
                #VOL HIGH
                #clkUp
                pygame.mixer.music.load('/home/pi/alarmPi/sound/wake-up.mp3')
                pygame.mixer.music.play(0)                
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()                

        time.sleep(0.1)