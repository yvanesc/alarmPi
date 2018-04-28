import pygame
import time

splashScr =pygame.image.load("/home/pi/pjtSmScr/wp/coplandOS.jpg")

def disSplash(DISPLAY):
    DISPLAY.blit(splashScr, (0, 0))
    pygame.display.update()
    time.sleep(3)