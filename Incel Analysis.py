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
        f = open(directory+filename,"r")
        lines = f.read()
        post_dict=json.loads(lines)
        
        titles.append(str(post_dict['Post Title']))
        bodies.append(str(post_dict['Post Body']))
        
        for comment in post_dict['Comments']:
            comments.append(str(comment['Comment Body']))
    return titles, bodies, comments
    

subreddits= ['ricecels','hapacels','IncelExit','inceltears','IncelswithoutHate','IncelsInAction','TruFemCels','AskTruFemCels']
title_dict={}
bodies_dict={}
comments_dict={}
for subreddit in subreddits:
    titles, bodies, comments = parsethru(subreddit)  
    title_dict[subreddit]= titles
    bodies_dict[subreddit]= bodies
    comments_dict[subreddit]= comments
 
print(title_dict)
print(bodies_dict)
print(comments_dict)
# # Apply a first round of text cleaning techniques
# import re
# import string

# def clean_text_round1(text):
#     '''Make text lowercase, remove text in square brackets, remove punctuation and remove words containing numbers.'''
#     text = text.lower()
#     #text = re.sub('\[.*?\]', '', text)
#     text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
#     text = re.sub('\w*\d\w*', '', text)
#     text = re.sub('[‘’“”…]', '', text)
#     text = re.sub('\n', ' ', text)
#     return text

# # round1 = lambda x: clean_text_round1(x)
# # data_clean = pd.DataFrame(data_df.transcript.apply(round1))
# # data_clean
# for value in dict:
#     data_clean=clean_text_round1(value)

# #the count
# from sklearn.feature_extraction.text import CountVectorizer

# cv = CountVectorizer(stop_words='english')
# data_cv = cv.fit_transform(data_clean.transcript)
# data_dtm = pd.DataFrame(data_cv.toarray(), columns=cv.get_feature_names())
# data_dtm.index = data_clean.index
# data_dtm

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
