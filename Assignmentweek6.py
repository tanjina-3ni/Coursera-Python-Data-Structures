# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 15:37:07 2019

@author: Aspire
"""

name = input("Enter file:")
handle = open(name)
t = list()
d = dict()
for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
		words = line.split()
		time = words[5]
		hour = time[0:2]
		d[hour] = d.get(hour,0) +1

t = d.items()
t.sort()
for key, val in t:
    print (key, val)