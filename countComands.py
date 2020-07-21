# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 21:48:15 2020

@author: Yeyubei Zhang
"""
import re

with open ("sample.tex", "r") as myfile:
    data=myfile.read()

title=re.findall(r'\\title\{([^}]+)\}',data)
print(title)

author=re.findall(r'\\author\{([^}]+)\}',data)
print(author)

with open ("sample.tex", "r") as myfile:
    data=myfile.readlines()

num_dcclass=0
linenum_dcclass=[]
for i in range(0,len(data)):
    if len(re.findall(r'\\documentclass',data[i])) != 0:
        num_dcclass+=1
        linenum_dcclass.append(i+1)


num_usepackage=0
linenum_usepackage=[]
for i in range(0,len(data)):
    if len(re.findall(r'\\usepackage',data[i])) != 0:
        num_usepackage+=1
        linenum_usepackage.append(i+1)
  



