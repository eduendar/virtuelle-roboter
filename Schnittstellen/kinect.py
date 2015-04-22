import socket
import UdpClnt_Python

#UdpSocket
UDPSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
listen_addr = ("141.82.50.192", 30000)
UDPSock.bind(listen_addr)

#UdpClient
udpClnt = UdpClnt_Python.UdpClnt("141.82.50.192", 50000)

stringPosition = []
floatPosition = []

#StringListe in floatListe umwandeln
def stringListToflaotList(liste):
		#Einzelne Koordinaten in float umwandeln
		for x in liste:
			floatPosition.append(float(x))
		return floatPosition
		
#While-Schleife vom Server / empfängt Koordinaten
while True:
	data,addr = UDPSock.recvfrom(1024)
	
	#Befehl gerade aus // 80 cm nach vorne
	if data == 'a':
		#aktuelle Position des Roboters holen und aufsplitten
		stringPosition = udpClnt.getCurrentJointPosition().split( )
		stringListToflaotList(stringPosition)
		floatPosition[0] += 0.80
		#Movecommand senden
		udpClnt.send(udpClnt.JointPositionToMoveCommand(' '.join(map(str, floatPosition))))
	
	#Befehl zurück // 80 cm nach hinten
	elif data == "b":
		#aktuelle Position des Roboters holen und aufsplitten
		stringPosition = udpClnt.getCurrentJointPosition().split( )
		stringListToflaotList(stringPosition)
		floatPosition[0] -= 0.80
		#Movecommand senden
		udpClnt.send(udpClnt.JointPositionToMoveCommand(' '.join(map(str, floatPosition))))
	
	#Befehl rechts // 80 cm nach rechts
	elif data == "c":
		#aktuelle Position des Roboters holen und aufsplitten
		stringPosition = udpClnt.getCurrentJointPosition().split( )
		stringListToflaotList(stringPosition)
		floatPosition[1] -= 0.80
		#Movecommand senden
		udpClnt.send(udpClnt.JointPositionToMoveCommand(' '.join(map(str, floatPosition))))
	
	#Befehl links // 80 cm nach links
	elif data == "d":
		#aktuelle Position des Roboters holen und aufsplitten
		stringPosition = udpClnt.getCurrentJointPosition().split( )
		stringListToflaotList(stringPosition)
		floatPosition[1] += 0.80
		#Movecommand senden
		udpClnt.send(udpClnt.JointPositionToMoveCommand(' '.join(map(str, floatPosition))))
	
	#Schritt zurück
	elif data == "e":
		udpClnt.stepBack()
	
	#Schritt vorwärts
	elif data == "f":
		udpClnt.stepForward()
	
	#Wenn Befehl nicht vorhanden
	else:
		print "Befehl nicht vorhanden " + data
