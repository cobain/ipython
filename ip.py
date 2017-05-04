# -*- coding: utf-8 -*-
import requests

# url = 'http://219.245.192.20:8080/portal/templatePage/20150510020658403/login_custom.jsp?userip=10.248.240.137'
#
#
# cook = {'Cookies':'hello1=2014012017; hello2=true; hello3=%CE%CE%CD%CE%C6%CE; hello4=; hello5=; i_p_c_un=2014012017; i_p_pl=JTdCJTIyZXJyb3JOdW1iZXIlMjIlM0ElMjIxJTIyJTJDJTIybmV4dFVybCUyMiUzQSUyMmh0dHAlM0ElMkYlMkYyMTkuMjQ1LjE5Mi4yMCUzQTgwODAlMkZwb3J0YWwlMkZ0ZW1wbGF0ZVBhZ2UlMkYyMDE1MDUxMDAyMDY1ODQwMyUyRmxvZ2luX2N1c3RvbS5qc3AlMjIlMkMlMjJxdWlja0F1dGglMjIlM0FmYWxzZSUyQyUyMmNsaWVudExhbmd1YWdlJTIyJTNBJTIyQ2hpbmVzZSUyMiUyQyUyMnNlcnZpY2VUeXBlRGVzQXJyYXklMjIlM0ElNUIlMjJwb3J0YWwlMjBsYWIlMjBhdXRoJTIyJTVEJTJDJTIyc2VydmljZVR5cGVWYWx1ZUFycmF5JTIyJTNBJTVCJTIycG9ydGFsJTIyJTVEJTJDJTIyYXNzaWduSXBUeXBlJTIyJTNBMCUyQyUyMmlOb2RlUHdkTmVlZEVuY3J5cHQlMjIlM0ExJTJDJTIyd2xhbm5hc2lkJTIyJTNBJTIyJTIyJTJDJTIybmFzSXAlMjIlM0ElMjIlMjIlMkMlMjJieW9kU2VydmVySXAlMjIlM0ElMjIyMTkuMjQ1LjE5Mi4yMCUyMiUyQyUyMmJ5b2RTZXJ2ZXJJcHY2JTIyJTNBJTIyMDAwMCUzQTAwMDAlM0EwMDAwJTNBMDAwMCUzQTAwMDAlM0EwMDAwJTNBMDAwMCUzQTAwMDAlMjIlMkMlMjJieW9kU2VydmVySHR0cFBvcnQlMjIlM0ElMjI4MDgwJTIyJTJDJTIyaWZUcnlVc2VQb3B1cFdpbmRvdyUyMiUzQWZhbHNlJTJDJTIydWFtSW5pdEN1c3RvbSUyMiUzQSUyMjElMjIlMkMlMjJjdXN0b21DZmclMjIlM0ElMjJNVEEzJTIyJTJDJTIydXNlckdyb3VwSWQlMjIlM0ElMjJNQSUyMiUyQyUyMmd1ZXN0TWFuYWdlcklkJTIyJTNBJTIyTUElMjIlMkMlMjJyZWdDb2RlVHlwZSUyMiUzQSUyMk1BJTIyJTdE'}
# html = requests.get(url,cookies = cook).content
# print html


# req = urllib2.Request("http://www.baidu.com/")
# fd = urllib2.urlopen(req)
# print fd.headers['Content-Type']
from urllib import urlencode




import redis
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)
r = redis.StrictRedis(connection_pool = pool)

r.zadd('cobain', 1, 'value1')
r.zadd('cobain', 2, 'value2')
r.zadd('cobain', 4, 'value4')
r.zadd('cobain', 3, 'value3')

print r.zrange('cobain', 0, -1, withscores=True)

print r.zrank('cobain', 'value1')

r.lpush('llll', 'cobain1')
r.lpush('llll', 'cobain2')
r.ltrim('llll', 0, 5)
print r.lrange('llll', 0, 99)