import vrpn_Tracker
import socket
import sys

# Konstante der Tracker
TRACKER = "PPT0@141.82.50.174"

#*********************************************************************#
# Diese Klasse baut eine Verbindung zum PPT-Server auf und leitet     #
# die erhalteten Daten an die als Parameter angegebene Adresse weiter #
#*********************************************************************#
class Udp_server:
    def __init__(self,tracker_name,recv_ip,recv_port):
        self.tracker_name = tracker_name
        self.tracker = vrpn_Tracker.vrpn_Tracker_Remote(tracker_name)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.ip = recv_ip
        self.port = recv_port

    # Hier wird der Tracker mit der Handler-Funktion verknuepft
    def listen_to_tracker(self):
        vrpn_Tracker.register_tracker_change_handler(self.handler_tracker)
        vrpn_Tracker.vrpn_Tracker_Remote.register_change_handler(self.tracker,
                                                                 None,
                                                                 vrpn_Tracker.get_tracker_change_handler())
        while 1:
            vrpn_Tracker.vrpn_Tracker_Remote.mainloop(self.tracker)
    # Die Handler-Funktion schickt die Daten ueber UDP an die Adresse weiter
    def handler_tracker(self,userdata,t):
        self.sock.sendto(str(t), (self.ip, self.port))
        #print t

if __name__ == "__main__":
    if len( sys.argv ) == 3:
        client = Udp_server(TRACKER,str(sys.argv[1]),int(sys.argv[2]))
        client.listen_to_tracker()
    else:
        print "Argumente fehlen"
        print "python udp_server.py <RECEIVER_IP> <RECEIVER_PORT>"