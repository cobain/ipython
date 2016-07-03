#-*-coding:UTF-8-*-
import socket,sys,urllib
from BaseHTTPServer import *

class Restful(BaseHTTPRequestHandler):  #����rest�ĸ���
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

class Test(Restful):            #����1
    def test(self):  #�����һ����Դ
        return "{\"date\":\"2013-11-19\"}"
    def do_GET(self):  #��дget��������ͨ���ͻ��������url�ҵ���Ӧ����Դ
        self.done()
        for key in self.router.keys():
            tmp=self.dp+key
            if tmp in self.path:
                  self.send(self.router[key]()) #ִ����Դ
    def basepath(self): #����򵥵�˵���Ǻ����溯���е�·����ϣ���/wm/time
        return "/wm"
    def getrestlet(self):  #�������URI����Դ��Ӧ������ֻ��test��Դ������ע����
        rr={}
        rr['/time']=self.test 
        return rr

class testjson(Restful):      #����2
    def testjson(self,vpc,vr):  #����Ȳ���1����Щ����Ϊ������ֵ��Ҫ��url�л��
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
    def do_GET(self):  #��дGET������url�������self.path���ƣ�/ins/json?vpc=1&vrouter=3
        self.done()
        print self.path
        if 'vpc' in self.path and 'vrouter' in self.path:
            query=None
            if '?' in self.path:
                query =    urllib.splitquery(self.path)
            key=query[0]+'?'
            param=query[1].split('&') #�������������Ϣ�����ݸ���Դ����
            pdict={}
            for p in param:
                tmp=p.split('=')
                pdict[tmp[0]]=tmp[1]  
            for k in self.router.keys():
                if k in key:
                    self.send(self.router[k](pdict['vpc'],pdict['vrouter'])) #ִ����Դ
        elif 'firewall' in self.path:
            self.send(self.router['/firewall']())
        else:
            self.send("{}")
    def basepath(self):
        return "/ins"
    def getrestlet(self):
        rr={}
        rr['/json?']=self.testjson #ע����Դ
        rr['/firewall']=self.firewall
        return rr
        
            
try:
    server=HTTPServer(('',8084),testjson) #����2
    server.serve_forever()
except KeyboardInterrupt:
    sys.exit(0)