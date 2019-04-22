#use execute
import os,sys,subprocess,re
from paramiko import AutoAddPolicy,Transport,Channel,client,SSHClient
from time import sleep

class target(dict):
#test server
    #IP
    def testip(self):
        #regular pattern
        pattern=r'丢失 = .'
        p=re.compile(pattern)
        #windows
        tmp=os.popen('ping {}'.format(self['hostname']))
        infoes=tmp.readlines()
        info=' '
        for i in infoes:
            info=info+i
        #match stdout
        print(info)
        m=p.search(info)#return None if no position in the string matches the pattern
        if m!=None:
            if m.group()[-1]=='0':
                print('ping 成功')
                return True
            else:
                print('ping 失败')
                return False
    #SSh
    def testssh(self):
        client=SSHClient()
        client.set_missing_host_key_policy(AutoAddPolicy())
        try:
            client.connect(hostname=self['hostname'],port=self['port'],username=self['username'],password=self['password'])
            print('连接成功')
            client.close()
        except Exception as e:
            print(e)
            print('连接失败')
    #execute
    def dosingletask(self,command):
        client = SSHClient()
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(hostname=self['hostname'],port=self['port'],username=self['username'],password=self['password'])
        stdin,stdout,stderr=client.exec_command(command)
        print(dir(stdout))
        print(stdout.read())
        print(stderr.read())
        client.close()
    #shell
    def doinshell(self,str):
        client = SSHClient()
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(hostname=self['hostname'], port=self['port'], username=self['username'], password=self['password'])
        chan=client.invoke_shell()
        chan.send(str)
        if chan.recv_stderr_ready():
            print(chan.recv_stderr(10000))
        else:
            print('没有报错信息')

if __name__=='__main__':
    server={'hostname':'192.168.220.129',
    'port':22,
    'username': "wz",
    'password':'12345678'
    }
    t1=target(server)
    print(t1)
    com='sudo apt -y -f install sslscan \n' \
        '12345678\n'

    t1.doinshell(com)