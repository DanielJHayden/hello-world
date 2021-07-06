#!/usr/bin/env python
# coding: utf-8

# In[18]:


import os
import re
f = "C://Users/danie/google-python-exercises/babynames/baby1990.html"

def name_extractor(file):
    """
    
    """
    name_list = []
    match = (re.search(r'(\d+)\.html$', file))
    print (match.group(1))
    
name_extractor(f)
        


# In[133]:


import os
import re

def name_extractor(file):
    """
    Needs an html file of popular baby names from the social security administration
    Reutrns a list of names in alphabhetical order in the format 'name + popularity_ranking'
    list starts with year of census data
    """
    name_list = []
    rank_dict = {}
    year = re.search(r'(\d+)\.html$', file)
    current = open(file)
    
    match = re.findall(r'<tr\salign="right"><td>(\d+).*?>(\w+).*?>(\w+)', current.read())
    
    for one_touple in match:
        rank_dict[one_touple[1]] = one_touple[0]
        rank_dict[one_touple[2]] = one_touple[0]
    
    for one_item in rank_dict:
        ranking = rank_dict[one_item]
        name_list.append(f"{one_item} {ranking}")    
                     
    name_list = sorted(name_list)
    name_list.insert(0,year.group(1))
    current.close
    
    return name_list

def main(html_file):
    biglist = name_extractor(html_file)
    text = '\n'.join(biglist) + '\n'
    print (text[0-100])
    
            
f = "C://Users/danie/google-python-exercises/babynames/baby1990.html"
main(f)
        


# In[ ]:


import re
s = 'the Quick Brown Fox jumped over The Lazy dog'
re.serac


# In[118]:


testlist = [('1', 'Michael', 'Jessica'), ('2', 'Christopher', 'Ashley'), ('3', 'Matthew', 'Brittany'), ('4', 'Joshua', 'Amanda'), ('5', 'Daniel', 'Samantha'), ('6', 'David', 'Sarah'), ('7', 'Andrew', 'Stephanie'), ('8', 'James', 'Jennifer'), ('9', 'Justin', 'Elizabeth')]
mydict = {i[0]:(i[1],i[2]) for i in testlist}
mydict
help (testlist.insert)


# In[117]:





# In[ ]:





# In[ ]:


<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>

