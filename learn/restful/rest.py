#-*-coding:UTF-8-*-
import socket,sys,urllib
from BaseHTTPServer import *

class Restful(BaseHTTPRequestHandler):  #所有rest的父类
    def __init__(self,request, client_address, server):
        BaseHTTPRequestHandler.__init__(self,request, client_address, server)
        self.dp=None
        self.router=None
        
    def basepath(self):
        pass
    def getresetlet(self):
        pass
    def send(self,src):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(src)
        self.wfile.close()
    def done(self):
        self.dp=self.basepath()
        self.router=self.getrestlet()

class Test(Restful):            #测试1
    def test(self):  #这就是一个资源
        return "{\"date\":\"2013-11-19\"}"
    def do_GET(self):  #重写get方法给了通过客户端请求的url找到对应的资源
        self.done()
        for key in self.router.keys():
            tmp=self.dp+key
            if tmp in self.path:
                  self.send(self.router[key]()) #执行资源
    def basepath(self): #这个简单的说就是和下面函数中的路径配合，即/wm/time
        return "/wm"
    def getrestlet(self):  #这儿就是URI与资源对应，这里只有test资源，可以注册多个
        rr={}
        rr['/time']=self.test 
        return rr

class testjson(Restful):      #测试2
    def testjson(self,vpc,vr):  #这里比测试1复杂些，因为参数的值需要从url中获得
        src1="{\"vpc\":1,\"vrouter\":3,\"day\":[1,2,3]}"
        src2="{\"vpc\":1,\"vrouter\":4,\"day\":[23,21,3]}"
        src3="{\"vpc\":5,\"vrouter\":3,\"day\":[13,2,23]}"
        tlist=[src1,src2,src3]
        cmpvpc="\"vpc\":"+vpc
        cmpvr="\"vrouter\":"+vr
        for k in tlist:
            if cmpvpc in k and cmpvr in k:
                return k
    def firewall(self):
        return "{\"filter\":[\"baid.com/\",\"c.cn/\"],\"acl\":{\"accept\":123,\"reject\":321}}"
    def do_GET(self):  #重写GET，解析url，这里的self.path类似：/ins/json?vpc=1&vrouter=3
        self.done()
        print self.path
        if 'vpc' in self.path and 'vrouter' in self.path:
            query=None
            if '?' in self.path:
                query =    urllib.splitquery(self.path)
            key=query[0]+'?'
            param=query[1].split('&') #解析获得属性信息，传递给资源函数
            pdict={}
            for p in param:
                tmp=p.split('=')
                pdict[tmp[0]]=tmp[1]  
            for k in self.router.keys():
                if k in key:
                    self.send(self.router[k](pdict['vpc'],pdict['vrouter'])) #执行资源
        elif 'firewall' in self.path:
            self.send(self.router['/firewall']())
        else:
            self.send("{}")
    def basepath(self):
        return "/ins"
    def getrestlet(self):
        rr={}
        rr['/json?']=self.testjson #注册资源
        rr['/firewall']=self.firewall
        return rr
        
            
try:
    server=HTTPServer(('',8084),testjson) #测试2
    server.serve_forever()
except KeyboardInterrupt:
    sys.exit(0)