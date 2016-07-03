#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
【版本信息】
版本：     v1.0
作者：     crifan

【详细信息】
用于：
【教程】抓取网并网页中所需要的信息 之 Python版 
http://www.crifan.com/crawl_website_html_and_extract_info_using_python/
的示例代码。

-------------------------------------------------------------------------------
"""

#---------------------------------import---------------------------------------
import urllib2;
import re;
from BeautifulSoup import BeautifulSoup;

#------------------------------------------------------------------------------
def main():
    userMainUrl = "www.baidu.cn";
    req = urllib2.Request(userMainUrl);
    resp = urllib2.urlopen(req);
    respHtml = resp.read();
    save_path = 'D:\Ac\mm.txt'
    f_obj = open(save_path, 'wb') # wb 表示打开方式
    f_obj.write(respHtml)
    f_obj.close()
    #print "respHtml=",respHtml; # you should see the ouput html
    
    print "Method 1: Use python re to extract info from html";
    #<h1 class="h1user">crifan</h1>
    foundH1user = re.search('$[0-9]\d', respHtml);
    print "foundH1user=",foundH1user;
    if(foundH1user):
        h1user = foundH1user.group("h1user");
        print "h1user=",h1user;

print'success'


    
###############################################################################
if __name__=="__main__":
    main();
