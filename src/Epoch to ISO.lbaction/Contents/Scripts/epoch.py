#!/usr/bin/env python

import datetime
import sys
import re
import json

items = []

item = {}

def isoformat(matchobj):
    if matchobj.group(2):
        timestamp = matchobj.group(2)
        pre = matchobj.group(1)
        post = matchobj.group(3)
        try:
            return pre + datetime.datetime.fromtimestamp(int(timestamp)).isoformat() + post
        except IndexError:
            return matchobj.group(0)
        except ValueError:
            return matchobj.group(0)
    
    return matchobj.group(0)

item = {"title": re.sub('(\D?)(\d{10})(\D)', isoformat, sys.argv[1])}

items.append(item)

print json.dumps(items)