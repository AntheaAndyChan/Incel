# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 11:59:46 2020

@author: Chan234
"""
import praw
import json

#setup reddit instance
reddit=praw.Reddit(client_id= 'AHg4WHV1FIjPig',
                   client_secret= 'pi7ttIzSPGcOt8B4VUtLYvkA8fg',
                   username= 'AndyResearch',
                   password= 'Greta-Andy-Kaylee2020',
                   user_agent= 'Incel Research')

def get_hot_posts(sub):
    return  sub.hot(limit=100)

def write_post_info(post, file_object):
    out = {
        'Post Title': post.title,
        'Post ID': post.id,
        'Post Upvotes': post.ups,
        'Post Downvotes': post.downs,
        'Post Body': post.selftext
        } 
    file_object.writelines(json.dumps(out, indent=4))
   
def write_comment_info(comment, file_object):
    c_out = {
        'Parent ID: ': str(comment.parent()), #parents can be the submission, or the comment
        'Comment ID: ': comment.id,
        'Comment Body: ': comment.body
        } 
    file_object.writelines(json.dumps(c_out,  indent=4))
     
def savehotsubreddit(subreddit):   
    incel_sub=reddit.subreddit(subreddit)
    
    #Basic subreddit info
    filename=f'C:\\Users\\Chan234\\Documents\\Personal Research\\Incels\\Scraping\\{subreddit}\\{subreddit}.txt'
    File_object = open(filename,"w+")
    L=["Subreddit Title:", str(incel_sub),"\n",incel_sub.description]
    File_object.writelines(L)
    File_object.close()

    #posts n comments
    hot_posts = get_hot_posts(incel_sub) 
    for post in hot_posts:
        post_path = f'C:\\Users\\Chan234\\Documents\\Personal Research\\Incels\\Scraping\\{subreddit}\\{post.id}.txt'
        post_file = open(post_path, "w+") 
        write_post_info(post, post_file)
         
        post.comments.replace_more(limit=None)
        comments = post.comments.list()
        for comment in comments:
            write_comment_info(comment, post_file)
        post_file.close()
 
# shortcel  #banned        
# ricecels
savehotsubreddit('ricecels') 
# hapacels 
savehotsubreddit('hapacels') 
# IncelExit
savehotsubreddit('IncelExit') 
# inceltears
savehotsubreddit('inceltears') 
# IncelswithoutHate
savehotsubreddit('IncelswithoutHate') 
# IncelsInAction
savehotsubreddit('IncelsInAction') 
# TruFemCels
savehotsubreddit('TruFemCels') 
# AskTruFemCels
savehotsubreddit('AskTruFemCels') 
# IntelligentCels   #banned 