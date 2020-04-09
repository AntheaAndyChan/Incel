# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 15:39:20 2020

@author: Chan234
"""

import json
import os 
#import pdb

def parsethru(folder):
    directory=f"C:\\Users\\Chan234\\Documents\\Personal Research\\Incels\\Scraping\\{folder}\\"
    titles=[]
    bodies=[]
    comments=[]
    for filename in os.listdir(directory):
        #print (filename)
        f = open(directory+filename,"r")
        lines = f.read()
        #print(lines)
        post_dict=json.loads(lines)
        
        #append Post Title to titles (1 per post)
        #titles = [post['Post Title'] for post in post_dict]
        titles.append(str(post_dict['Post Title']))
        #print(post_dict['Post Title'])
        
        #append Post Bodies to bodies (1 per post)
        #bodies = [post['Post Body'] for post in post_dict]
        bodies.append(str(post_dict['Post Body']))
        #print(post_dict['Post Body'])
        
        #append Post Comment to comments (many per post)
        for comment in post_dict['Comments']:
            comments.append(str(comment['Comment Body']))
        #comments.append([post['Comments'] for post in post_dict])
            
    return titles, bodies, comments
    
    
titles, bodies, comments = parsethru('hapacels')  
print("Titles: ", titles, "\n") 
print("Bodies: ", bodies, "\n") 
print("Comments: ",comments, "\n")


#sentiment analysis comparing incelswithouthate to incelexit
#word counts

#100 posts from each of the 10 incel subreddits
#word counts, look for overlap




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
