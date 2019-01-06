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
	pygame.draw.rect(DISPLAYSURF, GREEN, (0,(scrH/4),(scrW/8),(scrH/4)), 6)
	pygame.draw.rect(DISPLAYSURF, GREY, (0,(scrH/2),(scrW/8),(scrH/4)), 6)
	pygame.draw.rect(DISPLAYSURF, RED, (0,(scrH/4)*3,(scrW/8),(scrH/4)), 6)
	#center
    pygame.draw.rect(DISPLAYSURF, BLACK, ((scrW/8),0,(scrW/2)-(scrW/8),(scrH/2)), 6)
    pygame.draw.rect(DISPLAYSURF, BLUE, ((scrW/8),(scrH/2),(scrW/2)-(scrW/8),(scrH/2)), 6)
    pygame.draw.rect(DISPLAYSURF, RED, ((scrW/2),0,(scrW/2)-(scrW/8),(scrH/2)), 6)
    pygame.draw.rect(DISPLAYSURF, GREEN, ((scrW/2),(scrH/2),(scrW/2)-(scrW/8),(scrH/2)), 6)
    #last col and 3 row
    pygame.draw.rect(DISPLAYSURF, BLUE, (scrW-(scrW/8),0,(scrW/8),(scrH/4)), 6)
    pygame.draw.rect(DISPLAYSURF, GREY, (scrW-(scrW/8),(scrH/4),(scrW/8),(scrH/2)), 6)
	pygame.draw.rect(DISPLAYSURF, RED, (scrW-(scrW/8),(scrH/4)*3,(scrW/8),(scrH/4)), 6)