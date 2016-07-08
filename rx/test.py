__author__ = 'zhenghaitao'


# !/usr/bin/env python
# coding=utf-8
import sys
import urllib2
print sys.getdefaultencoding()

import rx
from rx import Observable, Observer

class MyObserver(Observer):
    def on_next(self, x):
        print("Got: %s" % x)

    def on_error(self, e):
        print("Got error: %s" % e)

    def on_completed(self):
        print("Sequence completed")

xs = Observable.from_iterable(range(10))
d = xs.subscribe(MyObserver())

xs = Observable.from_([1,2,3])
ys = xs * 4



req = urllib2.Request("http://www.baidu.com/")
fd = urllib2.urlopen(req)
print fd.headers['Content-Type']

xs = Observable.from_([1,2,3,4,5,6])
ys = xs.to_blocking()
zs = (x*x for x in ys if x > 3)
for x in zs:
    print(x)
