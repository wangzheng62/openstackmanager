import os,sys
class File():
    def __init__(self,file,mode):
        f=open(file,mode,encoding='utf-8')
        rd=f.read()
        self.content=rd
        f.close()
    def splitfile(self,splitstr,path,filetype='.txt'):
        print(os.path.isdir(path))
        if os.path.isdir(path):
            pass
        else:
            os.mkdir(path)
        l=self.content.split(splitstr)
        print(len(l))
        for index,s in enumerate(l):
            f=open(path+'\\'+'{}'.format(str(index))+filetype,'w',encoding='utf-8')
            f.write(s)
            f.close()
if __name__=='__main__':
    f=File(r'D:\文本\bare\一部顶二百部的[h小说].txt','r')
    f.splitfile('全文完',r'D:\文本\test')