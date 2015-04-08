import socket

class UdpClnt:
	
	def __init__(self, UDP_IP, UDP_PORT, currentPosition = " ", lastPosition = " ", sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM), interruptFlag = False):
		self.__UDP_IP = UDP_IP
		self.__UDP_PORT = UDP_PORT
		self.__currentPosition = currentPosition
		self.__lastPosition = lastPosition
		self.sock = sock
		self.__interruptFlag = interruptFlag 
		
	#Getter CurrentPosition
	def __getCurrentPosition(self):
		return self.__currentPosition
	
	#Setter CurrentPosition
	def __setCurrentPosition(self, position):
		self.__currentPosition = position
	
	#Getter LastPosition
	def __getLastPosition(self):
		return self.__lastPosition
	
	#Setter LastPosition
	def __setLastPosition(self, position):
		self.__lastPosition = position
		
	#Getter LastPosition
	def __getInterruptFlag(self):
		return self.__interruptFlag
	
	#Setter LastPosition
	def __setInterruptFlag(self, flag):
		self.__interruptFlag = flag
	
	#Probertys
	currentPosition = property(__getCurrentPosition, __setCurrentPosition)
	lastPosition = property(__getLastPosition, __setLastPosition)
	interruptFlag = property(__getInterruptFlag, __setInterruptFlag)
	

	#CurrentJointPosition in MoveBefehl umwandeln
	def JointPositionToMoveCommand(self, jointPosition):
		return "MOVE PTP 90.0 9     " + jointPosition

	#Daten senden
	def send(self, befehl):
		self.__setLastPosition(self.getCurrentJointPosition())
		self.sock.sendto(befehl, (self.__UDP_IP, self.__UDP_PORT)) #Befehl senden
		rueckmeldung = self.receive()				#Wenn Rueckmeldung dann Ausprinten
		if len(rueckmeldung) != 0:
			print rueckmeldung
			
	#Daten empfangen
	def receive(self):
		recv_data, addr = self.sock.recvfrom(self.__UDP_PORT)
		return recv_data

	#akutelle Position des Virtuelle Roboters
	def getCurrentJointPosition(self):
		self.sock.sendto("GET CURRENTJOINTPOSITION", (self.__UDP_IP, self.__UDP_PORT)) #Befehl senden
		self.__setCurrentPosition(self.receive())
		return self.__getCurrentPosition()

	#Schritt zurück
	def stepBack(self):
		self.send(self.JointPositionToMoveCommand(self.__getLastPosition()))

	#Schritt vorwärts
	def stepForward(self):
		if len(self.__getCurrentPosition()) != 0: 
			self.send(self.JointPositionToMoveCommand(self.__getCurrentPosition()))
		else:
			print "Kein Vorwärtsschritt vorhanden"
			
	#Simulation abbrechen
	def sendInterrupt(self):
		self.send("InterruptBefehl")
		
	
