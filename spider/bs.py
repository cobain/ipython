#!/usr/bin/python
# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup

import urllib2
import http.cookiejar
import re
import urllib
import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from multiprocessing import Process
from multiprocessing import Queue
import os
import json
import socket

def makeMyOpener(head = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}):
    cj = http.cookiejar.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

def handleUrl(url):
    html_doc = urllib.urlopen(url)
    soup = BeautifulSoup(html_doc)

    alist = soup.findAll('a')
    for link in alist:
        if link.get('class') == 'collection-link':
            name = link.findAll('h3')
            name__text = name[0].text
            print "community name: " + name__text
            dirname = name__text.replace(' ', '_')
            os.mkdir(dirname)
            detailUrl = link.get('href')
            print detailUrl
            detailContent = urllib.urlopen(detailUrl)
            detailSoup = BeautifulSoup(detailContent)
            uls = detailSoup.findAll('ul')
            for ul in uls:
                if ul.get('class') == 'community-details':
                    lis = ul.findAll('li')
                    address = lis[2].text
                    address = address.replace("&nbsp;", " ")
                    county = lis[3].text
                    district = lis[4].text
                    print address
                    print county
                    print district
                    f = open(dirname + '/' + 'address.txt', 'w')
                    f.write(address + '\n')
                    f.write(county + '\n')
                    f.write(district + '\n')
                    f.close()
                    break
            parseHomeDesign(detailUrl, dirname)
            parseGallery(detailUrl, dirname)


def parseHomeDesign(baseUrl, dirname):
    url = baseUrl + "#homedesigns"
    print "homedesign: " + url

    browser1 = webdriver.Chrome()
    browser1.get(url)
    WebDriverWait(browser1, 7).until(EC.presence_of_element_located((By.CLASS_NAME, 'js-home-multiview-toggle')))
    print "Page is ready!"

    homeDesign = browser1.page_source
    soup = BeautifulSoup(homeDesign)
    divs = soup.findAll('div')

    f = open(dirname + '/' + 'homedesign.txt', 'w')
    for div in divs:
        if div.get('class') == 'single-model group':
            f.write('----------------------------------' + '\n')
            divchilds = div.findAll('div')
            for child in divchilds:
                if child.get('class') == 'model-name':
                    print child.text
                    f.write(child.text + '\n')
                    break

            uls = div.findAll('ul')
            lis = uls[0].findAll('li')
            for li in lis:
                print li.text
                f.write(li.text + '\n')
            f.write('----------------------------------' + '\n')

    f.close()
    browser1.quit()


def parseGallery(baseUrl, dirname):
    url = baseUrl + "#gallery"

    oper = makeMyOpener()
    uop = oper.open(url,
                    timeout=1000)
    data = uop.read()

    p = re.compile(r'<div class="comm-slide-image-holder\s?.*">(.*\n.*\n.*\n.*)</div>')
    img = re.compile(r'<img data-src="(.*?)" alt=.*')
    photo = p.findall(data)
    for p in photo:
        imageobj = p.strip()
        # print imageobj
        i = img.search(imageobj)
        imageUrl = i.group(1)
        print imageUrl
        print "downloading..."
        urllib.urlretrieve(imageUrl, dirname + '/' + os.path.basename(imageUrl))


if __name__ == "__main__":
    creek = "https://www.tollbrothers.com/luxury-homes-for-sale/California/Alamo-Creek"
    handleUrl(creek)