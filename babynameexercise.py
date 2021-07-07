#!/usr/bin/env python
# coding: utf-8

# In[10]:


def name_extractor(file):
    """
    Needs an html file of popular baby names from the social security administration
    Reutrns a list of names in alphabhetical order in the format 'name + popularity_ranking'
    list starts with year of census data
    """
    
    import os
    import re
    
    name_list = []
    rank_dict = {}
    
    year = re.search(r'(\d+)\.html$', file)    
    current = open(file)    
    match = re.findall(r'<tr\salign="right"><td>(\d+).*?>(\w+).*?>(\w+)', current.read())
    current.close

    
    for one_touple in match:                                #Check for existing match, only accept lower rank value into dictionary
        
        for index in range(1,2):
            
            if one_touple[index] in rank_dict:
                if rank_dict[one_touple[index]] < one_touple[0]:
                    continue
            rank_dict[one_touple[index]] = one_touple[0]
    
    for one_item in rank_dict:
        
        ranking = rank_dict[one_item]            #Build target list from dictionary formatted as "Name rank"
        name_list.append(f"{one_item} {ranking}")    
                     
    name_list = sorted(name_list)
    name_list.insert(0,year.group(1))
    
    return name_list

def main(html_file):
    """
    Prints the list that name_extractor produces with newline characters to make it more readable.
    Requires: html file name and path
    """
    
    biglist = name_extractor(html_file)
    text = '\n'.join(biglist)
    print (text)
    
            
f = "C://Users/danie/google-python-exercises/babynames/baby1990.html"
main(f)
        

