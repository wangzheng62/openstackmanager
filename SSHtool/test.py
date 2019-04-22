import os,sys
from paramiko import AutoAddPolicy,Transport,Channel,client,SSHClient
from time import sleep
import socket
socket01=socket.socket()
socket01.connect(('192.168.220.129',22))
tran=Transport(socket01)
tran.connect(username='root',password='123456789')
print(tran.is_active())
chan=tran.open_channel(kind='session')
chan.invoke_shell()
com='sudo apt -y -f install sslscan \n' \
        '12345678\n'
com1='pwd\n'
com2='apt-get -y -f install sslscan\n'
chan.send(com2)
sleep(5)
if chan.recv_stderr_ready():
    print(chan.recv_stderr(10000).decode())
else:
    print(chan.recv(10000).decode())