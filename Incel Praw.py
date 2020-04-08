# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 11:59:46 2020

@author: Chan234
"""
import praw

#setup reddit instance
reddit=praw.Reddit(client_id= 'AHg4WHV1FIjPig',
                   client_secret= 'pi7ttIzSPGcOt8B4VUtLYvkA8fg',
                   username= 'AndyResearch',
                   password= 'Greta-Andy-Kaylee2020',
                   user_agent= 'Incel Research')

#Establish the subreddit
incelexit_sub=reddit.subreddit('IncelExit')

#Basic subreddit info
filename='C:\\Users\\Chan234\\Documents\\Personal Research\\Incels\\Scraping\\IncelExit\\' + str(incelexit_sub) + '.txt'
File_object = open(filename,"w+")
L=["Subreddit Title:", str(incelexit_sub),"\n",incelexit_sub.description]
File_object.writelines(L)
File_object.close()

# hottest posts
hot_IncelExit = incelexit_sub.hot(limit=100)
for submission in hot_IncelExit:
    filename = 'C:\\Users\\Chan234\\Documents\\Personal Research\\Incels\\Scraping\\IncelExit\\Posts\\' + submission.id + '.txt'
    File_object = open(filename, "w+")
    L = [(100 * '-'), "\n",
         str(filename), "\n",
         'Post Title: ', str(submission.title), "\n",
         'Post ID: ', str(submission.id), "\n",
         'Ups: ', str(submission.ups), "\n",
         'Downs: ', str(submission.downs), "\n",
         'Body: ', str(submission.selftext), "\n"]

    File_object.writelines(L)
    File_object.close()
     

hot_IncelExit = incelexit_sub.hot(limit=100)
for submission in hot_IncelExit:
    submission.comments.replace_more(limit=None)
    comments = submission.comments.list()
    comment_filename = 'C:\\Users\\Chan234\\Documents\\Personal Research\\Incels\\Scraping\\IncelExit\\Comments\\' + submission.id + '_comments.txt'
    comment_File_object = open(comment_filename,"w+")
    L_comments=[]
    for comment in comments:
        L_comments.append([(20*'-'), "\n",
        'Post ID: ', str(submission.id), "\n",
        'Parent ID: ', str(comment.parent()), "\n", #parents can be the submission, or the comment
        'Comment ID: ', str(comment.id), "\n",
        'Body: ', str(comment.body), "\n"])
    print(L_comments)
    comment_File_object.writelines(L_comments)
    comment_File_object.close()
 