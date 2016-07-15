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
print d

xs = Observable.from_([1,2,3,4,5,6])
ys = xs.to_blocking()
zs = (x*x for x in ys if x > 3)
for x in zs:
    print(x)

xs = Observable.from_([1,2,3,4,5,6])
ys = xs[1:-1]

xs = Observable.from_(range(10))
d = xs.subscribe(MyObserver())

#Filtering a sequence
xs = Observable.from_(range(10))
d = xs.filter(
        lambda x: x % 2
    ).subscribe(MyObserver())

#Transforming a sequence
xs = Observable.from_(range(10))
d = xs.map(
        lambda x: x * 2
    ).subscribe(MyObserver())

xs = Observable.from_(range(10, 20, 2))
d = xs.map(
        lambda x, i: "%s: %s" % (i, x * 2)
    ).subscribe(MyObserver())

#merge
xs = Observable.range(1, 5)
ys = Observable.from_("abcde")
zs = xs.merge(ys).subscribe(MyObserver())

#Subjects and Streams
from rx.subjects import Subject

stream = Subject()
stream.on_next(41)

d = stream.subscribe(MyObserver())
stream.on_next(42)
d.dispose()

stream.on_next(43)

