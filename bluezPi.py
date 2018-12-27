import os
import bluetooth
import datetime
import iniPi
from iniPi import * 
from time import gmtime, strftime
#import time
#timerStart = 0
flgTimer = 0
bluezDeviceFnd =[]

def search(timeStart): 
	#timer TODO
	#starttime=int(strftime("%S", gmtime()))
	#if flgTimer == 0:
	starttime = timeStart
	
	#	flgTimer = 1
	
	loopSc = True
	while loopSc == True:
		print("Searching ...")
		runTime=int(strftime("%S", gmtime()))
		print(starttime)
		print("run:")
		print(runTime)
		print(timerSc)
		devices = bluetooth.discover_devices(duration=10, lookup_names=1, flush_cache=1)
		for device_address, device_name in devices:
			#print("Found: {}".format(device_name))
			try:
			#if device_name in bluezDeviceFnd:
				print(bluezDeviceFnd.index(device_name))
			except ValueError:
			#else:				
				bluezDeviceFnd.append(device_name)
				bluezDeviceFnd.append(device_address)
				#print(device_address)

		if starttime > 49:
			starttime = starttime-50
			if (starttime - runTime) > timerSc:
				loopSc = False
				if not bluezDeviceFnd:
					bluezDeviceFnd.append("Nothing")
				print(bluezDeviceFnd)
				return(bluezDeviceFnd)
				break				
		else:
			if (runTime - starttime) > timerSc:
				loopSc = False
				if not bluezDeviceFnd:
					bluezDeviceFnd.append("Nothing")
				print(bluezDeviceFnd)
				return(bluezDeviceFnd)
				break
				#print(bluezDeviceFnd.index(device_name))
			#if bluezDeviceFnd.index(device_name)
			#print(device_name)
        #if(device_name.lower() == "chrisg"):
            #os.system("mplayer /home/pi/imperial.mp3")