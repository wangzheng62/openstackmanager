from paramiko.client import SSHClient
from paramiko import AutoAddPolicy,Transport
from time import sleep
UBUNTU01={'hostname':'192.168.0.123'}
clent01=SSHClient()
clent01.set_missing_host_key_policy(AutoAddPolicy())
clent01.connect(hostname='192.168.0.123',port=22,username='wz',password='12345678')
chan=clent01.invoke_shell()
chan.send('pwd'+'\n')
sleep(3)
s=chan.recv(10000)
print(s)
chanid=chan.get_id()
print(chanid)
clent01.close()