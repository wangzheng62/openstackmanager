#oop的第一次尝试，不谈实现只写框架
from paramiko import AutoAddPolicy,Transport,Channel,client,SSHClient
import os
#核心类的定义
#shell
class ShellBase():

    pass
class BASH(ShellBase):
    path='/bin/bash'
    def sudo(self,password,command):
        default=r'echo {}|sudo -S {}'.format(password,command)
        res=default
        return res
#目标服务器
class Servernode(dict):
    def __init__(self,**kwargs):
        super(Servernode,self).__init__(**kwargs)

#控制中心,接受服务器列表和待执行命令，将命令发送到每个服务器，并监控执行结果
class Controlcenter():
    def __init__(self):
        pass
    def serverstatus(self):
        return {}
#命令wrapper，将脚本，bash命令分解重组为规范命令
class Commandwrapper():
    def getbytes(self,target):
        print('二进制参数')
    def getstrs(self,target):
        print('字符串参数')
        #去除两端空格
        target=target.strip()
        #管道划分
        if '|' in target:
            tmp=[]
            subset=target.split('|')
            for sub in subset:
               tmp.append(sub.split())
            target=tmp
        return target
    def getfile(self,target):
        print('文件参数')


#过程定义
def getserver(*server,**serverlist):
    #single ip
    '192.168.0.1'
    #
    '192.168.0.1','192,168,0,2','192.168,0,3'
    #
    '192.168.0.1-25'
    return ['192.168.0.1','192,168,0,2','192.168,0,3']
def serverformat():
    return {'hostname':'192.168.0.1',
            'port':22,
            'username':'root',
            'password':'12345678'}
if __name__=='__main__':
    password='12345678'
    command='   echo 123456|sudo apt-get update   '
    wrap=Commandwrapper()
    com1=wrap.getstrs(command)
    print(com1)
