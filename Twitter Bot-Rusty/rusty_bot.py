import tweepy
import textblob
import re
import time

from keys import *
from textblob import TextBlob

# NOTE: Put your access keys and consumer keys in seperate file to acccess them

print('Twitter Bot intiated:')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_replied_tweet_id.txt'

def retrieve_last_replied_id(file_name):
    f_read = open(file_name, 'r')
    last_replied_id = int(f_read.read().strip())
    f_read.close()
    return last_replied_id

def store_last_replied_id(last_replied_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_replied_id))
    f_write.close()
    return

# Removing special characters and spaces to generate only meaningful words using regex
def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())

def get_tweet_sentiment(tweet):

# create TextBlob object of passed tweet text
    analysis = TextBlob(clean_tweet(tweet))
# set sentiment
    return analysis.sentiment.polarity

def reply_to_tweets():
    print('retrieving and replying to tweets...')

    last_replied_id = retrieve_last_replied_id(FILE_NAME)

    # NOTE: We need to use tweet_mode='extended' to preserve long tweets
    mentions = api.mentions_timeline(last_replied_id,tweet_mode='extended')

    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_replied_id = mention.id

        store_last_replied_id(last_replied_id, FILE_NAME)
        
        # Analyzing the sentiment of the mention as positive or negative
        tweet_sentiment= get_tweet_sentiment(mention.full_text.lower())
           
        # analyzing words that greet you and then replying back accordingly
        if 'hello' in mention.full_text.lower():
            api.update_status('@' + mention.user.screen_name +'#Hello', mention.id)

        elif 'hi' in mention.full_text.lower():
            api.update_status('@' + mention.user.screen_name +'#Hi', mention.id)

        elif 'hey' in mention.full_text.lower():
            api.update_status('@' + mention.user.screen_name +'#Hey', mention.id)
        
        # sentiment is negative for less than 0, positive for greater than 0 and neutral for equal to 0
        elif tweet_sentiment < 0 :
            api.update_status('@' + mention.user.screen_name +'#I am Sorry !', mention.id)

        elif tweet_sentiment > 0 :
            api.update_status('@' + mention.user.screen_name +'#Thank You !', mention.id)

        elif tweet_sentiment == 0 :
            api.update_status('@' + mention.user.screen_name +'#Alright !', mention.id)



while True:
    reply_to_tweets()
    time.sleep(15) # reinitiating the script after every 15 seconds
