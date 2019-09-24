# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 18:29:30 2019

@author: Aspire
"""

fname = input("Enter file name: ")
fh = open(fname)
s = 0
c = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find("0")
    n = float(line[pos:])
    c= c + 1
    s = s + n
    avg = s/c
print ("Average spam confidence:", avg)

