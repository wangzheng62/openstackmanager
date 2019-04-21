import socket
s1=socket.socket()
s1.connect(('192.168.220.129',22))
s1.send(b'pwd')
print(s1.recv(100).decode())