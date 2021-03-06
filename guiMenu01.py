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
#GPIO.output(27,GPIO.HIGH)
pygame.mouse.set_visible(False)

clock = pygame.time.Clock()
menuTxt = sqlPi.reqMainMenu("menu","Main")  
sec2Start = int(datetime.datetime.now().strftime("%S"))
while True:
        os.system('clear')        
        time2Display = datetime.datetime.now().strftime("%H:%M")
        hour2Display = int(datetime.datetime.now().strftime("%H"))        
        min2Display = int(datetime.datetime.now().strftime("%M"))        
        sec2Display = int(datetime.datetime.now().strftime("%S")) 
        date2Display = datetime.datetime.now().strftime("%d.%m.%y")
        disDay = datetime.datetime.today().strftime('%A')[:3]
        alarm2Display = actionPi.actFormatTime(alHour,alMin) 
        if alHour == hour2Display and alMin == min2Display and alarmOn == 0:
                alarmOn = 1
                soundPi.playMusic()
        if alarmOn == 1 and alarmOff == 1:
                soundPi.stopMusic()
        if dayNight == 0:  
                DISPLAYSURF.fill(iniPi.WHITE)              
                #displayPi.dayDis()
                icO=pygame.image.load(ic32PathS+ "power-standby" +ic32PathE)
                icX=pygame.image.load(ic32PathS+ "check" +ic32PathE)
                icRect=pygame.image.load(ic32PathS+ "moon" +ic32PathE)
                icTri=pygame.image.load(ic32PathS+ "loop-circular" +ic32PathE)
                icUp=pygame.image.load(ic32PathS+ "caret-top" +ic32PathE)
                icDown=pygame.image.load(ic32PathS+ "caret-bottom" +ic32PathE)
                stateBell = actionPi.alarmOn(flAlarm)
                icBell=pygame.image.load(ic32PathS+ stateBell +ic32PathE)                                        
                displayTime = fontSelL.render(time2Display, True, iniPi.BLACK)
                displayAlar = fontSelL.render(alarm2Display, True, iniPi.BLACK)
                displayDay = fontSelL.render(disDay, True, iniPi.BLACK)
                displayDate = fontSelL.render(date2Display, True, iniPi.BLACK)
        else:
                DISPLAYSURF.fill(iniPi.BLACK)
                icO=pygame.image.load(ic32PathR+ "power-standby" +ic32PathE)
                stateBell = actionPi.alarmOn(flAlarm)
                icX=pygame.image.load(ic32PathR+ stateBell +ic32PathE)
                icRect=pygame.image.load(ic32PathR+ "sun" +ic32PathE)
                icTri=pygame.image.load(ic32PathR+ "loop-circular" +ic32PathE)
                icUp=pygame.image.load(ic32PathR+ "caret-top" +ic32PathE)
                icDown=pygame.image.load(ic32PathR+ "caret-bottom" +ic32PathE)
                stateBell = actionPi.alarmOn(flAlarm)
                icBell=pygame.image.load(ic32PathR+ stateBell +ic32PathE)                
                displayTime = fontSelL.render(time2Display, True, iniPi.WHITE)
                displayAlar = fontSelL.render(alarm2Display, True, iniPi.WHITE)
                displayDate = fontSelL.render(date2Display, True, iniPi.GREY)
        if dayNight == 0 and reverse == 0 and typeAct == 0:
                if posCur == (scrH/8)*2:pygame.draw.rect(DISPLAYSURF, iniPi.RED, (scrW/2,posCur,(scrW/2)-64,60), 6)
                        
                else:
                        pygame.draw.rect(DISPLAYSURF, iniPi.RED, (64,posCur,(scrW/2)-64,60), 6)
        
        #screen        
        if reverse == 0:
                nbrMenu2Dis=0
                for row in menuTxt:
                        row = (', '.join(row))
                        if typeAct == 1 and str2search == "Day" and len(str(row)) < 4:
                                disInfoTxt = fontSel.render(str(row), True, iniPi.GREY)
                        else:
                                disInfoTxt = fontSel.render(str(row), True, iniPi.BLACK)
                        if typeAct == 1 and str2search == "Scan" and startSc == 0:
                                startSc = 1
                                lstDeviceBlu = bluezPi.search(sec2Display)                                
                                nbrMenu2Dis = nbrMenu2Dis - 1              
                                disInfoTxt = fontSel.render(lstDeviceBlu[0], True, iniPi.BLACK)
                        nb2dis= posMenu +spaceMenu * nbrMenu2Dis  
                        nbrMenu2Dis = nbrMenu2Dis + 1              
                        DISPLAYSURF.blit(disInfoTxt, (64,  nb2dis))                
          
                icOd = pygame.transform.rotate(icO,0)
                icXd = pygame.transform.rotate(icX,0)
                icRectd = pygame.transform.rotate(icRect,0)
                icTrid = pygame.transform.rotate(icTri,0)
                displayTimed = pygame.transform.rotate(displayTime,0)
                displayAlarm = pygame.transform.rotate(displayAlar,0)
                displayDated = pygame.transform.rotate(displayDate,0)
                DISPLAYSURF.blit(icDown, ((icDownPosX*2)-marge, icDownPosY*2))
                DISPLAYSURF.blit(icUp, ((icUpPosX*2)-marge, icUpPosY*2))
                if typeAct == 0:
                        DISPLAYSURF.blit(displayTimed, ((scrW/2)+marge, icOPosY*2))
                        DISPLAYSURF.blit(displayAlarm, ((scrW/2)+(marge*6), 120))
                        DISPLAYSURF.blit(displayDay, ((scrW/2)+marge, 310))
                        DISPLAYSURF.blit(displayDated, ((scrW/2)+marge, 370))
                angleRot = 0
        else:
                if angleRot < 90:
                        angleRot=angleRot+5
                icOd = pygame.transform.rotate(icO,90)   
                icXd = pygame.transform.rotate(icBell,90)   
                icRectd = pygame.transform.rotate(icRect,90)   
                icTrid = pygame.transform.rotate(icTri,90)   
                icBell = pygame.transform.rotate(icBell,90)   
                displayTimed = pygame.transform.rotate(displayTime,angleRot) 
                displayAlarm = pygame.transform.rotate(displayAlar,angleRot)   
                displayDated = pygame.transform.rotate(displayDate,angleRot)   
                DISPLAYSURF.blit(displayTimed, (scrW/4, 80))#icOPosY*2))
                DISPLAYSURF.blit(displayAlarm, ((scrW/2)-marge, 180))
                DISPLAYSURF.blit(displayDated, ((scrW/2)+(marge*8), 100))        

        DISPLAYSURF.blit(icOd, (icOPosX*4, icOPosY*2))
        DISPLAYSURF.blit(icXd, (icXPosX*4, icXPosY*2))
        DISPLAYSURF.blit(icRectd, (icRectPosX*4, icRectPosY*2))
        DISPLAYSURF.blit(icTrid, (icTriPosX*4, icTriPosY*2))
        #
        menu2DisT = (', '.join(menuTxt[0])) 
                                #
        print("->" + menu2DisT)

        if typeAct == 0 and (reverse == 1 or dayNight == 1):
                DISPLAYSURF.blit(icBell, ((scrW/2)+marge, icRectPosY*2))
        elif typeAct == 1 and menu2DisT == "Scan...":
                displayFindBlu = fontSelL.render(lstDeviceBlu[0], True, iniPi.BLACK)
                DISPLAYSURF.blit(displayFindBlu, ((scrW/2)+(marge*6), 120))
        pygame.display.update()
        clock.tick(60)  # Limit the frame rate to 60 FPS.

        if (not GPIO.input(5)):
                # X
                if alarmOn == 1:
                        alarmOff = 1

                if dayNight == 0 and reverse == 0:
                        if posCur == scrH/24:
                                str2search = (', '.join(menuTxt[0]))
                                menuTxt = sqlPi.reqMainMenu("menu",str2search)  
                                #print("->" + menuTxt)
                                #menuTop = sqlPi.reqMainTop("top",str2search)  
                        if posCur == scrH/24 + scrH/8:
                                str2search = (', '.join(menuTxt[1]))
                                menuTxt = sqlPi.reqMainMenu("menu",str2search) 
                                #menuTop = sqlPi.reqMainTop("top",str2search)
                        if posCur == scrH/24 + (scrH/8)*2:
                                str2search = (', '.join(menuTxt[2]))
                                menuTxt = sqlPi.reqMainMenu("menu",str2search) 
                                #menuTop = (', '.join(menuTxt[0]))
                                #menuTop = sqlPi.reqMainTop("top",top2search)
                                #print(menuTop)
                        if posCur == scrH/24 + (scrH/8)*3:
                                str2search = (', '.join(menuTxt[3]))
                                menuTxt = sqlPi.reqMainMenu("menu",str2search) 
                                #menuTop = sqlPi.reqMainTop("top",str2search)                                
                        if posCur == scrH/24 + (scrH/8)*4:
                                #g = git.Git('/home/pi/alarmPi')
                                #g.pull('origin','master')                        
                                # restart python soft to update change
                                #os.execl('/home/pi/alarmPi/runGui.sh', '')
                                str2search = (', '.join(menuTxt[4]))
                                menuTxt = sqlPi.reqMainMenu("menu",str2search)
                                #menuTop = sqlPi.reqMainTop("top",menuTxt)
                        if posCur == scrH/24 + (scrH/8)*5:
                                #pygame.quit()        		
                                #exit()  
                                str2search = (', '.join(menuTxt[5]))
                                menuTxt = sqlPi.reqMainMenu("menu",str2search)
                                #menuTop = sqlPi.reqMainTop("top",menuTxt)
                        if posCur == scrH/24 + (scrH/8)*6:
                                str2search = (', '.join(menuTxt[6]))
                                menuTxt = sqlPi.reqMainMenu("menu",str2search)
                                #menuTop = sqlPi.reqMainTop("top",menuTxt)
                        if posCur == (scrH/8)*2:
                                str2search = "Alarm"
                                #str2search = (', '.join("Alarm"))

                                menuTxt = sqlPi.reqMainMenu("menu",str2search)
                                #swType
                        #menuTop = sqlPi.reqMainTop("top",menuTxt)
                        menuTyp = sqlPi.reqMainMenu("type",str2search) 
                        #print(menuTyp)                         
                        typ2search = (', '.join(menuTyp[0]))  
                        typeAct = actionPi.swType(typ2search)                        
                        #remove red square
                        #side button to +1 hour/min
                else:
                        #alarm check if On
                        if flAlarm == 0:
                                icBell=pygame.image.load(ic32PathS+ "nobell" +ic32PathE)
                                flAlarm = 1
                        else: 
                                icBell=pygame.image.load(ic32PathS+ "bell" +ic32PathE)
                                flAlarm = 0

                #after selection reset cursor 
                posCur = scrH/24
        if (not GPIO.input(22)):
                # rect     
                dayNight = actionPi.flipBool(dayNight)          

        if (not GPIO.input(24)):
                # triangle
                reverse = actionPi.flipBool(reverse)

        if (not GPIO.input(23)):
                # O
                O.quit()
                sys.exit()            
        if (not GPIO.input(4)):
                #VOL LOW
                #displayAlar = displayAlar - 1
                #fct cursor
                if typeAct == 0:
                        if posCur < scrH/8*(len(menuTxt))-40 and posCur!= (scrH/8)*2:
                                posCur+=scrH/8 
                        elif posCur == (scrH/8)*2:
                                posCur = scrH/24
                        else:
                                posCur = (scrH/8)*2
                        if posCur == (scrH/8)*2:
                                posCur = (scrH/8)*2
                else:          
                        menu2Dis = (', '.join(menuTxt[0])) 
                        if menu2Dis == "Hour":
                                alHour = alHour - 1                              

        if (not GPIO.input(17)):
                #VOL HIGH
                #displayAlar = displayAlar + 1
                if posCur > scrH/24 and posCur!= (scrH/8)*2:
                        posCur-=scrH/8  
                elif posCur == (scrH/8)*2:                        
                        posCur = scrH/8*(len(menuTxt))-40
                elif posCur == scrH/24:
                        posCur = (scrH/8)*2

        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()    

        time.sleep(0.1)