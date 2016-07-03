#! /usr/bin/env python

line = 'aaa\nbbb\nccc\n'
print line.split('\n')
print line.splitlines()

str = 'xxxSPAMxxx'
print str.find('SPAM')

str = 'xxaaxxaa'
print str.replace('aa', 'SPAM')

str = '\t    Ni\n'
print str.strip()

str = 'SHRUBBERY'
print str.lower()

print str.isalpha()
print str.isdigit()

import string
print string.lowercase


import sys
print sys.platform, sys.maxint, sys.version
print sys.path

print sys.modules

print sys.modules.keys()

import traceback, sys
def grail(x):
    raise TypeError, 'already got one'

try:
    grail('arthur')
except:
    exc_info = sys.exc_info()
    print exc_info[0]
    print exc_info[1]
    traceback.print_tb(exc_info[2])


# import os
# os.startfile("more.py")
# print "string test"

# read numbers till eof and show squares

                                 # when run, not imported
