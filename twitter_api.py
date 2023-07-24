import tweepy
import pandas as pd

api_key = "" 
api_key_secret = ""
access_token = ""
access_token_secret = "" 

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

keywords = '@zomato'
limit=800

tweets = tweepy.Cursor(api.search_tweets, q=keywords, count=50, tweet_mode='extended').items(limit)
columns = ['User', 'Tweet','Time']
data = []

for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text,tweet.created_at])

df = pd.DataFrame(data, columns=columns)

df.to_csv('tweet.csv')


 
