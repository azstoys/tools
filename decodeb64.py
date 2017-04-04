#!/usr/bin/python
import base64
import sys

ostr = sys.argv[1]
dstr = base64.b64decode(ostr)
print dstr
