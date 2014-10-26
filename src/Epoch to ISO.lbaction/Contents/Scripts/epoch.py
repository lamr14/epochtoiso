#!/usr/bin/env python

import datetime
import sys
import re
import json

items = []

item = {}

def isoformat(matchobj):
    if matchobj.group(0):
        timestamp = matchobj.group(0)
        try:
            return datetime.datetime.fromtimestamp(int(timestamp)).isoformat()
        except IndexError:
            return timestamp
        except ValueError:
            return timestamp
    
    return timestamp

item = {"title": re.sub('\d{8}', isoformat, sys.argv[1])}

items.append(item)

print json.dumps(items)