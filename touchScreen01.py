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

from pygame.locals import *
from iniPi import * 
from git import Repo

repo = Repo("/home/pi/alarmPi")
assert not repo.bare

os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')
pygame.init()
# 2 put in iniPi
icO=pygame.image.load(ic16PathS+ "power-standby" +ic16PathE)
icRect=pygame.image.load(ic16PathS+ "eject" +ic16PathE)
icTri=pygame.image.load(ic16PathS+ "account-logout" +ic16PathE)
icX=pygame.image.load(ic16PathS+ "cog" +ic16PathE)
icUp=pygame.image.load(ic16PathS+ "caret-top" +ic16PathE)
icDown=pygame.image.load(ic16PathS+ "caret-bottom" +ic16PathE)
#rayFace =pygame.image.load("/home/pi/pjtSmScr/icon/raymond.png")
moon =pygame.image.load("/home/pi/alarmPi/ic64/moon.jpg")
sun =pygame.image.load("/home/pi/alarmPi/ic64/sun.png")
splashScr =pygame.image.load("/home/pi/pjtSmScr/wp/coplandOS.jpg")
#pygame.mouse.set_visible(False)
DISPLAYSURF = pygame.display.set_mode((scrWidth, scrHeigth))



fontSel=pygame.font.SysFont(iniPi.font, iniPi.font_size)
fontSelHalf=pygame.font.SysFont(iniPi.font, iniPi.font_sizeSm)
# update button
touch_buttons = {'17 on':(80,60), '4 on':(240,60), '17 off':(80,180), '4 off':(240,180)}

#GPIO.output(27,GPIO.HIGH)
pygame.mouse.set_visible(False)
DISPLAYSURF.blit(splashScr, (0, 0))
pygame.display.update()
time.sleep(3)
clock = pygame.time.Clock()
while True:
        os.system('clear')
        DISPLAYSURF.fill(iniPi.BLACK)
            
        # button 1 fct only (shutdown)
        
        #screen
        if (hour2Display<8 and hour2Display>20):
                DISPLAYSURF.blit(sun, (224, 160))
        else:
                DISPLAYSURF.blit(moon, (224, 160))
        # update button
        for k,v in touch_buttons.items():
                text_surface = fontSel.render('%s'%k, True, WHITE)
                rect = text_surface.get_rect(center=v)
                DISPLAYSURF.blit(text_surface, rect)

        pygame.display.update()
        clock.tick(60)  # Limit the frame rate to 60 FPS.


        for event in pygame.event.get():
                #if event.type == QUIT:
                        #pygame.quit()
                        #sys.exit()
                if(event.type is MOUSEBUTTONDOWN):
                        pos = pygame.mouse.get_pos()
                        print (pos)
                elif(event.type is MOUSEBUTTONUP):
                        pos = pygame.mouse.get_pos()
                        print (pos)
                        #Find which quarter of the screen we're in
                        x,y = pos
                        if y < 120:
                                if x < 160:
                                        #GPIO.output(17, False)
                                        print("17")
                                else:
                                        #GPIO.output(4, False)
                                        print("4")   
                        else:
                                if x < 160:
                                        #GPIO.output(17, True)
                                        print("17")
                                else:
                                        #GPIO.output(4, True)
                                        print("17")

        time.sleep(0.1)
