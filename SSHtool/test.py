import os,sys
from paramiko import AutoAddPolicy,Transport,Channel,client,SSHClient
from time import sleep
#set root password. input user's password,new password,retype password
setpassword=['sudo passwd root','12345678','12345678','12345678']
#modify /root/.profile
modifyrootprofile=[r"sudo sed -i 's/mesg n/tty -s \&\& mesg n/g' /root/.profile",'12345678']
#modify ssh_config 16.04
modifysshconfig1604=['sudo sed -i \'s/PermitRootLogin prohibit-password/PermitRootLogin yes/g\' /etc/ssh/sshd_config','12345678','sudo service ssh restart']
#modify ssh_config 18.04
modifysshconfig1804=['sudo chmod u+w /etc/ssh/sshd_config','12345678',r"sudo sed -i 's/\#PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config",'12345678','sudo service ssh restart']
sshclt=SSHClient()
sshclt.set_missing_host_key_policy(AutoAddPolicy())
sshclt.connect(hostname='192.168.0.123',port=22,username='wz',password='12345678')
chan=sshclt.invoke_shell()
for com in modifysshconfig1804:
    chan.send(com)
    chan.send('\n')
    sleep(3)
tmp=chan.recv(1000)
print(tmp.decode())

if __name__=='__main__':
    pass