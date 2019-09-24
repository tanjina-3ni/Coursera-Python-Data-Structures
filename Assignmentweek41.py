# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 23:51:16 2019

@author: Aspire
"""

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
res = list()
for line in fh:
    l = line.rstrip()
    lst = lst + l.split()

for word in lst:
    if word in res: continue
    res.append(word)
    res.sort()

print (res)