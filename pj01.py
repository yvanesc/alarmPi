import time
import RPi.GPIO as GPIO
import pygame, sys, os
import iniPi
import sqlPi
import ipPi
import timePi
import splashPi
import pagePi

from pygame.locals import *
from iniPi import * 


os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()

DISPLAYSURF = pygame.display.set_mode((320, 480))
#splashPi.disSplash(DISPLAYSURF)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27,GPIO.OUT)

fontSel=pygame.font.SysFont(iniPi.font, iniPi.font_size)

# DISPLAYSURF.fill(iniPi.WHITE)
# pygame.display.update()
GPIO.output(27,GPIO.HIGH)
pygame.mouse.set_visible(False)

while True:
        os.system('clear')
        #clkX+=1
        #clkRect+=1
        #def page+clkX + clkRect +
        #calMenu = "n" +str(clkX)+ str(clkRect) +str(clkTri)+str(clkUp)+str(clkDown)
        pagePi.askP (clkX, clkRect, clkTri, clkUp, clkDown, DISPLAYSURF)
        #pagePi.n+str(clkX)+ str(clkRect) +str(clkTri)+str(clkUp)+str(clkDown)(DISPLAYSURF)
        if (not GPIO.input(5)):
                # X limit 1 level
                if clkX==1:
                    clkX =0
                else:
                    clkX+=1
                # pygame.display.update()
        if (not GPIO.input(22)):
                # rect
                if clkRect==1:
                    clkRect =0
                else:
                    clkRect+=1                
                #pygame.display.update()
        if (not GPIO.input(23)):
                # O
                #pygame.quit()
                #sys.exit()
                if clkRect==1:
                    clkRect =0
                else:
                    clkRect+=1
        if (not GPIO.input(24)):
                # triangle
                if clkTri==1:
                    clkTri =0
                else:
                    clkTri+=1                  
                #pygame.display.update()
        if (not GPIO.input(4)):
                #VOL LOW
                if clkDown==1:
                    clkDown =0
                else:
                    clkDown+=1                 
                #GPIO.output(27,GPIO.HIGH)
        if (not GPIO.input(17)):
                #VOL HIGH
                if clkUp==1:
                    clkUp =0
                else:
                    clkUp+=1                
                #GPIO.output(27,GPIO.LOW)
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        #sys.exit()

        time.sleep(0.1)
