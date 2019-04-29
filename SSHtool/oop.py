#oop的第一次尝试，不谈实现只写框架
#核心类的定义
#目标服务器
class Servernode():
    def __init__(self):
        pass
    def excutecommand(self):
        pass
    def excutelog(self):
        pass
    def applist(self):
        pass
#控制中心,接受服务器列表和待执行命令，将命令发送到每个服务器，并监控执行结果
class Controlcenter():
    def __init__(self):
        pass
    def Serverstatus(self):
        return {}
#命令wrapper，将脚本，bash命令分解重组为规范命令
class Commandwrapper():
    def __init__(self):
        pass
