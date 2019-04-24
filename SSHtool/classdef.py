import os,sys,subprocess,re
from paramiko import AutoAddPolicy,Transport,Channel,client,SSHClient
from socket import socket
from time import sleep
import datetime
#string match
def strmatch(substr,str):
    res=str.find(substr)
    if res==-1:
        return False
    else:
        return True
#get time
lt=datetime.datetime.now()
#server define
class SSHServer():
    __slots__ = ('hostname','port','username','password')
    def __init__(self,hostname,username='root',password=None,port=22):
        self.hostname=hostname
        self.port=port
        self.username=username
        self.password=password

    def is_online(self):
        # regular pattern
        pattern = r'丢失 = .'
        p = re.compile(pattern)
        # windows
        tmp = os.popen('ping {}'.format(self['hostname']))
        infoes = tmp.readlines()
        info = ' '
        for i in infoes:
            info = info + i
        # match stdout
        print(info)
        m = p.search(info)  # return None if no position in the string matches the pattern
        if m != None:
            if m.group()[-1] == '0':
                print('ping 成功')
                return True
            else:
                print('ping 失败')
                return False

    def ssh_ready(self):
        client = SSHClient()
        client.set_missing_host_key_policy(AutoAddPolicy())
        try:
            client.connect(hostname=self['hostname'], port=self['port'], username=self['username'],
                           password=self['password'])
            print('连接成功')
            client.close()
            return True
        except Exception as e:
            print(e)
            print('连接失败')
            return False
#command define
def exec_command(server,command):
    sock=socket()
    sock.connect((server.hostname,server.port))
    tran=Transport(sock)
    tran.connect(username=server.username,password=server.password)
    chan=tran.open_channel(kind='session')
    chan.invoke_shell()
    chan.send('nohup '+command+'>>sshlog '+'2>&1 '+'&'+'\n')
    chan.send('jobs -l'+'\n')
    i=0
    res=False
    while(True):
        i=i+1
        tmp=chan.recv(1000).decode()
        print(i)
        print(tmp)
        if strmatch('Done',tmp):
            print('[{}]   >>>{}<<<  执行成功'.format(lt,command))
            res=True
            break

        if strmatch('Exit',tmp):
            print('[{}]   >>>{}<<<  执行失败'.format(lt, command))

            break

        chan.send('jobs -l' + '\n')
        sleep(5)

    return res




#script
class Script():
    def __init__(self,file):
        with open(file,mode='r') as fileobj:
            filecontent=fileobj.read()
            tmp=filecontent.split('\n')
            print(tmp)
        self.commandlist=tmp


#initial
def initial(server,commandlist):
    sshclt = SSHClient()
    sshclt.set_missing_host_key_policy(AutoAddPolicy())
    sshclt.connect(hostname=server.hostname, port=server.port, username=server.username, password=server.password)
    chan = sshclt.invoke_shell()
    for com in commandlist:
        chan.send(com)
        chan.send('\n')
        sleep(3)
    tmp = chan.recv(1000)
    print(tmp.decode())
if __name__=='__main__':
    # set root password. input user's password,new password,retype password
    setpassword = ['sudo passwd root', '12345678', '12345678', '12345678']
    # modify /root/.profile
    modifyrootprofile = [r"sudo sed -i 's/mesg n/tty -s \&\& mesg n/g' /root/.profile", '12345678']
    # modify ssh_config 16.04
    modifysshconfig1604 = [
        'sudo sed -i \'s/PermitRootLogin prohibit-password/PermitRootLogin yes/g\' /etc/ssh/sshd_config', '12345678',
        'sudo service ssh restart']
    # modify ssh_config 18.04
    modifysshconfig1804 = ['sudo chmod u+w /etc/ssh/sshd_config', '12345678',
                           r"sudo sed -i 's/\#PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config",
                           '12345678', 'sudo service ssh restart']
    server1={
        'hostname':'192.168.220.129',
        'port':22,
        'username':'wz',
        'password':'123456789'
    }
    ss=SSHServer(**server1)
    print(ss.username)
    sc=Script('d:/1234.txt')
    command='apt -y -f remove sslscannn'
    command1='sudo su \n 123456789'
    res=exec_command(ss,command1)
    print(lt)
    print(res)



