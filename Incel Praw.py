# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 11:59:46 2020

@author: Chan234
"""
import praw
import json

reddit=praw.Reddit(client_id= 'AHg4WHV1FIjPig',
                   client_secret= 'pi7ttIzSPGcOt8B4VUtLYvkA8fg',
                   username= 'AndyResearch',
                   password= 'Greta-Andy-Kaylee2020',
                   user_agent= 'Incel Research')

def get_hot_posts(sub):
    return  sub.hot(limit=100)

def jsonify_post(post, file_object):
    post_json = {
        'Post Title': post.title,
        'Post ID': post.id,
        'Post Upvotes': post.ups,
        'Post Downvotes': post.downs,
        'Post Body': post.selftext
        } 
    return post_json

def jsonify_comment(comment, file_object):
    c_out = {
        'Parent ID': str(comment.parent()), #parents can be the submission, or the comment
        'Comment ID': comment.id,
        'Comment Body': comment.body
        } 
    return c_out
     
def savehotsubreddit(subreddit):   
    incel_sub=reddit.subreddit(subreddit)
    
    hot_posts = get_hot_posts(incel_sub) 
    for post in hot_posts:
        post_path = f'C:\\Users\\Chan234\\Documents\\Personal Research\\Incels\\Scraping\\{subreddit}\\{post.id}.txt'
        post_file = open(post_path, "w+") 
        post_json = jsonify_post(post, post_file)
         
        post.comments.replace_more(limit=None)
        comments = post.comments.list()
        comment_json = []
        for comment in comments:
            comment_json.append(jsonify_comment(comment, post_file))
        post_json['Comments'] = comment_json
        post_file.writelines(json.dumps(post_json,  indent=4))
        post_file.close()
 
subreddits= ['ricecels','hapacels','IncelExit','inceltears','IncelswithoutHate','IncelsInAction','TruFemCels','AskTruFemCels']
for sub in subreddits:
    savehotsubreddit(sub)