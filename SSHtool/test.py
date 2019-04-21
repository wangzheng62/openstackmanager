import os,sys
from paramiko import AutoAddPolicy,Transport,Channel,client,SSHClient
from time import sleep
sys.path.append(os.path.abspath('..'))
print(sys.path)
from SSHtool.interactive import windows_shell
#transport
tran=Transport(('192.168.220.129',22))
tran.connect(username='wz',password='12345678')
#client
UBUNTU01={'hostname':'192.168.0.123'}
client01=SSHClient()
client01.set_missing_host_key_policy(AutoAddPolicy())
client01.connect(hostname='192.168.220.129',port=22,username='wz',password='12345678')
chan=client01.invoke_shell()
windows_shell(chan)
print(chan.__str__())
#chan.setblocking(1)
#chan.settimeout(2.0)
#chan.send('sudo apt -y -f remove sslscan'+'\n'+'12345678'+'\n')
#chan.send('pwd'+'\n')
#chan.send('ping 127.0.0.1 \n')
#sleep(10)
#inf=chan.recv(20000)
#print(inf.decode())
client01.close()
