import tweepy
import os 
consumer_key =  os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

# Authenticate to Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Specify the username of the user
username = "KartalOldotCom"

# Retrieve user ID
user = api.get_user(screen_name=username)
user_id = user.id_str

print("User ID:", user_id)

