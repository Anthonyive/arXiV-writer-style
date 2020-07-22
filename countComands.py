# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 21:48:15 2020

@author: Yeyubei Zhang
"""
import re
import csv

#the fisrt row in csv
row_list=[["Title", "Author","#dcclass","line_dcclass","#package","line_package","#Macros","line_Macros","#newThem","line_newThem"]]


#input a sample  tex
with open ("sample.tex", "r") as myfile:
    data=myfile.read()

#read title and author
title=re.findall(r'\\title\{([^}]+)\}',data)
author=re.findall(r'\\author\{([^}]+)\}',data)

#read lines of the sample tex & counting &line numbers
with open ("sample.tex", "r") as myfile:
    data=myfile.readlines()

num_dcclass=0
linenum_dcclass=[]

num_usepackage=0
linenum_usepackage=[]

num_Macros=0
linenum_Macros=[]

num_newThm=0
linenum_newThm=[]
for i in range(0,len(data)):
    if len(re.findall(r'\\documentclass',data[i])) != 0:
        num_dcclass+=1
        linenum_dcclass.append(i+1)

    if len(re.findall(r'\\usepackage',data[i])) != 0:
        num_usepackage+=1
        linenum_usepackage.append(i+1)
        
    if len(re.findall(r'\\newcommand',data[i])) != 0:
        num_Macros+=1
        linenum_Macros.append(i+1)
        
    if len(re.findall(r'\\newtheorem',data[i])) != 0:
        num_newThm+=1
        linenum_newThm.append(i+1)

#append info of this sample to row list
row_list.append([title,author,num_dcclass,linenum_dcclass,num_usepackage,linenum_usepackage,num_Macros,linenum_Macros,num_newThm,linenum_newThm])      
#write to csv
with open('sample_info.csv', 'w', newline='') as of:
    writer = csv.writer(of)
    writer.writerows(row_list)



    






