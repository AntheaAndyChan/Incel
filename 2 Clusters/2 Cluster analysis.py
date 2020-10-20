# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 16:49:41 2020

@author: anthe
"""

import os
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 

os.chdir('C:\\Users\\anthe\\Documents\\GitHub\\Incel\\2 Clusters') 
groups_agg = pd.read_csv(r'2 Cluster Solution.csv') 

plt.rcParams.update({'font.size': 12})


#Count
N= list(groups_agg.loc[:,'Count'])
groups_agg.loc[:,'Count'].plot.bar(title='Size of Groups')
plt.ylabel('Number of Members')
plt.xticks(rotation=0, horizontalalignment="center") 
plt.xticks(np.arange(2), ['Group 1', 'Group 2']) 

    
#Sentiment Valence
groups_agg['Sentiment.Valence'].plot.bar(title='Sentiment Valence',cmap="tab20c_r")
plt.ylabel('Valence')
plt.xticks(rotation=0, horizontalalignment="center")
plt.xticks(np.arange(2), ['Group 1', 'Group 2']) 

#Farrell -- Jargon
groups_agg.loc[:,'Hegemony_Conflict':'Trolling'].plot.bar(title='Incel Jargon',cmap="tab20c_r")
plt.ylabel('Proportion of Word Count')
plt.xticks(rotation=0, horizontalalignment="center")
plt.legend(title='Legend', bbox_to_anchor=(1, 1), loc='upper left',fontsize='small')
plt.xticks(np.arange(2), ['Group 1', 'Group 2']) 
#Farrell -- Misogyny
groups_agg.loc[:,'Belitting':'Total.Misogyny'].plot.bar(title='Misogyny',cmap="tab20c_r")
plt.ylabel('Proportion of Word Count')
plt.xticks(rotation=0, horizontalalignment="center")
plt.legend(title='Legend', bbox_to_anchor=(1, 1), loc='upper left',fontsize='small')
plt.xticks(np.arange(2), ['Group 1', 'Group 2']) 

#LIWC -- Summary Language
groups_agg.loc[:,'Analytic':'Tone'].plot.bar(title='LIWC -- Summary Language',cmap="tab20c_r")
plt.ylabel('Proportion of Word Count')
plt.xticks(rotation=0, horizontalalignment="center")
plt.legend(title='Legend', bbox_to_anchor=(1, 1), loc='upper left',fontsize='small')
plt.xticks(np.arange(2), ['Group 1', 'Group 2']) 
#LIWC -- Affective Processes
groups_agg.loc[:,'affect':'sad'].plot.bar(title='LIWC -- Affective Processes',cmap="tab20c_r")
plt.ylabel('Proportion of Word Count')
plt.xticks(rotation=0, horizontalalignment="center")
plt.legend(title='Legend', bbox_to_anchor=(1, 1), loc='upper left',fontsize='small')
plt.xticks(np.arange(2), ['Group 1', 'Group 2']) 
#LIWC -- Social Processes
groups_agg.loc[:,'social':'male'].plot.bar(title='LIWC -- Social Processes',cmap="tab20c_r")
plt.ylabel('Proportion of Word Count')
plt.xticks(rotation=0, horizontalalignment="center")
plt.legend(title='Legend', bbox_to_anchor=(1, 1), loc='upper left',fontsize='small')
plt.xticks(np.arange(2), ['Group 1', 'Group 2']) 
#LIWC -- Cognitive Processes
groups_agg.loc[:,'cogproc':'differ'].plot.bar(title='LIWC -- Cognitive Processes',cmap="tab20c_r")
plt.ylabel('Proportion of Word Count')
plt.xticks(rotation=0, horizontalalignment="center")
plt.legend(title='Legend', bbox_to_anchor=(1, 1), loc='upper left',fontsize='small')
plt.xticks(np.arange(2), ['Group 1', 'Group 2']) 
#LIWC -- Perceptual Processes
groups_agg.loc[:,'percept':'feel'].plot.bar(title='LIWC -- Perceptual Processes',cmap="tab20c_r")
plt.ylabel('Proportion of Word Count')
plt.xticks(rotation=0, horizontalalignment="center")
plt.legend(title='Legend', bbox_to_anchor=(1, 1), loc='upper left',fontsize='small')
plt.xticks(np.arange(2), ['Group 1', 'Group 2']) 
#LIWC -- Biological Processes
groups_agg.loc[:,'bio':'ingest'].plot.bar(title='LIWC -- Biological Processes',cmap="tab20c_r")
plt.ylabel('Proportion of Word Count')
plt.xticks(rotation=0, horizontalalignment="center")
plt.legend(title='Legend', bbox_to_anchor=(1, 1), loc='upper left',fontsize='small')
plt.xticks(np.arange(2), ['Group 1', 'Group 2']) 
#LIWC -- Drives
groups_agg.loc[:,'drives':'risk'].plot.bar(title='LIWC -- Drives',cmap="tab20c_r")
plt.ylabel('Proportion of Word Count')
plt.xticks(rotation=0, horizontalalignment="center")
plt.legend(title='Legend', bbox_to_anchor=(1, 1), loc='upper left',fontsize='small')
plt.xticks(np.arange(2), ['Group 1', 'Group 2']) 
#LIWC -- Time orientation
groups_agg.loc[:,'focuspast':'focusfuture'].plot.bar(title='LIWC -- Time orientation',cmap="tab20c_r")
plt.ylabel('Proportion of Word Count')
plt.xticks(rotation=0, horizontalalignment="center")
plt.legend(title='Legend', bbox_to_anchor=(1, 1), loc='upper left',fontsize='small')
plt.xticks(np.arange(2), ['Group 1', 'Group 2']) 
#LIWC -- Relativity
groups_agg.loc[:,'relativ':'time.1'].plot.bar(title='LIWC -- Relativity',cmap="tab20c_r")
plt.ylabel('Proportion of Word Count')
plt.xticks(rotation=0, horizontalalignment="center")
plt.legend(title='Legend', bbox_to_anchor=(1, 1), loc='upper left',fontsize='small')
plt.xticks(np.arange(2), ['Group 1', 'Group 2']) 
#LIWC -- Personal concerns
groups_agg.loc[:,'work':'death'].plot.bar(title='LIWC -- Personal concerns',cmap="tab20c_r")
plt.ylabel('Proportion of Word Count')
plt.xticks(rotation=0, horizontalalignment="center")
plt.legend(title='Legend', bbox_to_anchor=(1, 1), loc='upper left',fontsize='small')
plt.xticks(np.arange(2), ['Group 1', 'Group 2']) 
#LIWC -- Informal Language
groups_agg.loc[:,'informal':'filler'].plot.bar(title='LIWC -- Informal Language',cmap="tab20c_r")
plt.ylabel('Proportion of Word Count')
plt.xticks(rotation=0, horizontalalignment="center")
plt.legend(title='Legend', bbox_to_anchor=(1, 1), loc='upper left',fontsize='small')
plt.xticks(np.arange(2), ['Group 1', 'Group 2']) 
