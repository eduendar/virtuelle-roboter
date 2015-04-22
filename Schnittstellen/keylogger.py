import thread
import time
import socket

from msvcrt import getch  # try to import Windows version


#ServeIP + Port zur Auswertung der Gesten
UDP_IP = "141.82.50.192"
UDP_PORT = 30000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
	
char = None
 
 
while True:
	#tastatureingabe
	char = getch()
	
	#befehl senden
	sock.sendto(char, (UDP_IP, UDP_PORT)) #Befehl senden


