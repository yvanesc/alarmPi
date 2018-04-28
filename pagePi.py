import pygame
import iniPi
#import pages/*
from pages import n00000, n10000, n01000, n00100, n00010, n00001
from iniPi import *

# 2 put in iniPi
icO=pygame.image.load(ic16PathS+ "power-standby" +ic16PathE)
icRect=pygame.image.load(ic16PathS+ "camera-slr" +ic16PathE)
icTri=pygame.image.load(ic16PathS+ "transfer" +ic16PathE)
icX=pygame.image.load(ic16PathS+ "cog" +ic16PathE)
icUp=pygame.image.load(ic16PathS+ "lightbulb" +ic16PathE)
icDown=pygame.image.load(ic16PathS+ "menu" +ic16PathE)
rayFace =pygame.image.load("/home/pi/pjtSmScr/icon/raymond.png")
picsPath ="/home/pi/alarmPi/pics/"
simps=pygame.image.load(picsPath+"meSimps.png")
miaou=pygame.image.load(picsPath+"miaou.jpg")
noo=pygame.image.load(picsPath+"nope.png")
sleep=pygame.image.load(picsPath+"sleep.jpg")
wake=pygame.image.load(picsPath+"wake.jpg")
# define page ask
def askP(X, Rect, Tri, Up, Down, Dis):
    if (X==0 and Rect==0 and Tri == 0 and Up == 0 and Down == 0):
        n00000.n00000(Dis)
    elif (X==1 and Rect==0 and Tri == 0 and Up == 0 and Down == 0):
        n10000.n10000(Dis)
    elif (X==0 and Rect==1 and Tri == 0 and Up == 0 and Down == 0):
        n01000.n01000(Dis)
        
    elif (X==0 and Rect==0 and Tri == 1 and Up == 0 and Down == 0):
        n00100.n00100(Dis)
    elif (X==0 and Rect==0 and Tri == 0 and Up == 1 and Down == 0):
        n00010.n00010(Dis)
    elif (X==0 and Rect==0 and Tri == 0 and Up == 0 and Down == 1):
        n00001.n00001(Dis)
    else:
        n00000.n00000(Dis)
# end first level

