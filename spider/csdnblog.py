import time
import urllib
import urllib2

url = 'http://pdfmergefree.com'
#url = 'http://blog.csdn.net/zhtsuc/article/details/54577773'

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'name': 'cobain',
          'location': 'SDU',
          'language': 'cn'}

headers = {'User-Agent': user_agent}
data = urllib.urlencode(values)
req = urllib2.Request(url, None, headers)
cnt = 1
while cnt <= 10000:
    response = urllib2.urlopen(req)
    print cnt
    cnt += 1
    time.sleep(1.0)