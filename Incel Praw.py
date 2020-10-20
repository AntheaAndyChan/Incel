# -*- coding: utf-8 -*-
"""
Created on Tue Apr 7 11:59:46 2020

@author: Chan234
"""
import praw
import pandas as pd
# import json

reddit=praw.Reddit(client_id= 'AHg4WHV1FIjPig',
                   client_secret= 'pi7ttIzSPGcOt8B4VUtLYvkA8fg',
                   username= 'AndyResearch',
                   password= 'Greta-Andy-Kaylee2020',
                   user_agent= 'Incel Research')

# We now want to get all posts from incelexit specifically, and save them into a dataframe to export to csv later
subreddit = reddit.subreddit('IncelExit')
submission_title = []
submission_ID = []
ups = []
body = []
time = []
num_comments = []
link = []
redditor = []
i=0


for submission in subreddit.top(limit=10000):
    i+=1
    submission_title.append(submission.title)
    submission_ID.append(submission.id)
    time.append(submission.created_utc)
    ups.append(submission.ups)
    body.append(submission.selftext)
    num_comments.append(submission.num_comments)
    link.append(submission.permalink)
    redditor.append(submission.author) 
    if i%10 == 0:
        print(f'{i} submissions completed')
    
posts_df = pd.DataFrame(
    {'submission_title': submission_title, 
        'submission_ID': submission_ID,
        'redditor': redditor,
        'ups': ups,
        'body': body,
        'time': time,
        'num_comments': num_comments,
        'link': link
    })

posts_df.head(10)

#comments
submission_title = []
parent_ID = []
submission_ID = []
comment_ID = []
body = []
redditor = []
ups = []
time = []
is_submitter=[]
link = []
subs=0
bot1= "I'm a bot"
bot2= "^^I'm ^^a ^^bot" 

for submission in subreddit.top(limit=10000):
    subs+=1
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list(): 
       #check if comment contains bots 
       if bot1 not in comment.body and bot2 not in comment.body: 
            submission_ID.append(submission.id)
            submission_title.append(submission.title)
            parent_ID.append(str(comment.parent()))
            comment_ID.append(comment.id)
            redditor.append(comment.author)
            is_submitter.append(comment.is_submitter)
            body.append(comment.body)
            ups.append(comment.ups)
            link.append(submission.permalink)
            time.append(comment.created_utc)
    if subs%10 == 0:
        print(f'{subs} submissions comments completed')
    
        
comments_df = pd.DataFrame(
    {'submission_ID': submission_ID,
        'submission_title': submission_title, 
        'parent_ID': parent_ID,
        'comment_ID': comment_ID,
        'redditor': redditor,
        'ups': ups,
        'body': body,
        'time': time,
        'body': body,
        'is_submitter':is_submitter,
        'link': link
    })

comments_df.head(10)

#merge comments and post dfs, sort by submission ID then parent ID then comment ID, then export to csv
all_content = [posts_df, comments_df]
result = pd.concat(all_content)
result.to_csv (r'C:\Users\anthe\Documents\GitHub\Incel\IncelExit_Octobermore.csv', index = False, header=True)

#When we want to start investigating prolific posters, 
#check out this link: https://praw.readthedocs.io/en/latest/code_overview/models/redditor.html
#once we get the csv we can get a frequency of redditors! 