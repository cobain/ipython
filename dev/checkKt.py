#coding=utf8
#! /usr/bin/env python

import httplib
import re
import socket
import urllib

timeout = 60
socket.setdefaulttimeout(timeout)


def getTable():

    f = open('kvpage.html')
    page = f.readlines()
    f.close()
    pattern = re.compile(r'.*<tbody>(.*?)</tbody>.*')
    
    for line in page:
        #print line
        m = pattern.match(line.strip())
        if m is not None:
            return m.group(1)
    
    return None

def extractKvEvents(content):
    
    #init result
    table = []
    
    #init pattern
    patternTR = re.compile(r"<tr>(.*?)</tr>")
    patternTD = re.compile(r'<td class="confluenceTd">(.*?)</td>')
    
    #search all the rows
    allrows = patternTR.findall(content)
    if allrows is not None:
        for row in allrows:
            #print row
            cols = patternTD.findall(row)
            if cols is not None:
                
                table.append(cols)
            
    return table

def outputToExcel(table):
    for row in table:
        print row

def loginWiki():

    httpClient = None
    try:
        params = urllib.urlencode({'os_username': 'xxxx@xxx.com',
                                   'os_password': 'xxxx', 
                                   'login': 'Log In'})
        
        headers = {"Content-type": "application/x-www-form-urlencoded"
                        , "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
    
        httpClient = httplib.HTTPConnection("xxx.com", 8080, timeout=30)
        httpClient.request("POST", "/login.action", params, headers)
    
        response = httpClient.getresponse()
#         print response.status
#         print response.reason
#         print response.read()
#         print response.getheaders()
        print response.getheader('Set-Cookie')
        cookieFile = open('cookie.txt', 'w')
        cookieFile.write(response.getheader('Set-Cookie'))
        cookieFile.close()
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()

def catchPage():
    httpClient = None

    try:
        #read cookie
        f = open('cookie.txt')
        cookie = f.read().strip()
        print cookie
        f.close()
        
        #init headers
        headers = {"Content-type": "application/x-www-form-urlencoded",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                    'Cookie': cookie}
    
        #send request
        httpClient = httplib.HTTPConnection('xxx.com', 8080, timeout=30)
        httpClient.request('GET', '/xxxPath', headers=headers)
    
        #response是HTTPResponse对象
        response = httpClient.getresponse()
        print response.status
        print response.reason
        
        htmlPage = open('kvpage.html', 'w')
        htmlPage.write(response.read())
        htmlPage.close()
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()

if __name__ == '__main__':

    loginWiki()
    catchPage()
    tablecontent = getTable()
    table = extractKvEvents(tablecontent) 
    outputToExcel(table)
 
    
