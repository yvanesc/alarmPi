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
import pygame.display
import actionPi
import soundPi
import displayPi
import bluezPi

pygame.display.init()
scrW = pygame.display.Info().current_w
scrH = pygame.display.Info().current_h

from pygame.locals import *
from iniPi import * 
from git import Repo
#from datetime import timeDelta

repo = Repo("/home/pi/alarmPi")
assert not repo.bare

os.putenv('SDL_FBDEV', '/dev/fb1')

pygame.init()
pygame.display.set_caption(versionTitle)
# 2 put in iniPi
str2search = "Main"
DISPLAYSURF = pygame.display.set_mode((scrW, scrH), pygame.NOFRAME)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)


fontSelL=pygame.font.SysFont(iniPi.font, iniPi.font_sizeB)
fontSel=pygame.font.SysFont(iniPi.font, iniPi.font_sizeA)

pygame.mouse.set_visible(False)

clock = pygame.time.Clock()
menuTxt = sqlPi.reqMainMenu("menu","Main")  
sec2Start = int(datetime.datetime.now().strftime("%S"))

while True:
        os.system('clear')        
        #display grid                
        DISPLAYSURF.fill(WHITE)
        #first 4 row and first col
        #pygame.draw.rect(DISPLAYSURF, RED, (scrW/2,0,(scrW/2)-64,60), 6)
        displayPi.blueScr(DISPLAYSURF,scrW,scrH)
        #(scrW/8)/2 - get_width()/2 // (scrH/4)/2 - get_height()/2
        #DISPLAYSURF.blit(disInfoTxt, ((scrW/16),  (scrH/8)))           
        #center
        
        #last col and 3 row        
        

        pygame.display.update()
        clock.tick(60)  # Limit the frame rate to 60 FPS.

        if (not GPIO.input(5)):
                # X
                print("X")
        if (not GPIO.input(22)):
                # rect     
                print("Rect")
        if (not GPIO.input(24)):
                # triangle                
                print("triangle")
        if (not GPIO.input(23)):
                # O
                print("O")     
        if (not GPIO.input(4)):
                #VOL LOW                
                print ("LOW")
        if (not GPIO.input(17)):
                #VOL HIGH                
                print("HIGH")
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()    

        time.sleep(0.1)