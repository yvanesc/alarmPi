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
# Clean before start
#g = git.Git('alarmPi')
#g.pull('origin','master')
#os.execl('/home/pi/alarmPi/runme.sh', '')

os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()
# 2 put in iniPi
icO=pygame.image.load(ic16PathS+ "power-standby" +ic16PathE)
icRect=pygame.image.load(ic16PathS+ "eject" +ic16PathE)
icTri=pygame.image.load(ic16PathS+ "account-logout" +ic16PathE)
icX=pygame.image.load(ic16PathS+ "cog" +ic16PathE)
icUp=pygame.image.load(ic16PathS+ "caret-top" +ic16PathE)
icDown=pygame.image.load(ic16PathS+ "caret-bottom" +ic16PathE)
rayFace =pygame.image.load("/home/pi/pjtSmScr/icon/raymond.png")
splashScr =pygame.image.load("/home/pi/pjtSmScr/wp/coplandOS.jpg")
#pygame.mouse.set_visible(False)
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

# DISPLAYSURF.fill(iniPi.WHITE)
# pygame.display.update()
GPIO.output(27,GPIO.HIGH)
pygame.mouse.set_visible(False)
DISPLAYSURF.blit(splashScr, (0, 0))
pygame.display.update()
time.sleep(3)
clock = pygame.time.Clock()
while True:
        os.system('clear')
        DISPLAYSURF.fill(iniPi.WHITE)
        time2Display = datetime.datetime.now().strftime("%H:%M")
        menuTxtO= fontSel.render("...", True, iniPi.font_color)      
        infoTxt2 = fontSel.render(time2Display + " | "+ timePi.dayOfWeek, True, iniPi.BLACK)    #timePi.timePi + " | "+ timePi.dayOfWeek, True, iniPi.BLACK)  
        infoTxt3 = fontSel.render(timePi.nbDay + " "+ timePi.nbMonth + " " + timePi.nowYear, True, iniPi.BLACK)
        infoTxt4 = fontSel.render("Time last reboot : " + timePi.timePi , True, iniPi.BLACK)
        infoTxt4 = fontSel.render(timePi.nbMonth + " " + timePi.nowYear, True, iniPi.BLACK)
        #DISPLAYSURF.blit(splashScr, (0, 0))
	#pygame.display.update()
        #time.sleep(30)
        
        #pygame.display.update()
	#default display
        #menuTxtRect= fontSel.render(menuRect, True, iniPi.font_color)
            
        # button 1 fct only (shutdown)
        
        #screen
        DISPLAYSURF.blit(icO, (icOPosX, icOPosY))
        DISPLAYSURF.blit(icRect, (icRectPosX, icRectPosY))
        DISPLAYSURF.blit(icTri, (icTriPosX, icTriPosY))
        DISPLAYSURF.blit(icX, (icXPosX, icXPosY))
        DISPLAYSURF.blit(icDown, (icDownPosX, icDownPosY))
        DISPLAYSURF.blit(icUp, (icUpPosX, icUpPosY))
        #DISPLAYSURF.blit(rayFace, (34, 0))
        DISPLAYSURF.blit(menuTxtO, (iniPi.marge, 220))
        DISPLAYSURF.blit(infoTxt2, (55, 80))        
        DISPLAYSURF.blit(infoTxt3, (55, 120))
        DISPLAYSURF.blit(infoTxt4, (55, 160))

        pygame.display.update()
        clock.tick(60)  # Limit the frame rate to 60 FPS.

        #pygame.display.flip()

        if (not GPIO.input(5)):
                # X
                #clkX+=1
                pygame.quit()
                # pygame.display.update()
        if (not GPIO.input(22)):
                # rect
                #clkRect+=1
                exit()
                #pygame.display.update()
        if (not GPIO.input(23)):
                # pygame
                O.quit()
                sys.exit()
        if (not GPIO.input(24)):
                # triangle
                # clkTri+=1
                #subprocess.Call("/home/pi/alarmPi/fetchHb.sh", shell=True)
                #subprocess.Popen(["/bin/bash", "/home/pi/alarmPi/fetchHb.sh", "var=11; ignore all", "/home/pi/alarmPi/"])
                #repo.fetch ('master')
                g = git.Git('alarmPi')
                g.pull('origin','master')
                # WORK

                #->next to restart python soft to update change
                os.execl('/home/pi/alarmPi/runme.sh', '')
                #pygame.display.update()
        if (not GPIO.input(4)):
                #VOL LOW
                #clkDown+=1
                pygame.mixer.music.load('/home/pi/alarmPi/sound/cartoon002.wav')
                pygame.mixer.music.play(0)
                #GPIO.output(27,GPIO.HIGH)
        if (not GPIO.input(17)):
                #VOL HIGH
                #clkUp
                pygame.mixer.music.load('/home/pi/alarmPi/sound/wake-up.mp3')
                pygame.mixer.music.play(0)
                #GPIO.output(27,GPIO.LOW)
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

        time.sleep(0.1)
