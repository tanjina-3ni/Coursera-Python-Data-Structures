# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 00:43:28 2019

@author: Aspire
"""

fname = input("Enter file name: ")
fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()
    if not line.startswith('From:'): continue
    count = count+1
    words = line.split()
    print (words[1])
print("There were", count, "lines in the file with From as the first word")


