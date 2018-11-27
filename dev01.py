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
import ipPi

from pygame.locals import *
from iniPi import * 
from git import Repo

repo = Repo("/home/pi/alarmPi")
assert not repo.bare

os.putenv('SDL_FBDEV', '/dev/fb1')

pygame.init()
# 2 put in iniPi
icO=pygame.image.load(ic16PathS+ "power-standby" +ic16PathE)
icRect=pygame.image.load(ic16PathS+ "eject" +ic16PathE)
icTri=pygame.image.load(ic16PathS+ "account-logout" +ic16PathE)
icX=pygame.image.load(ic16PathS+ "cog" +ic16PathE)
icUp=pygame.image.load(ic16PathS+ "caret-top" +ic16PathE)
icDown=pygame.image.load(ic16PathS+ "caret-bottom" +ic16PathE)
moon =pygame.image.load("/home/pi/alarmPi/ic64/moon.jpg")
sun =pygame.image.load("/home/pi/alarmPi/ic64/sun.png")
splashScr =pygame.image.load("/home/pi/pjtSmScr/wp/coplandOS.jpg")
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
fontSelL=pygame.font.SysFont(iniPi.font, iniPi.font_sizeL)

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
        hour2Display = int(datetime.datetime.now().strftime("%H"))        
        date2Display = datetime.datetime.now().strftime("%d")
        menuTxtO= fontSel.render("...", True, iniPi.BLACK)      
        infoTxt2 = fontSelL.render(time2Display , True, iniPi.RED)    
        infoTxt3 = fontSel.render(timePi.dayOfWeek + " | "+ date2Display + " "+ timePi.nbMonth + " " + timePi.nowYear, True, iniPi.BLACK)
        infoTxt4 = fontSelHalf.render("Last reboot : " + timePi.timePi , True, iniPi.BLACK)
        infoTxt5 = fontSelHalf.render(timePi.nbDay + " "+ timePi.nbMonth + " " + timePi.nowYear , True, iniPi.BLACK)                   
        heightInfoTxt = infoTxt5.get_rect().height
        widthInfoTxt = infoTxt5.get_rect().width
        wlan2find = ipPi.getIp(b"wlan0")
        lan2find = ipPi.getIp(b"eth0")
        chkNet = ipPi.checkNet()
        infoTxt6 = fontSelHalf.render("wlan : " + wlan2find, True, iniPi.BLACK)                   
        infoTxt7 = fontSelHalf.render("lan : " + lan2find, True, iniPi.BLACK)                   
        infoTxt8 = fontSelHalf.render(chkNet, True, iniPi.BLACK)                   
        
        #screen
        DISPLAYSURF.blit(icO, (icOPosX, icOPosY))
        DISPLAYSURF.blit(icRect, (icRectPosX, icRectPosY))
        DISPLAYSURF.blit(icTri, (icTriPosX, icTriPosY))
        DISPLAYSURF.blit(icX, (icXPosX, icXPosY))
        DISPLAYSURF.blit(icDown, (icDownPosX, icDownPosY))
        DISPLAYSURF.blit(icUp, (icUpPosX, icUpPosY))        
        DISPLAYSURF.blit(menuTxtO, (iniPi.marge, 220))
        DISPLAYSURF.blit(infoTxt2, (widthInfoTxt/2, 20))        
        DISPLAYSURF.blit(infoTxt3, (32, 80))
        DISPLAYSURF.blit(infoTxt4, (32, 140))
        DISPLAYSURF.blit(infoTxt5, (32, 160))
        DISPLAYSURF.blit(infoTxt6, (32, 180))
        DISPLAYSURF.blit(infoTxt7, (32, 200))
        DISPLAYSURF.blit(infoTxt8, (32, 220))
        if (hour2Display<8 or hour2Display>20):
                DISPLAYSURF.blit(moon, (224, 160))
        else:
                DISPLAYSURF.blit(sun, (224, 160))

        pygame.display.update()
        clock.tick(60)  # Limit the frame rate to 60 FPS.

        if (not GPIO.input(5)):
                # X
                #clkX+=1
                pygame.quit()               
        if (not GPIO.input(22)):
                # rect
                #clkRect+=1
                exit()                
        if (not GPIO.input(23)):
                # pygame
                # O
                O.quit()
                sys.exit()
        if (not GPIO.input(24)):
                # triangle
                # clkTri+=1
                g = git.Git('/home/pi/alarmPi')
                g.pull('origin','master')
                
                # restart python soft to update change
                os.execl('/home/pi/alarmPi/runme.sh', '')                
        if (not GPIO.input(4)):
                #VOL LOW
                #clkDown+=1
                pygame.mixer.music.load('/home/pi/alarmPi/sound/cartoon002.wav')
                pygame.mixer.music.play(0)                
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