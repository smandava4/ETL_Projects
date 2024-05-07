import pandas as pd
import s3fs 
import json 
from datetime import datetime
import tweepy
import config as c


# Initialize the client
client = tweepy.Client(bearer_token=c.bearer_token,
                        access_token=c.access_token,
                        access_token_secret=c.access_token_secret,
                        consumer_key=c.api_key,
                        consumer_secret=c.api_secret)
# To get information about me  
#tweepy.user.USER_FIELDS= ['created_at', 'description', 'entities', 'id', 'location', 'name', 'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics', 'url', 'username', 'verified', 'verified_type', 'withheld']
# Specify the user fields you want to retrieve
user_fields = ['created_at', 'description', 'entities', 'id', 'location', 'name', 'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics', 'url', 'username', 'verified', 'verified_type', 'withheld']

# Get user information with specified user fields
user = client.get_me(user_fields=user_fields)

print(user.data)


# to post a tweet into my account 
response=client.create_tweet(text=input("Enter a tweet to post into your account"))

response_data=response.data
print(response_data)
tweet_ids=response_data['edit_history_tweet_ids']

print(tweet_ids)
# to delete a tweet  use 	Client.delete_tweet()

del_response=client.delete_tweet()
del_response=client.delete_tweet(tweet_ids[0])

print(del_response.data)