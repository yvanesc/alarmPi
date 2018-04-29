# get information ip
import socket
import fcntl
import struct
#import urllib2
import urllib.request

def getIp(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
                s.fileno(),
                0x8915,  # SIOCGIFADDR
                struct.pack('256s', ifname[:15])
        )[20:24])
def checkNet():
    try:
        x = urllib.request.urlopen("https://www.google.com/") #, timeout=1)
        #urllib2.urlopen("http://216.58.192.142", timeout=1)
        return x + "Connection OK"
    except : #urllib2.URLError as err:
        return "No connection"
        
