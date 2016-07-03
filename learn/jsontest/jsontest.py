#coding=utf8
#! /usr/bin/env python

import simplejson
obj = simplejson.dumps(['foo', {'bar':('baz', None, 1.0, 2)}])
print obj

print simplejson.dumps("\"foo\bar")
print simplejson.dumps(u'\u1234')
print simplejson.dumps('\\')
print simplejson.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)

from simplejson.compat import StringIO
io = StringIO()
simplejson.dump(['streaming API'], io)

print io.getvalue()

print(simplejson.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4 * ' '))

obj = [u'foo', {u'bar': [u'baz', None, 1.0, 2]}]

print simplejson.loads('["foo", {"bar":["baz", null, 1.0, 2]}]') == obj
print simplejson.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')[0]

print simplejson.loads('"\\"foo\\bar"') == u'"foo\x08ar'

print u'"foo\x08ar'
print simplejson.loads('"\\"foo\\bar"')

io = StringIO('["streaming API"]')
print simplejson.load(io)[0] == 'streaming API'

from decimal import Decimal

print simplejson.loads('1.1', use_decimal=True) == Decimal('1.1')

print simplejson.loads('1.1', use_decimal=True)
print Decimal('1.1')
print simplejson.dumps(Decimal('1.1'), use_decimal=True) == '1.1'
