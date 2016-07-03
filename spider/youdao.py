__author__ = 'zhenghaitao'
# coding: utf-8
# !/usr/bin/env python

import re
import time
import thread
import urllib
import urllib2
from urllib import quote


class Spider_Youdao:

    def __init__(self):

        self.Trans_Youdao_Tag = re.compile(r'\s?<li>.*?</li>\s?')
        self.Trans_Shiji_Tag = re.compile(r'\s?<span.*?class="def">.*?</span>')
        self.run = True


    def SearchWord(self):
        S_Word = raw_input("\n#[输入单词]\n>")

        return S_Word


    def GetUrl(self):
        SWord = self.SearchWord()
        if quote(SWord) == SWord:
            MyUrl = "http://dict.youdao.com/search?len=eng&q="+quote(SWord)+"&keyfrom=dict.top"
            return MyUrl


    def GetPage(self):
        Youdao_Url = self.GetUrl()
        user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:32.0) Gecko/20100101 Firefox/32.0'
        headers = { 'User-Agent' : user_agent }
        req = urllib2.Request(Youdao_Url, headers = headers)
        Res = urllib2.urlopen(req)
        ResultPage = Res.read().decode("utf-8")
        return ResultPage


    def ExtractPage(self):
        MyPage = self.GetPage()
        YoudaoTrans = self.Trans_Youdao_Tag
        ShijiTrans = self.Trans_Shiji_Tag
        print "--------------------------------------------"
        YouDaoTrans = self.Trans_Youdao_Tag
        TransYdIterator = YouDaoTrans.finditer(MyPage)
        print "#(翻译来自有道词典):"
        myItems = re.findall('<div.*?class="trans-container">(.*?)<div id="webTrans" class="trans-wrapper trans-tab">',MyPage,re.S)
        for item in myItems:
            YDTmp = item
        TransYdIterator = YouDaoTrans.finditer(YDTmp)
        for iterator in TransYdIterator:
            YouDao = iterator.group()
            YDTag = re.compile('\s?<.*?>')
            print YDTag.sub('',YouDao)
        print "--------------------------------------------"
        TransSjIterator = ShijiTrans.finditer(MyPage)
        print "#(翻译来自21世纪大词典):"
        for iterator in TransSjIterator:
            ShiJi = iterator.group()
            SJTag = re.compile('\s?<.*?>')
            print SJTag.sub('',ShiJi)
        print "--------------------------------------------"


    def Start(self):
        while self.run:
            S_Word = raw_input("\n#[\"!\"号退出.回车继续.]\n>")
            if S_Word != "!":
                self.ExtractPage()
                #thread.start_new_thread(self.ExtractPage,())
                #time.sleep(5)
            else:
                self.run = False



if __name__ == '__main__':
    mydict = Spider_Youdao()
    mydict.Start()