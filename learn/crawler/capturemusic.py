# -*- coding: utf-8 -*-
#!/usr/bin/python
import urllib2,sys,sqlite3
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def  __init__(self):
        HTMLParser.__init__(self)
        self.t=False
        self.trans=[]
        self.prs=[]
        self.pr=False
    def handle_starttag(self, tag, attrs):
        if tag=='div':
            for attr in attrs:
                if attr==('class','hd_prUS') or \
                 attr==('class','hd_pr'):
                    self.pr=True
        if tag=='span':                       
            for attr in attrs:
                if attr==('class','def'):
                    self.t=True
    def handle_data(self, data):
        if self.t:
            length=len(self.trans)+1
            self.trans.append(str(length)+". "+data)
            self.t=False
        if self.pr:
            self.prs.append(data)
            self.pr=False
    def getTrans(self):
        return self.trans
    def getPr(self):
        return self.prs
class trans:
    _URL='http://cn.bing.com/dict/search'
    _DBPATH='./dic.sqlite'        #���ݿ��ļ�λ��
    def __init__(self):
        self.url=trans._URL+"?q=%s&go=&qs=bs&form=CM&mkt=zh-CN&setlang=ZH"
        self.html=None
        self.s=None               #���淭��
        self.pr=None              #���淢����US��UK��
        self.word=None            #���浥��
        self.conn=sqlite3.connect(trans._DBPATH)
        self.cur = self.conn.cursor()
    def getHtml(self):
        self.url=self.url %self.word
        req = urllib2.Request(self.url)
        fd=urllib2.urlopen(req)
        self.html=fd.read()
        self.html=unicode(self.html,'utf-8')
        fd.close()
    
    def parseHtml(self):
        parser = MyHTMLParser()
        self.html=parser.unescape(self.html) #����&��&#�ȿ�ͷ�������ַ���
        parser.feed(self.html)
        self.s=parser.getTrans()
        self.pr=parser.getPr()
        print self.word,':'
        #for sk in self.pr:
        print self.pr[0],',',self.pr[1]
        print ''
        for i in self.s:
            print i

    def saveDB(self):            #�ѵ�����Ϣ�������ݿ�
        sjoin='\n'.join(self.s)
        uspr=self.pr[0]
        ukpr=self.pr[1]
        #self.cur.execute("create table if not exists  translate ( word CHAR(40) primary key, us CHAR(40), uk CHAR(40), trans text )")
        self.cur.execute("insert into translate values(?,?,?,?);", \
                    (self.word,uspr,ukpr,sjoin))
        self.conn.commit()

    def isExists(self,word):     #�жϵ����Ƿ���db�У������ֱ�Ӵ�ӡ������
        self.word=word
        rows=self.cur.execute("select * from translate where word=?",(self.word,))
        key=rows.fetchall()
        if key==[]:
            return False
        else:
            for row in key:
                print row[0],':'
                print row[1],",",row[2]
                print ''
                print row[3]
            return True
    def select(self):              #���Բ鿴�õģ�ɾ��ɾ����ν��
        rows=self.cur.execute("select * from translate")
        for row in rows:
            print row[0]
            print row[1],",",row[2]
            print row[3]
    def closeDB(self):
        self.conn.close()
if __name__=='__main__':
    t=trans()    
    flag=t.isExists(sys.argv[1])  
    if not flag:
        t.getHtml()
        t.parseHtml()
        t.saveDB()
    # t.select()
    t.closeDB()