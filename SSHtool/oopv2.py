#oop的第二次尝试，不谈实现只写框架
#基于数据ipo
#input
def getcommand(command):
    res=command
    return res
def getserver(**kw):
    servernode=kw
    return servernode
#process
def exec(servernode,command):
    info={'servernode':servernode,
    'command':command,
    'stdout':'',
    'stderr':''}
    return info
#out
def check(info):
    if info['stdout'] and not info['stderr']:
        return True
    elif info['stderr']:
        return False
    else:
        raise Exception('no info')
#control
def control(commandlist,servernode):
    for com in commandlist:
        command=getcommand(com)
        node=getserver(servernode)
        info=exec(node,command)
        while(not check(info)):
            exec(node, command)
