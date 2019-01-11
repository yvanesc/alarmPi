"""
 Animating multiple objects using a list.
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/Gkhz3FuhGoI
"""
 
# Import a library of functions called 'pygame'
import pygame
import random
import iniPi
import datetime
import time

from iniPi import * 
# Initialize the game engine
pygame.init()
 
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
 
# Set the height and width of the screen
SIZE = [400, 400]
 
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snow Animation")
 
# Create an empty array
snow_list = []
##dark_list = []
#oneshoot creation flake
snFlake = 0
# Loop 50 times and add a snow flake in a random x,y position

fontSelL=pygame.font.SysFont(iniPi.font, iniPi.font_sizeB)
clock = pygame.time.Clock()
 
# Loop until the user clicks the close button.
done = False
while not done:
    time2Display = datetime.datetime.now().strftime("%H:%M")
##    print(time2Display)
    displayTime = fontSelL.render(time2Display, True, RED)
    
    for event in pygame.event.get():   # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True   # Flag that we are done so we exit this loop
    
    if snFlake == 0:
        snFlake = 1
        for i in range(50):
            x = random.randrange(0, 400)
            y = random.randrange(0, 400)
            snow_list.append([x, y])
##    for i in range(10):
##        x = random.randrange(0, 400)
##        y = random.randrange(0, 400)
##        dark_list.append([x, y])
    # Set the screen background
    screen.fill(BLACK)
##    snowList()
    
    # Process each snow flake in the list
    for i in range(len(snow_list)):
 
        # Draw the snow flake
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)
##        pygame.draw.circle(screen, BLACK, dark_list[i], 2)
 
        # Move the snow flake down one pixel
        snow_list[i][1] += 1
##        dark_list[i][1] -= 1
 
        # If the snow flake has moved off the bottom of the screen
##        if snow_list[i][1] > 400:
        if snow_list[i][1] > 400 or (snow_list[i][1] > 50 and snow_list[i][0] > 215):        
            # Reset it just above the top
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            # Give it a new x position
            x = random.randrange(0, 400)
            snow_list[i][0] = x
            
##        if dark_list[i][1] > 1:
##            # Reset it just above the top
##            y = random.randrange(0, 400)
##            dark_list[i][1] = y
##            # Give it a new x position
##            x = random.randrange(0, 400)
##            dark_list[i][0] = x
 
    # Go ahead and update the screen with what we've drawn.
    screen.blit(displayTime, (230, 52))
    pygame.display.flip()
    clock.tick(20)
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
