#!/usr/bin/env python3

from dotenv import load_dotenv
import os
import sys
import tweepy

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
print(dotenv)
load_dotenv(dotenv_path)

try:
  consumer_key = os.getenv('TWEETER_CONSUMER_KEY')
  consumer_secret = os.getenv('TWEETER_CONSUMER_SECRET')
  access_token = os.getenv('TWEETER_ACCESS_TOKEN')
  access_token_secret = os.getenv('TWEETER_ACCESS_TOKEN_SECRET')
except KeyError(e):
  pass

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

stamp = '#tweeterminal '

tweet = sys.argv[1]
final_tweet = stamp + tweet
api.update_status(final_tweet)
