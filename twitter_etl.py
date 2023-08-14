import tweepy, pandas as pd, json, s3fs
from datetime import datetime
#import twitter

def run_twitter_etl():
	CONSUMER_KEY = 'QDSOD0qvG5AE7skDsega7HkeY'
	CONSUMER_SECRET = '9ybUtOloNk9C7m3OckSDj39r356ysT4W8Jbfsq9eY1WYFtfVKm'
	OAUTH_TOKEN = '1259453588524408834-4zQyoBtECTnYru2OjyjyuFWCx8FSod'
	OAUTH_TOKEN_SECRET = 'CJQkT8GTvdqCEEDNxWDTeTJGSlwVpBxEK8PNGDxKUDPnf'
	auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
	auth.set_access_token(OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
	api = tweepy.API(auth)
	tweets = api.user_timeline(screen_name = '@joebiden',
						   count = 1000,
						   include_rts = False, 
						   tweet_mode = 'extended')
	print(tweets)
	tweet_list = []
	for tweet in tweets:
		text = tweet._json["full_text"]
		tweet_data = {"user": tweet.user.screen_name,
					  "name": tweet.user.name,
					  #"description" : tweet.user.description,
					  'text': text,
					  'favourite_count': tweet.favorite_count,
					  #'statuses_count': tweet.statutes_count,
					  #'friends_count': tweet.friends_count,
					  'retweet_count': tweet.retweet_count,
					  'create_id': tweet.created_at}
		tweet_list.append(tweet_data)

	df = pd.DataFrame(tweet_list)
	df.to_csv('joebiden_twitter_data.csv')
run_twitter_etl()