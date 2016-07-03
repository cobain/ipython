#coding=utf8
#! /usr/bin/env python

import httplib
import re
import socket
import urllib

timeout = 60
socket.setdefaulttimeout(timeout)


def test():

    httpClient = None
    try:
        params = "{\"emo_type\":2, \"emo_id\":1,\"tags\":[\"呵呵\",\"哈哈\"]}"
        
#         headers = {"Content-type": "application/json; charset=utf-8"
#                         , "Accept": "application/json; charset=utf-8"}
    
        httpClient = httplib.HTTPConnection("182.92.80.22", 8000, timeout=30)
        httpClient.request("POST", "/anotate_emo/", params, null)
    
        response = httpClient.getresponse()
        print response.status
        print response.reason
        print response.getheaders()
        print response.read()

    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()


if __name__ == '__main__':
    test()
    
