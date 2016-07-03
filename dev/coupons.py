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
        params = json.dumps({                                      
   "eMailAddress"     : "INFO@UATMOBILEDEMO.COM",
   "password"         : "m081Led3m0uat"})
        
        headers = {"content-type": "application/json; charset=UTF-8"
                        , "accept": "application/json",
                        "user-agent": "Apache-HttpClient/4.2 (java 1.5)"}
    
        httpClient = httplib.HTTPConnection("uat.api.entertainment.com", timeout=60)
        httpClient.request("POST", "https://uat.api.entertainment.com/mobile-rs-2.2.0/resources/accounts/partnerlogin", params, headers)
    
        response = httpClient.getresponse()
        print response.status
        print response.reason
        print response.read()
        print response.getheaders()
        print response.read()
       
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()

def getoffers():

    httpClient = None
    try:
        params = json.dumps({
                               "sortBy" : "DISTANCE",
                               "searchRadius" : 1,
                               "redemptionTypes" : ["MOBILE"],
                               "startRecIndex" : "0",
                               "limitPerPage" : "50",
                               "searchLocation" : {
                                     "latitude" : 42.5408,
                                     "longitude" : -83.2063
                               },
                               "category" : {
                                    "groupName" : "Category",
                                    "name" : "Dining",
                                    "id" : 25,
                                    "offerCount" : 0
                               },
                               "keywordSearch" : "",
                               "includeCategories" : "false",
                               "theToken" : "xp9v5KE7ArUkUcuA7XaTT6HWjwre92135L+tgCy1nZCGmplEAojcIKoHeKt4yD++77NEyIz48O/rl+epKP/BFOSLAtgFclvUKumdILV5WcA=",
                               "editionIds" : ["PR000000008A"]})
        
        headers = {"content-type": "application/json; charset=UTF-8",
                   "accept": "application/json",
                   "user-agent": "Apache-HttpClient/4.2 (java 1.5)",
                   "CLIENTIP":"216.111.89.3"}
    
        httpClient = httplib.HTTPConnection("uat.api.entertainment.com", timeout=60)
        httpClient.request("POST", "https://uat.api.entertainment.com/mobile-rs-2.2.0/resources/offers/merchantoffers", params, headers)
    
        response = httpClient.getresponse()
        print response.status
        print response.reason
        print response.read()
        print response.getheaders()
        print response.read()
       
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
    
        #response��HTTPResponse����
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

import json
import urllib2
def curl_keystone():
    url = 'https://uat.api.entertainment.com/mobile-rs-2.2.0/resources/accounts/partnerlogin'
    values = {"eMailAddress":"INFO@UATMOBILEDEMO.COM","password":"m081Led3m0uat"}
    params = json.dumps(values)
    headers = {"content-type":"application/json;charset=UTF-8","accept": "application/json", "user-agent": "Apache-HttpClient/4.2 (java 1.5)"}
    req = urllib2.Request(url, params, headers)
    response = urllib2.urlopen(req)
    print response.read()

# xp9v5KE7ArUkUcuA7XaTT6HWjwre92135L+tgCy1nZCGmplEAojcIKoHeKt4yD++77NEyIz48O/rl+epKP/BFOSLAtgFclvUKumdILV5WcA=

def getoffer():
    url = 'https://uat.api.entertainment.com/mobile-rs-2.2.0/resources/offers/merchantoffers'
    values = {
   "sortBy" : "DISTANCE",
   "searchRadius" : 5,
   "redemptionTypes" : ["MOBILE"],
   "startRecIndex" : "0",
   "limitPerPage" : "50",
   "searchLocation" : {
         "latitude" : 42.5408,
         "longitude" : -83.2063
   },
   "category" : {
             "groupName" : "Category",
             "name" : "Shopping",
             "id" : 27,
             "offerCount" : 0
             },
   "keywordSearch" : "",
   "merchantDBAName" : "Jax Kar Wash",
   "includeCategories" : "false",
   "theToken" : "xp9v5KE7ArUkUcuA7XaTT6HWjwre92135L+tgCy1nZCGmplEAojcIKoHeKt4yD++77NEyIz48O/rl+epKP/BFOSLAtgFclvUKumdILV5WcA=",
   "editionIds" : ["PR000000008A"]}

    params = json.dumps(values)
    print params
    headers = {"content-type":"application/json;charset=UTF-8","accept": "application/json", "user-agent": "Apache-HttpClient/4.2 (java 1.5)","CLIENTIP":"216.111.89.3"}
    req = urllib2.Request(url, params, headers)
    response = urllib2.urlopen(req)
    print response.read()
    
def getMechant():
    url = 'https://uat.api.entertainment.com/mobile-rs-2.2.0/resources/offers/merchants'
    values = {
             "theToken" : "xp9v5KE7ArUkUcuA7XaTT6HWjwre92135L+tgCy1nZCGmplEAojcIKoHeKt4yD++77NEyIz48O/rl+epKP/BFOSLAtgFclvUKumdILV5WcA=",
             "editionIds" : ["PR000000008A"],
             "searchLocation" : {
             "latitude" : 42.5408,
             "longitude" : -83.2063
             },
             "category" : {
             "groupName" : "Category",
             "name" : "Shopping",
             "id" : 27,
             "offerCount" : 0
             },
             "redemptionTypes" : ["MOBILE"],
             "keywordSearch" : "",
             "searchRadius" : 5,
             "includeCategories" : "false",
             "startRecIndex" : 0,
             "limitPerPage" : 20,
             "sortBy" : "DISTANCE",
             }


    params = json.dumps(values)
    print params
    headers = {"content-type":"application/json;charset=UTF-8","accept": "application/json", "user-agent": "Apache-HttpClient/4.2 (java 1.5)","CLIENTIP":"216.111.89.3"}
    req = urllib2.Request(url, params, headers)
    response = urllib2.urlopen(req)
    print response.read()

def getMechants2():

    httpClient = None
    try:
        params = json.dumps({
             "theToken" : "xp9v5KE7ArUkUcuA7XaTT6HWjwre92135L+tgCy1nZCGmplEAojcIKoHeKt4yD++77NEyIz48O/rl+epKP/BFOSLAtgFclvUKumdILV5WcA=",
             "editionIds" : ["PR000000008A"],
             "searchLocation" : {
             "latitude" : 42.5408,
             "longitude" : -83.2063
             },
             "category" : {
             "groupName" : "Category",
             "name" : "Shopping",
             "id" : 27,
             "offerCount" : 0
             },
             "redemptionTypes" : ["MOBILE"],
             "keywordSearch" : "",
             "searchRadius" : 5,
             "includeCategories" : "false",
             "startRecIndex" : 0,
             "limitPerPage" : 20,
             "sortBy" : "DISTANCE",
             })
        
        headers = {"content-type": "application/json; charset=UTF-8",
                   "accept": "application/json",
                   "user-agent": "Apache-HttpClient/4.2 (java 1.5)",
                   "CLIENTIP":"216.111.89.3"}
    
        httpClient = httplib.HTTPConnection("uat.api.entertainment.com", timeout=60)
        httpClient.request("POST", "https://uat.api.entertainment.com/mobile-rs-2.2.0/resources/offers/merchants", params, headers)
    
        response = httpClient.getresponse()
        print response.status
        print response.reason
        print response.read()
        print response.getheaders()
        print response.read()
       
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()

if __name__ == '__main__':

    getoffer()
     
#     catchPage()
#     tablecontent = getTable()
#     table = extractKvEvents(tablecontent) 
#     outputToExcel(table)
