import socket
import string

UDP_IP = "141.82.175.206"
UDP_PORT = 5555

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
x = 0
while True:
    x += 1
    data, addr = sock.recvfrom(1024)
    if x == 100:
        t_data = eval(data)
        print "X=",t_data[1]
        print "Y=",t_data[2]
        print "Z=",t_data[3]
        x = 0
