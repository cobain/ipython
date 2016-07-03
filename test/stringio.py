#! /usr/bin/env python

# https://docs.python.org/2/library/stringio.html
from StringIO import StringIO
import sys

buff = StringIO()

temp = sys.stdout
sys.stdout = buff

print 42, 'spam', 3.141
sys.stdout = temp

print buff.getvalue()

import sys
print >> sys.stderr, 'spam' * 2

import StringIO

output = StringIO.StringIO()
output.write('First line.\n')
print >> output, 'Second line.'

# Retrieve file contents -- this will be
# 'First line.\nSecond line.\n'
contents = output.getvalue()

# Close object and discard memory buffer --
# .getvalue() will now raise an exception.
output.close()

print contents


import cStringIO

output = cStringIO.StringIO()
output.write('First line.\n')
print >>output, 'Second line.'

# Retrieve file contents -- this will be
# 'First line.\nSecond line.\n'
contents = output.getvalue()

# Close object and discard memory buffer --
# .getvalue() will now raise an exception.
output.close()

print contents

