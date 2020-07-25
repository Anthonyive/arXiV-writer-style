#!/usr/bin/env python
# coding: utf-8

# In[18]:


import re
import pandas as pd

# input a sample  tex
greeks_list=["\alpha","\beta","\gamma","\Gamma","\delta","\Delta","\epsilon","\varepsilon",
             "\zeta","\eta","\theta","\vartheta","\Theta","\iota","\kappa","\lambda","\Lambda",
             "\mu","\nu","\pi","\Pi","\rho","\varrho","\sigma","\Sigma","\tau","\phi","\varphi","\Phi",
             "\chi","\psi","\Psi","\omega","\Omega"]

with open('sample.tex', 'r') as myfile:
    matches={'line num':[],'Command':[]}
    i = 0
    matches_df = pd.DataFrame(matches)
    

    for line in myfile:

        match = re.findall(r'\\\w+', line)
        
        if '\\end' in match:
            match = []

        if '\\begin' in match:
            match = [re.findall('(?!\\begin{)\w+', line)[1]]
        
        for g in greeks_list:
            match[:]=[x for x in match if x != g]

        for j in match:
            new_row = {'line num': i+1 , 'Command': [j]}
            matches_df=matches_df.append(new_row, ignore_index=True)

        i += 1
print(matches_df)


# In[ ]:




