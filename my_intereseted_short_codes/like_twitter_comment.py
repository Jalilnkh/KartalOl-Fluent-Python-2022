import tweepy
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# Get your Twitter API credentials from https://developer.twitter.com/en/apps
# Create a Tweepy API object
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Post a message
message = "Hello, world! This is my first tweet using Python."
api.update_status(message)

print("Tweeted: %s" % message)