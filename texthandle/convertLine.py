#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

f = open('xxx.csv')
content = f.read()

f.close()

new_content = re.sub(r'\n', r'\r\n', content)

new_file = open('xxx_windows.txt', 'w')
new_file.write(new_content)
new_file.flush()
new_file.close()
