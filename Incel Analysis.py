# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 15:39:20 2020

@author: Chan234
"""

import json
import os 
#import pdb
import re
import string
#import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from nltk.stem.porter import PorterStemmer


#this function parses each file(post) in each folder(subreddit)
#it creates lists that contain all the titles, bodies, and comments seperately 
def parsethru(folder):
    directory=f"E:\\Work\\Incels\\Scraping\\{folder}\\"
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
    
subreddits= ['IncelExit']
#subreddits= ['ricecels','hapacels','IncelExit','IncelswithoutHate','IncelsInAction','TruFemCels','AskTruFemCels']
title_dict={}
bodies_dict={}
comments_dict={}

for subreddit in subreddits:
    titles, bodies, comments = parsethru(subreddit)  
    title_dict[subreddit]= titles
    bodies_dict[subreddit]= bodies
    comments_dict[subreddit]= comments

# print("\n Titles: ") 
# print(title_dict)
# print("\n Bodies: ") 
# print(bodies_dict)
# print("\n Comments: ") 
# print(comments_dict)
# print(comments_dict.keys())

# text cleaning 
stop_words = stopwords.words('english')
stop_words.append('like')
stop_words.append('im')
stop_words.append('get')
stop_words.append('would')
stop_words.append('ive')
stop_words.append('youre')
stop_words.append('cant')
stop_words.append('also')
stop_words.append('didnt')
stop_words.append('dont')
stop_words.append('got')
stop_words.append('really')
stop_words.append('thats')
stop_words.append('even')

#Make text lowercase, remove punctuation and remove words containing numbers.
# remove remaining tokens that are not alphabetic
# filter out stop words
def clean_text_round1(text):
    text = text.lower()
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = re.sub('[‘’“”…]', '', text)
    text = re.sub('\n', ' ', text)
    tokens = word_tokenize(text)
    words = [word for word in tokens if word.isalpha()]
    words = [w for w in words if not w in stop_words]
    # convert words to stems
    porter = PorterStemmer()
    words = [porter.stem(word) for word in words]
    return words
  
def listToString(s):  
    str1 = ""  
    for ele in s:  
        str1 += ele  
        str1 += " "  
    return str1  

for subreddit,commentslist in comments_dict.items():
    data_clean=[]
    for comment in commentslist:        
        data_clean.append(listToString(clean_text_round1(comment)))
    comments_dict[subreddit]=listToString(data_clean)
 
#print(comments_dict.keys())
#print("hapacels: ", comments_dict['hapacels'])
#print("ricecels: ", comments_dict['ricecels'])

def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


#sort values lowest to highest 
wordcounts_dict={}
for subreddit, comments in comments_dict.items():
    wordcounts_dict[subreddit]=word_count(comments)
    
#print(wordcounts_dict)

for subreddit, comments in wordcounts_dict.items():
    filename=f"E:\\Work\\Incels\\Scraping\\wordcounts\\{subreddit}.txt"
    f=open(filename,"w+")
    for word in sorted(comments, key=comments.get, reverse=True):
        f.write(f'{word} {comments[word]}\n')
        if comments[word] < 10:
            break 
    f.close()
        

 