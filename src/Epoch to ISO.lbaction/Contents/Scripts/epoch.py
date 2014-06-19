#!/usr/bin/env python

import datetime
import sys
import re
import json

items = []

item = {}
try:
    item['title'] = datetime.datetime.fromtimestamp(int(sys.argv[1])).isoformat()
except IndexError:
    pass
    
items.append(item)

print json.dumps(items)