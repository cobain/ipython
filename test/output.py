#! /usr/bin/env python
# coding:utf-8

# https://docs.python.org/2/library/pprint.html

import pprint

stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
stuff.insert(0, stuff[:])

print pprint.isreadable(stuff)
print pprint.saferepr(stuff)

pprint.pprint(stuff)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(stuff)

tup = ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead', ('parrot', ('fresh fruit',))))))))
pp = pprint.PrettyPrinter(depth=6)
pp.pprint(tup)

