#coding=utf8
#! /usr/bin/env python

#

import urllib
import urllib2
import httplib
import json

url = "http://api.thinkpage.cn/weather/api.svc/getWeather?city=101010100&language=zh-chs&unit=c&aqi=city&format=json&key=OEDZ0TJPOA"
def using_httplib():
    pass


def using_urllib():
    page = urllib.urlopen(url)
    print "status", page.getcode()
    print "url:", page.geturl()
    print "head_info:\n", page.info()
    return page.read()
    pass



def using_urllib2():
    pass


def parseXml(page):
    pass

def parseJson(page):
    pass

def getContentType(type):
    pass


if __name__ == "__main__":
    resp = using_urllib()
    print json.dumps(resp, sort_keys=True, indent=4, separators=(',', ': '))
    obj = json.loads(resp)
    weatherArry =  obj["Weathers"]
    print weatherArry
    firstitem = weatherArry[0]
    print firstitem
    print firstitem["CityName"]
    
