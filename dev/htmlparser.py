import urllib2
from jparser import PageModel


html = urllib2.urlopen("http://news.sohu.com/20170512/n492734045.shtml").read().decode('gb18030')
pm = PageModel(html)
result = pm.extract()

print "==title=="
print result['title']
print "==content=="
for x in result['content']:
    if x['type'] == 'text':
        print x['data']
    if x['type'] == 'image':
        print "[IMAGE]", x['data']['src']