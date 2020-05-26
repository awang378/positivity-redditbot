import os
import praw 
import config
import requests
import time
import random
import json

# Reddit API login
def get_reddit():
    print("Logging in...")
    reddit = praw.Reddit(username = config.username,
                        password = config.password,
                        client_id = config.client_id,
                        client_secret = config.client_secret,
                        user_agent = "positivity bot by /u/awang378")
    print("Logged in!")
    return reddit

# Aggregating Top Wholesome Posts of the Day

# Top r/aww posts daily
def get_aww_data(reddit):
    aww = reddit.subreddit("Aww")
    posts = []
    for post in aww.top("day", limit=5):
       posts.append("https://www.reddit.com" + post.permalink)
    return posts

# Top r/Eyebleach posts daily 
def get_eyebleach_data(reddit):
    eyebleach = reddit.subreddit("Eyebleach")
    posts = []
    for post in eyebleach.top("day", limit=5):
       posts.append("https://www.reddit.com" + post.permalink)
    return posts

# Top r/AnimalsBeingBros posts daily
def get_animalsbros_data(reddit):
    animalsbros = reddit.subreddit("AnimalsBeingBros")
    posts = []
    for post in animalsbros.top("day", limit=5):
       posts.append("https://www.reddit.com" + post.permalink)
    return posts

# Top r/HumansBeingBros posts daily
def get_humansbros_data(reddit):
    humanbros = reddit.subreddit("HumansBeingBros")
    posts = []
    for post in humanbros.top("day", limit=5):
       posts.append("https://www.reddit.com" + post.permalink)
    return posts

# Top r/UpliftingNews posts daily
def get_news_data(reddit):
    news = reddit.subreddit("UpliftingNews")
    posts = []
    for post in news.top("day", limit=5):
       posts.append("https://www.reddit.com" + post.permalink)
    return posts

# Top r/MadeMeSmile posts daily
def get_smile_data(reddit):
    smile = reddit.subreddit("MadeMeSmile")
    posts = []
    for post in smile.top("day", limit=10):
       posts.append("https://www.reddit.com" + post.permalink)
    return posts

# Top r/wholesomememes posts daily
def get_wholesome_data(reddit):
    wholesome = reddit.subreddit("wholesomememes")
    posts = []
    for post in wholesome.top("day", limit=10):
       posts.append("https://www.reddit.com" + post.permalink)
    return posts

# Reply to user's comment
def reply_to_comment(reddit, comment_id, comment_reply, comment_subreddit, comment_author, comment_body):
    
    try:
        comment_to_be_replied_to = reddit.comment(id=comment_id)
        comment_to_be_replied_to.reply(comment_reply)
        print (f"\nReply details:\nSubreddit: r/{comment_subreddit}\nComment:\"{comment_body}\"\nUser: u/{comment_author}\a")

    # Error Handling
    except Exception as e:
        time_remaining = 15
        if (str(e).split()[0] == "RATELIMIT:"):
            for i in str(e).split():
                if (i.isdigit()):
                    time_remaining = int(i)
                    break
            if (not "seconds" or not "second" in str(e).split()):
                time_remaining *= 60

        print (str(e.__class__.__name__) + ": " + str(e))
        for i in range(time_remaining, 0, -5):
            print ("Retrying in", i, "seconds..")
            time.sleep(5)


def run(reddit):
    # We need to handle which comments our bot replies to efficiently
    last_utc = 0

    with open("utc.txt", "r") as f:
        # Retrieve the last UTC replied to
        last_utc = f.read().split("\n")[-1]

    try:
        # Search Reddit 
        comment_url = r"https://api.pushshift.io/reddit/search/comment/?q=!positivity-redditbot&sort=desc&size=50&fields=author,body,created_utc,id,subreddit&after=" + last_utc
        parsed_comment_json = json_dump_and_parse("comment_data.json", requests.get(comment_url))
        
        if (len(parsed_comment_json["data"]) == 0):
            return str(last_utc)
        else:
            last_utc = parsed_comment_json["data"][0]["created_utc"]

        # Write to File the last utc
        with open("utc.txt", "w") as f:
            f.write(str(last_utc))

        for comment in parsed_comment_json["data"]:
            comment_author = comment["author"]
            comment_body = comment["body"]
            comment_id = comment["id"]
            comment_subreddit = comment["subreddit"]
            comment_reply = ""

            if (("!positivity-redditbot" in comment_body.lower()) and comment_author != "positivity-redditbot"):
                print ("\n\nFound a comment!")

                # Update posts
                animal_posts = get_aww_data(reddit) + get_eyebleach_data(reddit) + get_animalsbros_data(reddit)
                human_posts = get_humansbros_data(reddit) + get_news_data(reddit) + get_smile_data(reddit)
                funny_posts = get_wholesome_data(reddit)

                # Randomly choose posts
                rand_animal = random.choice(animal_posts)
                rand_person = random.choice(human_posts)
                rand_meme = random.choice(funny_posts)

                # Format reply
                comment_reply = f"Hey, {comment_author}! I hope I can make your day with these wholesome reddit posts 😊!\n\n{rand_animal}\n\n{rand_person}\n\n{rand_meme}"
                comment_reply += ("\n\n\n\n---\n\n^(Beep beep, I'm a bot. Checkout my [github](https://github.com/awang378/positivity-redditbot).)")
                print(comment_body)
                print(comment_reply)
                reply_to_comment(reddit, comment_id, comment_reply, comment_subreddit, comment_author, comment_body)
                print ("\nFetching comments..")

    except Exception as e:
            print (str(e.__class__.__name__) + ": " + str(e))

    return str(last_utc)

# Parse JSON File
def json_dump_and_parse(file_name, request):
    with open(file_name, "w+") as f:
        json.dump(request.json(), f, sort_keys = True, ensure_ascii = False, indent = 4)
    with open(file_name) as f:
        data = json.load(f)
    return data


if __name__ == "__main__":
    reddit = get_reddit()
    run(reddit)

    