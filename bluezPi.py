import os
import bluetooth
from time import gmtime, strftime
#import time

bluezDeviceFnd =[]

def search(): 
	starttime=strftime("%S", gmtime())
	loopSc = True
	while loopSc == True:
		print("Searching ...")
		print(starttime)
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
		if ((time.time() - starttime)%60.0) > 10:
			break
				#print(bluezDeviceFnd.index(device_name))
			#if bluezDeviceFnd.index(device_name)
			#print(device_name)
        #if(device_name.lower() == "chrisg"):
            #os.system("mplayer /home/pi/imperial.mp3")