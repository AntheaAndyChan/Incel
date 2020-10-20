# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 15:39:20 2020

@author: Chan234
"""

import os
import pandas as pd
import numpy as np
import string
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 

os.chdir('C:\\Users\\anthe\\Documents\\GitHub\\Incel') 
df = pd.read_csv(r'IncelExit_October.csv') 
print("Number of observations:", len(df["body"])) #49279
print("Average number of characters in text:", np.mean([len(str(df["body"])) for text in df["body"]])) #689.0

""" Quick Cleaning """
df = df.dropna(subset=['body']) #drop people without bodies  - 49181
df=df[df['redditor']!='AutoModerator']#Delete all lines by Automoderator - 47963
df=df[df['body']!='[removed]']#Delete all removed bodies - 45150
df=df[df['body']!='[deleted]']#Delete all removed bodies - 43625

#Convert Time to datetime
df["time"]=pd.to_datetime(df["time"],unit='s')

stopwords = stopwords.words('english')
stopwords.append('nan')
def clean_text(text):
    """Clean Text: make lowercase, remove punctuation, words with numbers
    Remove stop words
    Tokenize"""
    text = str(text).lower() # Make text lowercase
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text) # remove punctuation and remove words containing numbers.
    text = re.sub('\w*\d\w*', '', text) 
    text = re.sub('[‘’“”…]', '', text)
    text = re.sub('\n', ' ', text)
    tokens = word_tokenize(text) # Each line gets a new column containing a list of clean tokens
    words = [word for word in tokens if word.isalpha()] # remove remaining tokens that are not alphabetic
    words = [w for w in words if not w in stopwords] # filter out stop words
    return words
   
df['clean_text'] = df.apply(lambda row: clean_text(row.body), axis=1)

def word_count(dataframe, dictionary):   
    """Word count dictionary analysis
    "coding_data" is a df with all the data and "dictionary" is a df with dictionary words and values
    The function will output "coding_data" with the coding dimensions as new columns"""
    coding_data= dataframe['clean_text']
    coding_dimensions = list(dictionary.columns)[1:]  #extract coding dimensions

    for dimension in coding_dimensions:   #iterate over coding dimensions
        print("Starting: ",dimension)
        dimension_dict = {}
        for index, row in dictionary.iterrows():
            dimension_dict[row['word']] = row[dimension]
        text_value = [] 
        for text_list in coding_data:     
            word_count = 0
            sum_value = 0
            for word in text_list:
                word_count += 1  #add up values for words in our dictionary
                if word in dimension_dict:
                    sum_value += float(dimension_dict[word])
            if word_count > 0:
                average_value = float(sum_value)/float(word_count)  #get average value in text   
            else:
                average_value = None
            text_value.append(average_value)  #append average value to text_value
    
        dataframe[dimension] = text_value #add text_value to initial dataframe
        print("Completed: ", dimension)
    return dataframe

""" Farrell & Miriam's Incel Jargon categories """
incel_codes = pd.read_csv('Jargon_codes.csv')
incel_codes = incel_codes.drop(incel_codes.columns[[0]], axis=1)
word_count(df,incel_codes) 

""" Farrell & Miriam's Misogyny categories """
miso_codes = pd.read_csv('Misogyny_codes.csv')
miso_codes = miso_codes.drop(miso_codes.columns[[0]], axis=1)
miso_codes['Total Misogyny']=1
word_count(df,miso_codes) 

""" Sentiment Analysis """
sentiment_codes = pd.read_csv('sentiment_dict.csv')
sentiment_codes=sentiment_codes.rename(columns={"Word": "word", "Valence": "Sentiment Valence"})
word_count(df,sentiment_codes) 


""" Export Main Sheet """
df.to_csv('coding_data_processed_October.csv')

""" Summary Statistics """
for dimension in list(incel_codes.columns)[1:]:
    print(dimension, ":\tMean: ", round(df[dimension].mean(),4),
          ',\tSD: ', round(df[dimension].std(),3),
      ", \tMin: ", round(df[dimension].min(),3),
      ", \tMax: ", round(df[dimension].max(),3),sep='')
for dimension in list(miso_codes.columns)[1:]:
    print(dimension, ":\tMean: ", round(df[dimension].mean(),4),
          ',\tSD: ', round(df[dimension].std(),3),
      ", \tMin: ", round(df[dimension].min(),3),
      ", \tMax: ", round(df[dimension].max(),3),sep='')
print("Sentiment Valence: \tMean: ", round(df["Sentiment Valence"].mean(),4),
      ', \tSD: ', round(df["Sentiment Valence"].std(),3),
      ", \tMin: ", df["Sentiment Valence"].min(),
      ", \tMax: ", df["Sentiment Valence"].max(),
      sep='')

##############################################################################
# TODO: 
""" Make a User Sheet (w/ average scores) """
users = df.groupby(["redditor"])
df["redditor"].value_counts().head(20)
df["redditor"].value_counts(normalize=True).head(20)
users['body'].get_group('library_wench').head(20)
    #OK she looks normal, just super prolific

#means=df.groupby('redditor').mean()  
grouped_single = df.groupby('redditor').agg({'time': ['min', 'max']})
grouped_single['Timespan'] = grouped_single['max']-grouped_single['min']

usersheet=pd.DataFrame()

for dimension in list(df.loc[:,'Hegemony_Conflict':'Sentiment Valence']):
    usersheet[dimension]=df.groupby(["redditor"])[dimension].transform(np.mean)
    #Create an aggregated usersheet with Averages
users.first() 
#Time of first post, time of last post, length of time in subreddit

#Total number of posts 
#Range of Dates

#Subsample those with scores 3 SDs above/below mean on each dimension
#

"""Word Frequency"""
#Most Frequent Words
#Most Frequent Bigrams
# from nltk.probability import FreqDist
# for row in df['clean_text']:
#     fdist = FreqDist(row)
#     print(fdist)
# import matplotlib.pyplot as plt
# fdist.plot(30,cumulative=False)
# plt.show()

"""count number of words in each post"""
# def my_count(var):
#     tmp = len(str(var.split()))
#     return tmp
"""count UNIQUE words in each post"""
# def my_unique_count(var):
#     tmp = len(set(var.split()))
#     return tmp
    
# coding_data['count'] = coding_data.body.apply(my_count)
# coding_data['unique_count'] = coding_data.body.apply(my_unique_count)




# import json
# import os 
# #import pdb
# import re
# import string
# #import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize 
# from nltk.stem.porter import PorterStemmer


# #this function parses each file(post) in each folder(subreddit)
# #it creates lists that contain all the titles, bodies, and comments seperately 
# def parsethru(folder):
#     directory=f"E:\\Work\\Incels\\Scraping\\{folder}\\"
#     titles=[]
#     bodies=[]
#     comments=[]

#     for filename in os.listdir(directory):
#         f = open(directory+filename,"r")
#         lines = f.read()
#         post_dict=json.loads(lines)
        
#         titles.append(str(post_dict['Post Title']))
#         bodies.append(str(post_dict['Post Body']))
        
#         for comment in post_dict['Comments']:
#             comments.append(str(comment['Comment Body']))
#     return titles, bodies, comments
    
# subreddits= ['IncelExit']
# #subreddits= ['ricecels','hapacels','IncelExit','IncelswithoutHate','IncelsInAction','TruFemCels','AskTruFemCels']
# title_dict={}
# bodies_dict={}
# comments_dict={}

# for subreddit in subreddits:
#     titles, bodies, comments = parsethru(subreddit)  
#     title_dict[subreddit]= titles
#     bodies_dict[subreddit]= bodies
#     comments_dict[subreddit]= comments

# # print("\n Titles: ") 
# # print(title_dict)
# # print("\n Bodies: ") 
# # print(bodies_dict)
# # print("\n Comments: ") 
# # print(comments_dict)
# # print(comments_dict.keys())

# # text cleaning 
# stop_words = stopwords.words('english')
# stop_words.append('like')
# stop_words.append('im')
# stop_words.append('get')
# stop_words.append('would')
# stop_words.append('ive')
# stop_words.append('youre')
# stop_words.append('cant')
# stop_words.append('also')
# stop_words.append('didnt')
# stop_words.append('dont')
# stop_words.append('got')
# stop_words.append('really')
# stop_words.append('thats')
# stop_words.append('even')

# #Make text lowercase, remove punctuation and remove words containing numbers.
# # remove remaining tokens that are not alphabetic
# # filter out stop words
# def clean_text_round1(text):
#     text = text.lower()
#     text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
#     text = re.sub('\w*\d\w*', '', text)
#     text = re.sub('[‘’“”…]', '', text)
#     text = re.sub('\n', ' ', text)
#     tokens = word_tokenize(text)
#     words = [word for word in tokens if word.isalpha()]
#     words = [w for w in words if not w in stop_words]
#     # convert words to stems
#     porter = PorterStemmer()
#     words = [porter.stem(word) for word in words]
#     return words
  
# def listToString(s):  
#     str1 = ""  
#     for ele in s:  
#         str1 += ele  
#         str1 += " "  
#     return str1  

# for subreddit,commentslist in comments_dict.items():
#     data_clean=[]
#     for comment in commentslist:        
#         data_clean.append(listToString(clean_text_round1(comment)))
#     comments_dict[subreddit]=listToString(data_clean)
 
# #print(comments_dict.keys())
# #print("hapacels: ", comments_dict['hapacels'])
# #print("ricecels: ", comments_dict['ricecels'])

# def word_count(str):
#     counts = dict()
#     words = str.split()
#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1
#     return counts


# #sort values lowest to highest 
# wordcounts_dict={}
# for subreddit, comments in comments_dict.items():
#     wordcounts_dict[subreddit]=word_count(comments)
    
# #print(wordcounts_dict)

# for subreddit, comments in wordcounts_dict.items():
#     filename=f"E:\\Work\\Incels\\Scraping\\wordcounts\\{subreddit}.txt"
#     f=open(filename,"w+")
#     for word in sorted(comments, key=comments.get, reverse=True):
#         f.write(f'{word} {comments[word]}\n')
#         if comments[word] < 10:
#             break 
#     f.close()
        

 