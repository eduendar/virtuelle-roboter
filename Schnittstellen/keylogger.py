import thread
import time
import socket

from msvcrt import getch  # try to import Windows version

UDP_IP = "141.82.50.192"
UDP_PORT = 30000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
	
char = None

def keypress():
    global char
    char = getch()
 
thread.start_new_thread(keypress, ())
 
while True:
	char = getch()
	if char is not None:
		sock.sendto(char, (UDP_IP, UDP_PORT)) #Befehl senden


