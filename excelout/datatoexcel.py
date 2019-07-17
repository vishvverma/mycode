#!/usr/bin/env python3

## sudo apt install python3-pip

## python3 -m pip install pyexcel
## python3 -m pip install pyexcel-xls
import pyexcel

import json
import csv

f = open('astros.json')
data = json.load(f)
f.close()

f = csv.writer(open('file.csv', 'wb+'))
# use encode to convert non-ASCII characters
for item in data:
    values = [ x.encode('utf8') for x in item['fields'].values() ]
    f.writerow([item['people'], item['number'], item['message']] + values)
