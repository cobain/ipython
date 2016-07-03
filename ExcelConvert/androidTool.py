__author__ = 'htzheng'

# coding:utf-8

import urllib
import urllib2
import httplib
import json

import os
import sys
import json

dict = {'48':'mdpi',
        '72':'hdpi',
        '96':'xhdpi',
        '144':'xxhdpi'
        }

for key in dict.keys():
        path = 'res/old/' + key + '_' + key + '.png'
        destDir = 'res/new/drawable-' + dict[key]
        if (os.path.exists(destDir) is False):
                os.mkdir(destDir)
        file(destDir + '/icon_app.png', 'w').write(open(path, 'r').read())




