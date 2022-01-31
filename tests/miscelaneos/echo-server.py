'''

import socket
import struct
import codecs
import sys
import binascii

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', 40000))
mreq = struct.pack("=4sl", socket.inet_aton("224.51.105.104"), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
   codigo = sock.recv(1024)
   #print(codigo)
   #print(binascii.crc32(codigo))
   print(binascii.b2a_hex(codigo))
   #print(binascii.b2a_base64(codigo))
   #print(binascii.b2a_qp(codigo, quotetabs=False, istext=True, header=False))
   

'''



import socket
import binascii

camera_ip = '10.50.2.145'
camera_port = 40000
buffer_size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', camera_port))

visca_response_dictionary = {
    b'01':'sequence number reset',
    b'0f01':'sequence number error',
    b'9041ff':'acknowledge',
    b'9051ff':'complete',
}

while True:
    data = s.recvfrom(buffer_size)
    message = data[0]
    address_port = data[1]
    address = address_port[0]
    port = address_port[1]
    payload_type = message[0:2]
    payload_length = int(binascii.hexlify(message[2:4]), 16)
    sequence_number = int(binascii.hexlify(message[4:8]), 16)
    payload = binascii.hexlify(message[8:])
    message_type = payload[0:8]
    print(data)
    print('sequence_number', sequence_number)
    print('address', address)
    print('port', port)
    print('payload_type', payload_type)
    print('payload_length', payload_length)
    print('payload', payload)
    try:
        print(sequence_number, visca_response_dictionary[message_type])
    except:
        print(sequence_number, payload)