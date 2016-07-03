__author__ = 'htzheng'

# coding=utf8
# ! /usr/bin/env python


import urllib
import urllib2
import httplib
import json

import os
import sys
import json


def filterfiles(f):
    if os.path.isdir(f) and f.endswith('-html'):
        return True


dirs = os.listdir('.')
targetDirs = filter(filterfiles, dirs)
print targetDirs

itemList = list()

targetDocDirectory = 'HtmlData'
if os.path.isdir(targetDocDirectory) and os.path.exists(targetDocDirectory):
    pass
else:
    os.mkdir(targetDocDirectory);

for htmlDir in targetDirs:
    files = os.listdir(htmlDir)
    for f in files:
        filename = f.split('.')[0]
        if filename.startswith('_'):
            filename = filename.replace('_', ':', 1)
        node = dict()
        node['name'] = filename
        node['source'] = htmlDir.split('-')[0]
        itemList.append(node)
        # copy and rename for new doc
        destPath = targetDocDirectory + '/' + node['source'] + '-' + f
        sourcePath = htmlDir + '/' + f
        sourcePath = sourcePath.encode("utf-8")
        destPath = destPath.encode("utf-8")
        print "source -> " + sourcePath
        print "dest -> " + destPath
        file(destPath, 'w').write(open(sourcePath, 'r').read())
jsonStr = dict()
jsonStr["resultCode"] = 1
jsonStr["data"] = itemList
json.dump(jsonStr, file("test.json", 'w'))
