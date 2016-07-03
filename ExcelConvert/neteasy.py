# encoding=utf-8

import urllib2
import json
import re
import time

class JSON():
    def __init__(self):
        self.user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers={'User-Agent':self.user_agent}
        self.url1='http://comment.news.163.com/data/news_guonei8_bbs/df/SPEC0001B60046CG_1.html'
    def getUrls(self,pageIndex):
        url2='http://comment.news.163.com/cache/newlist/news_guonei8_bbs/SPEC0001B60046CG_'+str(pageIndex)+'.html'
        return url2
    def getHtml(self,url):
        try:
            request=urllib2.Request(url,headers=self.headers)
            respone=urllib2.urlopen(request)
            html=respone.read()
            return html
        except urllib2.URLError,e:
            if hasattr(e,'reason'):
                print u"连接失败",e.reason
                return  None
    #处理字符串，没有处理干净的可以再打开文件进行处理
    def strDeal(self,data,pageIndex):
        if pageIndex==1:
            data=data.replace('var replyData=','')
        else:
            data=data.replace('var newPostList=','')
        reg=re.compile("&nbsp;\[<a href=''>")
        data=reg.sub('--',data)
        reg2=re.compile('<\\\/a>\]')#<\/a>]的正则?
        data=reg2.sub('',data)
        reg3=re.compile('<br>')
        data=reg3.sub('',data)
        return data
    #解析json数据并存入文件
    def parserJson(self):
        with open('wangyi2.txt','a') as f:
            f.write('用户ID'+'|'+'评论'+'|'+'点赞数'+'\n')

        for i in range(1,35):
            if i==1:
                url=self.url1
                data=self.getHtml(url)
                data=self.strDeal(data,i)[:-1]
                value=json.loads(data)
                f=open('wangyi2.txt','a')

                for item in value['hotPosts']:
                    f.write(item['1']['f'].encode('utf-8')+'|')
                    f.write(item['1']['b'].encode('utf-8')+'|')
                    f.write(item['1']['v'].encode('utf-8')+'\n')
                f.close()
                print 'sleeping pageload %d/34'%i
                time.sleep(6)
            else:
                url=self.getUrls(i)
                data=self.getHtml(url)
                data=self.strDeal(data,i)[:-2]
                # 转换，一开始得到的数据类型为str，使用json.loads()函数，得到原始数据，此时的value的数据类型为dict，接下来就可以正常访问字典了。
                value=json.loads(data)
                f=open('wangyi2.txt','a')

                for item in value['newPosts']:
                    f.write(item['1']['f'].encode('utf-8')+'|')
                    f.write(item['1']['b'].encode('utf-8')+'|')
                    f.write(item['1']['v'].encode('utf-8')+'\n')

                f.close()
                print 'sleeping pageload %d/34'%i
                time.sleep(6)


js=JSON()
js.parserJson()