import praw

reddit = praw.Reddit(
    client_id="lX0p4n5l0hpoZNnwCnFmdw",
    client_secret="AnzH84wIDlnzR8fg0WT6bHD3x4seNQ",
    user_agent="testbot by u/languageexchangebot",
    username="languageexchangebot",
    password="WS6miMJvUAM96mxL"
)

subreddit = reddit.subreddit("test")

# Create a post
title = "Hello from my bot!"
selftext = "This is a test post made by a bot."
post = subreddit.submit(title=title, selftext=selftext)

print(f"Post created: {post.url}")
