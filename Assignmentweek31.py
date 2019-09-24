# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 19:04:32 2019

@author: Aspire
"""

#7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.

fname = input("Enter file name: ")
fh = open(fname)
 
for line in fh: 
    l = line.rstrip()
    print(l.upper())
        
