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
pygame.display.init()
scrW = pygame.display.Info().current_w
scrH = pygame.display.Info().current_h

from pygame.locals import *
from iniPi import * 
from git import Repo

repo = Repo("/home/pi/alarmPi")
assert not repo.bare

os.putenv('SDL_FBDEV', '/dev/fb1')

#init menu
timerMenu=30
posMenu =20
spaceMenu = 60
#Dev Test Stage Prod GitPull Exit
infoTxt = ["Prod", "Stage","Test", "Dev", "Git pull", "Exit"]
posCur = 20

pygame.init()

# 2 put in iniPi
icO=pygame.image.load(ic32PathS+ "power-standby" +ic32PathE)
icX=pygame.image.load(ic32PathS+ "check" +ic32PathE)
icRect=pygame.image.load(ic32PathS+ "sun" +ic32PathE)
icTri=pygame.image.load(ic32PathS+ "loop-circular" +ic32PathE)
icUp=pygame.image.load(ic32PathS+ "caret-top" +ic32PathE)
icDown=pygame.image.load(ic32PathS+ "caret-bottom" +ic32PathE)

DISPLAYSURF = pygame.display.set_mode((scrW, scrH))

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)


fontSelL=pygame.font.SysFont(iniPi.font, iniPi.font_sizeB)

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
        for nbrMenu2Dis in range (0, 6):
                disInfoTxt = fontSelL.render(infoTxt[nbrMenu2Dis], True, iniPi.BLACK)
                nb2dis= posMenu +spaceMenu * nbrMenu2Dis                
                DISPLAYSURF.blit(disInfoTxt, (64,  nb2dis))         
        
        #screen        
        pygame.draw.rect(DISPLAYSURF, iniPi.RED, (64,posCur,(scrW/2)-marge,60), 6)
        DISPLAYSURF.blit(icO, (icOPosX*4, icOPosY*2))
        DISPLAYSURF.blit(icX, (icXPosX*4, icXPosY*2))
        DISPLAYSURF.blit(icRect, (icRectPosX*4, icRectPosY*2))
        DISPLAYSURF.blit(icTri, (icTriPosX*4, icTriPosY*2))
        DISPLAYSURF.blit(icDown, ((icDownPosX*2)-marge, icDownPosY*2))
        DISPLAYSURF.blit(icUp, ((icUpPosX*2)-marge, icUpPosY*2))
                
        pygame.display.update()
        clock.tick(60)  # Limit the frame rate to 60 FPS.

        if (not GPIO.input(5)):
                # X
                #clkX+=1
                if posCur == 20:
                        os.execl('/home/pi/alarmPi/runProd.sh', '')
                if posCur == 80:
                        os.execl('/home/pi/alarmPi/runStage.sh', '')
                if posCur == 140:
                        #os.execl('/home/pi/alarmPi/runTest.sh', '')
                        file = open('/home/pi/testfile.txt', 'r') 
                        for line in file: 
                                print (line)
                if posCur == 200:
			#os.execl('/home/pi/alarmPi/runTest.sh', '')
                #if posCur == 110:
                        os.execl('/home/pi/alarmPi/runDev.sh', '')
                if posCur == 260:
                        g = git.Git('/home/pi/alarmPi')
                        g.pull('origin','master')
                
                        # restart python soft to update change
                        os.execl('/home/pi/alarmPi/runGui.sh', '')
                if posCur == 320:
                        pygame.quit()
		#if posCur == 170:
			#pygame.quit()    
                        exit()   
        if (not GPIO.input(22)):
                # rect
                #clkRect+=1
                exit()             
        if (not GPIO.input(24)):
                # triangle
                exit()  
        if (not GPIO.input(23)):
                # pygame
                # O
                O.quit()
                sys.exit()            
        if (not GPIO.input(4)):
                #VOL LOW
                #clkDown+=1
                if posCur < 320: #(50 + 30*(len(infoTxt))):
                        posCur+=60
                
        if (not GPIO.input(17)):
                #VOL HIGH
                #clkUp
                if posCur > 20:
                        posCur-=60                
                
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()    
        #print(posCur)
        #timerMenu = timerMenu - 0.1
        #if (timerMenu < 0):
        #        pygame.quit()
        time.sleep(0.1)