import pygame
import iniPi

from iniPi import * 

def dayDis():
	
	icO=pygame.image.load(ic32PathS+ "power-standby" +ic32PathE)
	icX=pygame.image.load(ic32PathS+ "check" +ic32PathE)
	icRect=pygame.image.load(ic32PathS+ "moon" +ic32PathE)
	icTri=pygame.image.load(ic32PathS+ "loop-circular" +ic32PathE)
	icUp=pygame.image.load(ic32PathS+ "caret-top" +ic32PathE)
	icDown=pygame.image.load(ic32PathS+ "caret-bottom" +ic32PathE)

	return icO, icX, icRect, icTri, icUp, icDown

def blueScr(DISPLAYSURF,scrW,scrH):
	pygame.draw.rect(DISPLAYSURF, BLUE, (0,0,(scrW/8),(scrH/4)), 6)