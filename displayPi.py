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
	fontSel=pygame.font.SysFont(iniPi.font, iniPi.font_sizeA)
	#left col 4 rows
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
	#nbr display left 1 to 4
	disInfoTxt = fontSel.render("1", True, BLACK)
	DISPLAYSURF.blit(disInfoTxt, ((scrW/8)/2 - disInfoTxt.get_width()/2,  (scrH/4)/2 - disInfoTxt.get_height()/2))
	disInfoTxt = fontSel.render("2", True, iniPi.BLACK)        
	disInfoTxt = pygame.transform.rotate(disInfoTxt,90)
	DISPLAYSURF.blit(disInfoTxt, ((scrW/8)/2 - disInfoTxt.get_width()/2,  (scrH/4)+ (scrH/4)/2 - disInfoTxt.get_height()/2))
	disInfoTxt = fontSel.render("3", True, iniPi.BLACK)
	DISPLAYSURF.blit(disInfoTxt, ((scrW/8)/2 - disInfoTxt.get_width()/2,  (scrH/8)+ (scrH/2) - disInfoTxt.get_height()/2))
	disInfoTxt = fontSel.render("4", True, iniPi.BLACK)
	DISPLAYSURF.blit(disInfoTxt, ((scrW/8)/2 - disInfoTxt.get_width()/2,  scrH -scrH/8 - disInfoTxt.get_height()/2))
	#nbr display center 5 to 8
	disInfoTxt = fontSel.render("5", True, iniPi.BLACK)
	DISPLAYSURF.blit(disInfoTxt, ((scrW/2 - scrW/8)/2 + scrW/8 - disInfoTxt.get_width()/2,  scrH/4 - disInfoTxt.get_height()/2))
	disInfoTxt = fontSel.render("6", True, iniPi.BLACK)
	DISPLAYSURF.blit(disInfoTxt, ((scrW/2 - scrW/8)/2 + scrW/8 - disInfoTxt.get_width()/2,  scrH/2 + scrH/4 - disInfoTxt.get_height()/2))
	disInfoTxt = fontSel.render("7", True, iniPi.BLACK)
	DISPLAYSURF.blit(disInfoTxt, ((scrW/2 - scrW/8)/2 + scrW/2 - disInfoTxt.get_width()/2,  scrH/4 - disInfoTxt.get_height()/2))
	disInfoTxt = fontSel.render("8", True, iniPi.BLACK)
	DISPLAYSURF.blit(disInfoTxt, ((scrW/2 - scrW/8)/2 + scrW/2 - disInfoTxt.get_width()/2,  scrH/2 + scrH/4 - disInfoTxt.get_height()/2))
	#nbr display right 9 to 11
	disInfoTxt = fontSel.render("9", True, iniPi.BLACK)
	DISPLAYSURF.blit(disInfoTxt, (scrW - (scrW/8)/2 - disInfoTxt.get_width()/2,  (scrH/4)/2 - disInfoTxt.get_height()/2))        
	disInfoTxt = fontSel.render("10", True, iniPi.BLACK)
	DISPLAYSURF.blit(disInfoTxt, (scrW - (scrW/8)/2 - disInfoTxt.get_width()/2,  (scrH)/2 - disInfoTxt.get_height()/2))        
	disInfoTxt = fontSel.render("11", True, iniPi.BLACK)
	DISPLAYSURF.blit(disInfoTxt, (scrW - (scrW/8)/2 - disInfoTxt.get_width()/2, scrH - (scrH)/8 - disInfoTxt.get_height()/2))

