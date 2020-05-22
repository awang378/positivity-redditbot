import os
import praw 
import config
import requests

# Reddit API login
def get_reddit():
    print ("Logging in...")
    reddit = praw.Reddit(username = config.username,
                        password = config.password,
                        client_id = config.client_id,
                        client_secret = config.client_secret,
                        user_agent = "positivity bot by /u/awang378")
    print("Logged in!")
    return reddit

# Top r/aww posts
def get_aww_data(reddit):
    aww = reddit.subreddit("Aww")
    posts = []
    for post in aww.top("day", limit=10):
       posts.append(post.url)

    return posts

# Top r/eyebleach posts
def get_eyebleach_data(reddit):
    aww = reddit.subreddit("Eyebleach")
    posts = []
    for post in aww.top("day", limit=10):
       posts.append(post.url)

    return posts



if __name__ == "__main__":
    reddit = get_reddit()