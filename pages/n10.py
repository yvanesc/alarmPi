import pygame
import iniPi

from iniPi import *
# 2 put in iniPi
icO=pygame.image.load(ic16PathS+ "power-standby" +ic16PathE)
icRect=pygame.image.load(ic16PathS+ "volume-off" +ic16PathE)
icTri=pygame.image.load(ic16PathS+ "menu" +ic16PathE)
icX=pygame.image.load(ic16PathS+ "clock" +ic16PathE)
icUp=pygame.image.load(ic16PathS+ "lightbulb" +ic16PathE)
icDown=pygame.image.load(ic16PathS+ "cog" +ic16PathE)

picsPath ="/home/pi/alarmPi/pics/"
simps=pygame.image.load(picsPath+"meSimps.png")
miaou=pygame.image.load(picsPath+"miaou.jpg")
noo=pygame.image.load(picsPath+"nope.png")
sleep=pygame.image.load(picsPath+"sleep.jpg")
wake=pygame.image.load(picsPath+"wake.jpg")
# page default all button 0
def n1(DISPLAY):
        #DISPLAYSURF.blit(splashScr, (0, 0))
	#pygame.display.update()
        #time.sleep(30)
        DISPLAY.fill(iniPi.GREY)

        #screen
        DISPLAY.blit(icO, (icOPosX, icOPosY))
        DISPLAY.blit(icRect, (icRectPosX, icRectPosY))
        DISPLAY.blit(icTri, (icTriPosX, icTriPosY))
        DISPLAY.blit(icX, (icXPosX, icXPosY))
        DISPLAY.blit(icDown, (icDownPosX, icDownPosY))
        DISPLAY.blit(icUp, (icUpPosX, icUpPosY))
        DISPLAY.blit(sleep, (34, 0))
        
        pygame.display.flip()