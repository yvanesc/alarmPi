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
import butPi

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
#pygame.display.set_caption(versionTitle)
# 2 put in iniPi
#str2search = "Main"
DISPLAYSURF = pygame.display.set_mode((scrW, scrH), pygame.NOFRAME)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pygame.mouse.set_visible(False)

clock = pygame.time.Clock()
menuTxt = sqlPi.reqMainMenu("menu","Main")  
sec2Start = int(datetime.datetime.now().strftime("%S"))


while True:
        os.system('clear')        
        #display background
		
		#display button 1-4 & 5-6
		
		#display center
        displayPi.scrSaveClock(DISPLAYSURF,scrW,scrH)
        displayPi.scrLeftButt(DISPLAYSURF,scrW,scrH)

        pygame.display.update()
        clock.tick(60)  # Limit the frame rate to 60 FPS.

        if (not GPIO.input(5)):
                # X
                butPi.croi()
        if (not GPIO.input(22)):
                # rect     
                butPi.rect()
        if (not GPIO.input(24)):
                # triangle                
                butPi.tria()
        if (not GPIO.input(23)):
                # O
                butPi.rond()     
        if (not GPIO.input(4)):
                #VOL LOW                
                butPi.low()
        if (not GPIO.input(17)):
                #VOL HIGH                
                butPi.high()
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()    

        time.sleep(0.1)