import pygame

def playMusic():
	file = '/home/pi/alarmPi/sound/wake-up.mp3'
	pygame.init()
	pygame.mixer.init()
	pygame.mixer.music.load(file)
	pygame.mixer.music.play()
	pygame.event.wait()
def stopMusic():
	pygame.mixer.music.stop()