# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 15:39:20 2020

@author: Chan234
"""

import json
import os 

def parsethru(folder):
    directory=f"C:\\Users\\Chan234\\Documents\\Personal Research\\Incels\\Scraping\\{folder}\\"
    
    for filename in os.listdir(directory):
        print (filename)
        f = open(directory+filename)
        lines = f.read()
        post_dict=json.loads(lines)
        continue   
parsethru('hapacels')  


#sentiment analysis comparing incelswithouthate to incelexit
#word counts

#100 posts from each of the 10 incel subreddits
#word counts, look for overlap

words={}

#downloading comment and post history of a specific user?

# ricecels
# hapacels 
# IncelExit
# inceltears
# IncelswithoutHate
# IncelsInAction
# TruFemCels
# AskTruFemCels

#8 folders, each with a bunch of text files.
#iterate thru a folder
#post titles
#post bodies
#comments
