import praw
import os
import re

bot_instance = praw.Reddit("bot1")
subreddit = bot_instance.subreddit("learnpython")

if not os.path.isfile("repiled.txt"):
    post_replied = []

else:
    with open("replied.txt", "r") as f:
        post_replied = f.read()
        post_replied = post_replied.split("\n")
        post_replied = list(filter(None.post_replied))


for submission in subreddit.hot(limit=5):
    if submission.id not in post_replied:
        if re.search("i love pyhton", submission.title, re.IGNORECASE):
            submission.reply("MEEEEE TOOOOOO!!!!")
            post_replied.append(submission.id)

with open("repiled.txt", "w") as f:
    for id in post_replied:
        f.write(id + "\n")
