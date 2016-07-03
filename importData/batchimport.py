#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'zhenghaitao'

import MySQLdb

db = MySQLdb.connect(host="url",user="dbuser", passwd="dbpwd",db="dbname",charset='utf8')

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print "Database version : %s " % data

db.close()
