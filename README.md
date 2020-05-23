# positivity-redditbot
A simple Reddit bot just tryna spread some positivity! 

## Background
Reddit is a unique platform that lets users explore their interests, discuss information, and post content. However, often times it can be deemed as a controversial place due to peoples' opinions and can be seen as a negative platform. 

I decided to create **positivity-redditbot** which was inspired by **[my_friendly_bot](https://www.youtube.com/watch?v=AL0Oy22Rhtw)**, because there is alot of wholesome and uplifting content on Reddit from subreddits like r/aww to r/wholesomememes that are often overlooked by users in their daily content digestion.

Upon calling the bot, it will generate some wholesome Reddit posts that'll hopefully make you smile or make you feel good inside. The posts that the bot outputs updates daily. 

This project gave me a good introduction to what are social media bots, how do they work, and why do we use them. I also practiced using many different tools such as virtualenv to isolate Python environments and dependencies, Heroku to automate scripts, and APIs to fetch data.

I utilized [PRAW](https://praw.readthedocs.io/en/latest/#) (Python Reddit API Wrapper), [pushshift.io](https://pushshift.io/api-parameters/), and Python to create this bot. PRAW allowed my bot to aggregate wholesome subreddit content and respond to comments, while pushshift.io was used to monitor all Reddit comments for invocation of the bot.

## Try it out!
To use the bot, type:
```
!positivity-redditbot
```
into any Reddit comment.
