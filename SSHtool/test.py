import os,sys
from paramiko import AutoAddPolicy,Transport,Channel,client,SSHClient
from time import sleep
#set root password. input user's password,new password,retype password
setpassword=['sudo passwd root','12345678','12345678','12345678']
#modify /root/.profile
modifyrootprofile=['sudo sed \'s/mesg n/tty -s && mesg n/g\'','12345678']
#modify ssh_config
modifysshconfig=['sudo sed \'s/PermitRootLogin prohibit-password/PermitRootLogin yes/g\' /etc/ssh/sshd_config','12345678','sudo service ssh restart']
#
sshclt=SSHClient()
sshclt.set_missing_host_key_policy(AutoAddPolicy())
sshclt.connect(hostname='192.168.220.129',port=22,username='wz',password='12345678')
chan=sshclt.invoke_shell()
for com in setpassword:
    chan.send(com+'\n')
    sleep(3)
while(True):
    tmp=chan.recv(1000)
    print(tmp.decode())

if __name__=='__main__':
    pass