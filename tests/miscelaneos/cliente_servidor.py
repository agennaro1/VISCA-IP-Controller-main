import socket
import sys
 
# Create a TCP/IP socket
stream_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Define host
host = 'localhost'
 
# define the communication port
port = 64589
 
# Connect the socket to the port where the server is listening
server_address = ((host, port))
 
print ("connecting")

stream_socket.connect(server_address)
 
 
# Send data
message = 'message'
stream_socket.sendall(message)
 
# response
data = stream_socket.recv(10)
print (data)
 
 
print ('socket closed')
stream_socket.close()