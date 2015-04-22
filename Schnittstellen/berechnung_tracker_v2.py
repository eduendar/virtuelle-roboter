import socket
import UdpClnt_Python

#UdpClient
udpClnt = UdpClnt_Python.UdpClnt("141.82.50.192", 50000)

#UdpSocket
UDPSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
listen_addr = ("141.82.50.192", 30000)
UDPSock.bind(listen_addr)

#Methode mit mehreren Ausfuerbaren Befehlen fuer den SunSim-Server
def Simulation():
	udpClnt.send("MOVE PTP 90.0 9    0.0 0.0 0.0 1.2 -3.14 1.57 0.0 -1.57 -3.14")
	udpClnt.send("MOVE PTP 90.0 9    0.0 0.0 -0.75 1.2 -3.14 1.57 0.0 -1.57 -3.14")
	udpClnt.send("MOVE PTP 90.0 9    2.0 -2.2 -0.8 1.2 -3.14 1.57 0.0 -1.57 -3.14")
	udpClnt.send("MOVE PTP 90.0 9    2.0 -2.2 2.2 1.2 -3.14 1.57 0.0 -1.57 -3.14")
	udpClnt.send("MOVE PTP 90.0 9    0.0 0.0 2.2 1.2 -3.14 1.57 0.0 -1.57 -3.14")
	udpClnt.send("MOVE PTP 90.0 9    0.0 0.0 0.0 1.2 -3.14 1.57 0.0 -1.57 -3.14")
	print udpClnt.getCurrentJointPosition()
	udpClnt.send("MOVE PTP 90.0 9    1.2 0.2 1.2 1.2 -3.14 1.57 0.0 -1.57 -3.14")
	udpClnt.stepBack()
	udpClnt.stepForward()

#Variablen um die Koordinaten auszuwerten
startx = 0
starty = 0
startz = 0

#Koordianten auswerten (Links -> Rechts // Rechts -> Links)
def distance(x,y,z):

    global startx, starty, startz
    
    if (startx == 0 and starty == 0 and startz ==0):
        
        startx = x
        starty = y
        startz = z
        print x,y,z
    
    deltax = startx - x
    deltay = starty - y
    deltaz = startz - z
    
    if ((deltay > 0.1) or (deltay < -0.1) or (deltaz > 0.1) or (deltaz < -0.1)):
        startx = x
        starty = y
        startz = z
        #print "if block"
    
    elif (deltax <= -0.40):
        
         #print "Befehl Start erkannt!"
         startx =0
         starty =0
         startz = 0
         udpClnt.send("MOVE PTP 90.0 9    0.0 0.0 0.0 1.2 -3.14 1.57 0.0 -1.57 -3.14")
    
    elif (deltax >= 0.40):
         
         #print "Befehl Stop erkannt!"
         startx =0
         starty =0
         startz = 0
         udpClnt.send("MOVE PTP 90.0 9    2.0 -2.2 -0.8 1.2 -3.14 1.57 0.0 -1.57 -3.14")
         
#While-Schleife vom Server / empfängt Koordinaten
while True:
        data,addr = UDPSock.recvfrom(1024)
        x = eval(data)
        distance(x[1],x[2],x[3])
        #print x

	


