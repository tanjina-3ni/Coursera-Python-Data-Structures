# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 01:46:03 2019

@author: Aspire
"""
name = input("Enter file:")
handle = open(name)
lst = list()
counts = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From:'): continue
    words = line.split()
    lst.append(words[1])
for word in lst:
    counts[word] = counts.get(word,0)+1    

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword = word
        bigcount = count
print (bigword,bigcount)
    