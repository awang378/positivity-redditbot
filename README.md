# positivity-redditbot
A simple Reddit bot just tryna spread some positivity! 

## Background
Reddit is a unique platform that lets users explore their interests, discuss information, and post content. However, often times it can be deemed as a controversial place due to people's opinions and negativity.

I decided to create **positivity-redditbot** which was inspired by **[my_friendly_bot](https://www.youtube.com/watch?v=AL0Oy22Rhtw)**, because there is a lot of wholesome and uplifting content on Reddit from subreddits like r/aww to r/wholesomememes that are often overlooked by users in their daily content digestion.

Upon calling the bot, it will generate some wholesome Reddit posts that'll hopefully make you smile or lift up your day. The posts that the bot outputs updates daily. 

I utilized [PRAW](https://praw.readthedocs.io/en/latest/#) (Python Reddit API Wrapper), [pushshift.io](https://pushshift.io/api-parameters/), and Python to create this bot. PRAW allowed my bot to aggregate wholesome subreddit content and respond to comments, while pushshift.io was used to monitor all Reddit comments for invocation of the bot. I also added basic automation functionality using a service called [Python Anywhere](www.pythonanywhere.com) which is a web hosting service for Python that will run the bot script every 24 hours. 

## Setup
You can try it out locally by cloning this repository.
I would also create a config.py file to hold your global configuration variables which you can get by registering a [Reddit application](https://www.reddit.com/prefs/apps/).
The variables needed are
* username
* password
* client_id
* client_secret

```
pip install -r requirements.txt
python3 bot.py
```

## Try it out!
To use the bot, type:
```
!positivity-redditbot
```
into any Reddit comment. It should respond within 24 hours. 

If you're interested in learning more, checkout this [tutorial](https://www.pythonforengineers.com/build-a-reddit-bot-part-1/), [bottiquette](https://www.reddit.com/r/Bottiquette/wiki/bottiquette), and the [inspiration repo](https://github.com/harshibar/friendly-redditbot).
