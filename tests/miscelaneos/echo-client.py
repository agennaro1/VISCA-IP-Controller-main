
import socket

UDP_IP = "10.50.2.145"
UDP_PORT = 40000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # IPv4, UDP


while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received message: %s" % data)