#coding=utf8
#! /usr/bin/env python

#
# you can refer to this link below for more details about ElementTree
#http://www.python.org/doc//current/library/xml.etree.elementtree.html

import urllib
from xml.etree import ElementTree
import os.path

urlfomat = "http://tar1.telenav.com:8080/repository/telenav/client/trunk/NavigationSDK/NavigationSDK-android-%s-trunk.xml"
versionMap = {}
navsdk_ver = ""

def retrieveXMLFromTar(version):
    url = urlfomat % (version)
    print "retrieving the ivy xml: " + url
    page = urllib.urlopen(url)
#     print "status", page.getcode()
#     print "url:", page.geturl()
#     print "head_info:\n", page.info()
    
    xmlData = page.read()
    filename = os.path.basename(url)
    f = open(filename, 'w')
    f.write(xmlData)
    f.close()
    
    return xmlData

#for offline testing
def readLocal():
    f = open('NavigationSDK-android-2.1.2.100899-trunk.xml')
    data = f.read()
    #print data
    return data
    pass

def buildVersionMap(xmlData):
    per = ElementTree.fromstring(xmlData)
    dependencies = per.findall('./dependencies/dependency')
    #build name -> rev map
    if dependencies is not None:
        for dependency in dependencies:
            versionMap[dependency.attrib['name']] = dependency.attrib['rev']
    print versionMap

def upgrade(ivyFile):
    #read old ivy file        
    oldivy = ElementTree.ElementTree()
    oldivy.parse(ivyFile)
    
    oldDepends = oldivy.find('./dependencies')
    headpointer = oldDepends.iter("dependency")
    for item in headpointer:
        print item.attrib
        componentName = item.attrib['name']
        #componentRev = item.attrib['rev']
        
        if componentName in versionMap.keys():
            item.attrib['rev'] = versionMap[componentName]
        elif componentName == "NavigationSDK":
            item.attrib['rev'] = navsdk_ver
    
    oldivy.write(ivyFile, "utf-8")
    ElementTree.dump(oldivy)
    
if __name__ == "__main__":
    
    navsdk_ver = raw_input("please input the navsdk version: ")
    if len(navsdk_ver) <= 0:
        print "invalid input"
        exit(0)

    xmlData = retrieveXMLFromTar(navsdk_ver) #retrieve the latest xml files
    buildVersionMap(xmlData)  # build version map according to the latest ivy file     
    upgrade("ivy.xml") #update ivy xml under root directory
    #upgrade("./apps/ivy-android.xml") #update ivy-android xml under apps directory
    
    print "update finished"
 
    