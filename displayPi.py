import pygame
import iniPi
import datetime
import actionPi
import sqlPi
import random

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
	#display grid                
	DISPLAYSURF.fill(WHITE)
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

def welcScr(DISPLAYSURF,scrW,scrH):
	menuTxt = sqlPi.reqMainMenu("menu","Main")  
	fontSelL=pygame.font.SysFont(iniPi.font, iniPi.font_sizeB)
	fontSel=pygame.font.SysFont(iniPi.font, iniPi.font_sizeA)
	time2Display = datetime.datetime.now().strftime("%H:%M")
	hour2Display = int(datetime.datetime.now().strftime("%H"))        
	min2Display = int(datetime.datetime.now().strftime("%M"))        
	sec2Display = int(datetime.datetime.now().strftime("%S")) 
	date2Display = datetime.datetime.now().strftime("%d.%m.%y")
	disDay = datetime.datetime.today().strftime('%A')[:3]
	alarm2Display = actionPi.actFormatTime(alHour,alMin) 
	if alHour == hour2Display and alMin == min2Display and iniPi.alarmOn == 0:
		iniPi.alarmOn = 1
		soundPi.playMusic()
	if iniPi.alarmOn == 1 and iniPi.alarmOff == 1:
		soundPi.stopMusic()
	if dayNight == 0:  
		DISPLAYSURF.fill(WHITE)              
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
	#print("->" + menu2DisT)

	if typeAct == 0 and (reverse == 1 or dayNight == 1):
		DISPLAYSURF.blit(icBell, ((scrW/2)+marge, icRectPosY*2))
	elif typeAct == 1 and menu2DisT == "Scan...":
		displayFindBlu = fontSelL.render(lstDeviceBlu[0], True, iniPi.BLACK)
		DISPLAYSURF.blit(displayFindBlu, ((scrW/2)+(marge*6), 120))


def scrSave(DISPLAYSURF,scrW,scrH):
	#screen saver snowflake time + date + day display
	
	fontSelL=pygame.font.SysFont(iniPi.font, int(scrW/4))#iniPi.font_sizeB)
	fontSel=pygame.font.SysFont(iniPi.font, int(scrW/6))
	DISPLAYSURF.fill(BLACK)
	time2Display = datetime.datetime.now().strftime("%H:%M")
	date2Display = datetime.datetime.now().strftime("%d.%m.%y")
	disDay = datetime.datetime.today().strftime('%A')[:3]
	displayTime = fontSelL.render(time2Display, True, RED)
	displayDate = fontSel.render(date2Display, True, RED)
	displayDay = fontSel.render(disDay, True, RED)
	lenDisTime = displayTime.get_width()	

	#create only once
	if iniPi.snFlake == 0:		
		iniPi.snFlake = 1
		for i in range(100):
			x = random.randrange(0, scrW)
			y = random.randrange(0, scrH)
			snow_list.append([x, y])
	# Process each snow flake in the list
	for i in range(len(snow_list)):
 
		# Draw the snow flake
		pygame.draw.circle(DISPLAYSURF, WHITE, snow_list[i], 4)		

		# Move the snow flake down one pixel
		snow_list[i][1] += 1

		# If the snow flake has moved off the bottom of the screen
		#lenDisTime = scrW - lenDisTime
		if snow_list[i][1] > scrH or (snow_list[i][1] > 51 and snow_list[i][0] > (scrW - lenDisTime - marge)):        
			# Reset it just above the top
			y = random.randrange(-50, -10)
			snow_list[i][1] = y
			# Give it a new x position
			x = random.randrange(0, scrW)
			snow_list[i][0] = x           
 
	# Go ahead and update the screen with what we've drawn.
	DISPLAYSURF.blit(displayTime, (scrW - lenDisTime - marge, 52)) 
	DISPLAYSURF.blit(displayDate, (scrW - lenDisTime - marge, 182)) 
	DISPLAYSURF.blit(displayDay, (scrW - lenDisTime - marge, 282)) 
	pygame.display.flip()

def scrSaveT01(DISPLAYSURF,scrW,scrH):
	#screen saver snowflake time + date + day display
	
	fontSelL=pygame.font.SysFont(iniPi.font, int(scrW/4))#iniPi.font_sizeB)
	fontSel=pygame.font.SysFont(iniPi.font, int(scrW/6))
	DISPLAYSURF.fill(BLACK)
	time2Display = datetime.datetime.now().strftime("%H:%M")
	date2Display = datetime.datetime.now().strftime("%d.%m.%y")
	disDay = datetime.datetime.today().strftime('%A')[:3]
	displayTime = fontSelL.render(time2Display, True, RED)
	displayDate = fontSel.render(date2Display, True, RED)
	displayDay = fontSel.render(disDay, True, YELLOW)
	lenDisTime = displayTime.get_width()	
	posXRect = scrW - lenDisTime - marge
	#create only once
	if iniPi.snFlake == 0:		
		iniPi.snFlake = 1		
		print("YesOne")
		for i in range(100):
			x = random.randrange(0, scrW)
			y = random.randrange(0, scrH)
			snow_list.append([x, y])
	# Process each snow flake in the list
	for i in range(len(snow_list)):
 
		# Draw the snow flake
		pygame.draw.circle(DISPLAYSURF, WHITE, snow_list[i], 4)				

		# Move the snow flake down one pixel
		snow_list[i][1] += 1

		# If the snow flake has moved off the bottom of the screen
		if snow_list[i][1] > scrH :#or (snow_list[i][1] > 51) and snow_list[i][0] > (scrW - lenDisTime - marge)):        
			# Reset it just above the top
			y = random.randrange(-50, -10)
			snow_list[i][1] = y
			# Give it a new x position
			x = random.randrange(0, scrW)
			snow_list[i][0] = x

		# if the snow fall on time
		if (49 < snow_list[i][1] > 51) and snow_list[i][0] > (scrW - lenDisTime - marge):
			#draw the snow
			#first snow
			if iniPi.snowOnTime == 0:
				iniPi.snowOnTime = 1
				
				#posXRect = scrW - lenDisTime - marge#random.randrange(scrW - lenDisTime - marge, scrW)
				
			#if posXRect > (scrW - lenDisTime - marge):
				#posXRect = posXRect - 1
			try:
				iniPi.widthRect += random.randrange(0,2)
			except:
				iniPi.widthRect = random.randrange(0,2)

			try:
				iniPi.heigthRect = heigthRect - random.randrange(0,2)
			except:
				iniPi.heigthRect = random.randrange(0,-2)
			# add snow flak and check if place alone
			snow_pack.append([snow_list[i][0],snow_list[i][1]])
			#snow_list.append([x, y])
			# Reset it just above the top
			y = random.randrange(-50, -10)
			snow_list[i][1] = y
			# Give it a new x position
			x = random.randrange(0, scrW)
			snow_list[i][0] = x

		#pygame.draw.rect(DISPLAYSURF, WHITE, (posXRect,51, iniPi.widthRect, iniPi.heigthRect))
	for i in range(len(snow_pack)):
		if len(snow_pack) < 500:
			if snow_pack[i][1] > 52:
				#pygame.draw.circle(DISPLAYSURF, GREYDARK, snow_pack[i], 1)	
				print("Yes")
			else:
				pygame.draw.circle(DISPLAYSURF, WHITE, snow_pack[i], 2)	
				print("No")
		elif len(snow_pack) < 1000:
			if snow_pack[i][1] > 52:
				#pygame.draw.circle(DISPLAYSURF, GREYDARK, snow_pack[i], 1)	
				print("Yes")
			else:
				pygame.draw.circle(DISPLAYSURF, WHITE, snow_pack[i], 4)	
		else:
			if snow_pack[i][1] > 52:
				#pygame.draw.circle(DISPLAYSURF, GREYDARK, snow_pack[i], 1)	
				print("Yes")
			else:
				pygame.draw.circle(DISPLAYSURF, WHITE, snow_pack[i], 8)	
				print("No")


	# Go ahead and update the screen with what we've drawn.	
	DISPLAYSURF.blit(displayTime, (scrW - lenDisTime - marge, 52)) 
	DISPLAYSURF.blit(displayDate, (scrW - lenDisTime - marge, 182)) 
	DISPLAYSURF.blit(displayDay, (scrW - lenDisTime - marge, 282)) 
	pygame.display.flip()

def scrSaveT02(DISPLAYSURF,scrW,scrH):
	#screen saver snowflake time + date + day display
	
	fontSelL=pygame.font.SysFont(iniPi.font, int(scrW/4))#iniPi.font_sizeB)
	fontSel=pygame.font.SysFont(iniPi.font, int(scrW/6))
	DISPLAYSURF.fill(BLACK)
	time2Display = datetime.datetime.now().strftime("%H:%M")
	date2Display = datetime.datetime.now().strftime("%d.%m.%y")
	disDay = datetime.datetime.today().strftime('%A')[:3]
	displayTime = fontSelL.render(time2Display, True, RED)
	displayDate = fontSel.render(date2Display, True, RED)
	displayDay = fontSel.render(disDay, True, YELLOW)
	lenDisTime = displayTime.get_width()	
	posXRect = scrW - lenDisTime - marge	
	#create only once
	if iniPi.snFlake == 0:		
		iniPi.snFlake = 1		
		print("YesOne")
		for i in range(10):
			x = random.randrange(0, scrW)
			y = random.randrange(0, scrH)
			snow_list.append([x, y])
	# Process each snow flake in the list
	for i in range(len(snow_list)):
 
		# Draw the snow flake		
						
		#snow_list[i][1] += 2
		pygame.draw.circle(DISPLAYSURF, YELLOW, snow_list[i], 4)				
		posSnY = snow_list[i][1]
		posSnY -= 2
		posSnX = snow_list[i][0]
		pygame.draw.circle(DISPLAYSURF, RED, (posSnX, posSnY), 3)
		posSnY = snow_list[i][1]
		posSnY -= 4
		posSnX = snow_list[i][0]
		if iniPi.blinkComet == 0:
			iniPi.blinkComet = 1
			pygame.draw.circle(DISPLAYSURF, WHITE, (posSnX, posSnY), 2)
		else:
			iniPi.blinkComet = 0
			pygame.draw.circle(DISPLAYSURF, GREY, (posSnX, posSnY), 2)

		# Move the snow flake down one pixel
		snow_list[i][1] += 4

		# If the snow flake has moved off the bottom of the screen
		if snow_list[i][1] > scrH :#or (snow_list[i][1] > 51) and snow_list[i][0] > (scrW - lenDisTime - marge)):        
			# Reset it just above the top
			y = random.randrange(-50, -10)
			snow_list[i][1] = y
			# Give it a new x position
			x = random.randrange(0, scrW)
			snow_list[i][0] = x

		# if the snow fall on time
		if (49 < snow_list[i][1] > 51) and snow_list[i][0] > (scrW - lenDisTime - marge):
			#draw the snow
			#first snow
			if iniPi.snowOnTime == 0:
				iniPi.snowOnTime = 1
				
				#posXRect = scrW - lenDisTime - marge#random.randrange(scrW - lenDisTime - marge, scrW)
				
			#if posXRect > (scrW - lenDisTime - marge):
				#posXRect = posXRect - 1
			try:
				iniPi.widthRect += random.randrange(0,2)
			except:
				iniPi.widthRect = random.randrange(0,2)

			try:
				iniPi.heigthRect = heigthRect - random.randrange(0,2)
			except:
				iniPi.heigthRect = random.randrange(0,-2)
			# add snow flak and check if place alone
			snow_pack.append([snow_list[i][0],snow_list[i][1]])
			#snow_list.append([x, y])
			# Reset it just above the top
			y = random.randrange(-50, -10)
			snow_list[i][1] = y
			# Give it a new x position
			x = random.randrange(0, scrW)
			snow_list[i][0] = x

		#pygame.draw.rect(DISPLAYSURF, WHITE, (posXRect,51, iniPi.widthRect, iniPi.heigthRect))
	for i in range(len(snow_pack)):
		if len(snow_pack) < 500:
			if snow_pack[i][1] > 52:
				#pygame.draw.circle(DISPLAYSURF, GREYDARK, snow_pack[i], 1)	
				print("Yes")
			else:
				pygame.draw.circle(DISPLAYSURF, WHITE, snow_pack[i], 2)	
				print("No")
		elif len(snow_pack) < 1000:
			if snow_pack[i][1] > 52:
				#pygame.draw.circle(DISPLAYSURF, GREYDARK, snow_pack[i], 1)	
				print("Yes")
			else:
				pygame.draw.circle(DISPLAYSURF, WHITE, snow_pack[i], 4)	
		else:
			if snow_pack[i][1] > 52:
				#pygame.draw.circle(DISPLAYSURF, GREYDARK, snow_pack[i], 1)	
				print("Yes")
			else:
				pygame.draw.circle(DISPLAYSURF, WHITE, snow_pack[i], 8)	
				print("No")


	# Go ahead and update the screen with what we've drawn.	
	DISPLAYSURF.blit(displayTime, (scrW - lenDisTime - marge, 52)) 
	DISPLAYSURF.blit(displayDate, (scrW - lenDisTime - marge, 182)) 
	DISPLAYSURF.blit(displayDay, (scrW - lenDisTime - marge, 282)) 
	pygame.display.flip()