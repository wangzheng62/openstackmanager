#oop的第一次尝试，不谈实现只写框架
#核心类的定义
#目标服务器
class Servernode():
    def __init__(self):
        pass
    def excutecommand(self):
        return True
    def excutelog(self):
        pass
    def applist(self):
        pass
    def serverstatus(self):
        pass

class Bash(Servernode):
    def sed(self):
        return True
    def apt(self):
        return True
#控制中心,接受服务器列表和待执行命令，将命令发送到每个服务器，并监控执行结果
class Controlcenter():
    def __init__(self):
        pass
    def serverstatus(self):
        return {}
#命令wrapper，将脚本，bash命令分解重组为规范命令
class Commandwrapper():
    def __init__(self):
        pass
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
