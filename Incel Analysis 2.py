# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 23:53:09 2020
Incel Analysis based on Sudeep's Tutorial
@author: anthe
"""
import os
import pandas as pd
import numpy as np
import string
#import liwc 
#from scipy.spatial import distance
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score
# from sklearn import preprocessing

os.chdir('E:\\Work\\Incels\\Scrape_August 2020') 

# upload a dataset as a df. create ids. 
df = pd.read_csv(r'IncelExit.csv')
#print(coding_data.head())
coding_data=pd.DataFrame(df["body"] )
# coding_data.to_csv('coding_data.csv')
# coding_data = pd.read_csv(r'coding_data.csv')[1:]
print("Number of observations:", len(coding_data)) #41778
print("Averge number of characters in text:", np.mean([len(str(text)) for text in coding_data['body']])) #358.18


#TODO: remove /n 
# Total Misogyny Variable
# Merge codes to Original sheet (to get User)
# Make a User Sheet (w/ average scores)
# Manually code for leaving community
# Code users

# Word count dictionary analysis
# "coding_data" is a df with all the data and "dictionary" is a df with dictionary words and values
# The function will output "coding_data" with the coding dimensions as new columns
def word_count(coding_data, dictionary):    
  #print("coding_data: ", coding_data)   
  #print("type of coding_data: ", type(coding_data))
  text_data = list(coding_data.iloc[:, 0])   #convert text column to a list of strings
  #print("text_data: ", text_data)
  coding_dimensions = list(dictionary.columns)[1:]  #extract coding dimensions

  for dimension in coding_dimensions:   #iterate over coding dimensions
    print("Starting",dimension)
    dimension_dict = {}
    for index, row in dictionary.iterrows():
      dimension_dict[row['word']] = row[dimension]
    text_value = []
    #print(dimension_dict)
    
    for text in text_data:     
      clean_text = str(text).translate(str.maketrans('', '', string.punctuation)).lower().split(' ')  #remove punctuation, lower case, and split by whitespace
      #print("Text:", clean_text)
      word_count = 0
      sum_value = 0
      for word in clean_text:
          word_count += 1  #add up values for words in our dictionary
          if word in dimension_dict:
              sum_value += float(dimension_dict[word])
      #print("Sum val", sum_value)
      if word_count > 0:
        average_value = float(sum_value)/float(word_count)  #get average value in text    
        #print("Avg val", average_value)
      else:
        average_value = -99
      text_value.append(average_value)  #append average value to text_value

    #print("Text val", text_value)
    #print("Adding to original DF")
    coding_data[dimension] = text_value #add text_value to initial dataframe
    #print("type", type(coding_data))
    print("Completed", dimension)
  return coding_data

#Now upload dictionary, perform word count-based coding on each of the dictionary columns, and save as "coding_data_processed" into Google Drive.

# #Sentiment Valences 
# sentiment_codes = pd.read_csv('sentiment_dict.csv')
# sentiment_codes = sentiment_codes.drop(sentiment_codes.columns[[0]], axis=1)
# coding_data_processed = word_count(coding_data[1:],sentiment_codes) 
# coding_data_processed.to_csv('coding_data_processed.csv')

#Farrell & Miriam's Misogyny categories
incel_codes = pd.read_csv('miriam_codes.csv')
incel_codes = incel_codes.drop(incel_codes.columns[[0]], axis=1)
coding_data_processed = word_count(coding_data[1:],incel_codes) 
coding_data_processed.to_csv('coding_data_processed.csv')
 
# #print summary mean, stdev, and count of each dimension in dictionary
for dimension in list(incel_codes.columns)[1:]:
   print(dimension, coding_data_processed[dimension].mean(), '+-',coding_data_processed[dimension].std()/(coding_data_processed[dimension].count()**.5))


# #Do this again with Sudeep's sentiment valences
# sentiment_dic = pd.read_csv(r'coding_dictionary_sentiment.csv')
# coding_data_processed = word_count(coding_data,sentiment_dic)

# for dimension in list(sentiment_dic.columns)[1:]:
#   print(dimension,coding_data_processed[dimension].mean(), '+-',coding_data_processed[dimension].std()/(coding_data_processed[dimension].count()**.5))

# #count number of words in each post
# def my_count(var):
#     tmp = len(str(var.split()))
#     return tmp
# #count UNIQUE words in each post
# def my_unique_count(var):
#     tmp = len(set(var.split()))
#     return tmp
    
# coding_data['count'] = coding_data.body.apply(my_count)
# coding_data['unique_count'] = coding_data.body.apply(my_unique_count)





# #save
# coding_data_processed.to_csv('coding_data_processed.csv')
