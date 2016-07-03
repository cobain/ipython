import urllib2
import http.cookiejar
import re
import urllib
import os
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

oper = makeMyOpener()
uop = oper.open('https://www.tollbrothers.com/luxury-homes-for-sale/California/Ashbury-at-Alamo-Creek#gallery', timeout = 1000)
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
    urllib.urlretrieve(imageUrl, os.path.basename(imageUrl))