#%%
import tweepy
import os
# Twitter API credentials
consumer_key =  os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

# Authenticate to Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Define keywords to search for
keywords = ["آدربایجان", "ترکی", "منوفارسی"]

# Get tweets based on keywords
try:
    api.verify_credentials()
    print("Authentication successful. Your Twitter Developer account is valid.")
except tweepy.error.TweepError as e:
    print(f"Authentication failed. Error: {str(e)}")
# Create a tweet