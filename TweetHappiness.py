# Dependencies
import tweepy
import time
import json
import random
import os

# Twitter API Keys
consumer_key = os.environ['consumer_key']
consumer_secret = os.environ ['consumer_secret']
access_token= os.environ['access_token']
access_secret= os.environ['access_secret']

#     # Twitter credentials
# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Import and Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Quotes to Tweet
happy_quotes = [
    "For every minute you are angry you lose sixty seconds of happiness. - Ralph Waldo Emerson",
    "Folks are usually about as happy as they make their minds up to be. - Abraham Lincoln",
    "Happiness is when what you think, what you say, and what you do are in harmony. - Mahatma Gandhi",
    "Count your age by friends, not years. Count your life by smiles, not tears. - John Lennon",
    "Happiness is a warm puppy. - Charles M. Schulz",
    "The happiness of your life depends upon the quality of your thoughts. - Marcus Aurelius",
    "Now and then it's good to pause in our pursuit of happiness and just be happy. - Guillaume Apollinaire"]



for quote in happy_quotes:
	api.update_status(quote)
    print("{0} \n".format(quote))
    time.sleep(5)

	

#     # Tweet a random quote
api.update_status(happy_quotes)

#     # Print success message
#     # YOUR CODE HERE
#     raise NotImplementedError()

# # Set timer to run every minute
# # YOUR CODE HERE
# raise NotImplementedError()
