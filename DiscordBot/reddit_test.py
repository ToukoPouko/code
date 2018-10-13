import praw
import pprint

reddit = praw.Reddit(client_id="nmNjm5-kOyATOA", client_secret="n3Sf8xOmZIJka9-bvjtcwQUWPsw", password="IcPMLmJUK3CbXONRk2dv", user_agent="test by /u/gamedeal_bot", username="gamedeal_bot")

reddit.read_only = True

subreddit = reddit.subreddit("dankmemes")
submission = subreddit.random()
print(submission.url)