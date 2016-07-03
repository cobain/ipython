#! /usr/bin/env python
#coding:utf-8

import codecs

print codecs.encode(u"我是谁", 'utf8')
print codecs.decode("我是谁", 'utf8')