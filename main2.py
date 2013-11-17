from twitter import *

stream = TwitterStream(auth=UserPassAuth('TwDuke_hackduke', 'mushrooms'))
auth = OAuth(
	consumer_key='kK38G4kaJ96PjsTVeLydA',
	consumer_secret='yLFu9sgN7Bw0e3QWuXzHzOts9zkPaojmRRVDnNE8vhY',
	token='2198562481-VUI1bP2GtTz2sZzNPkKG3FJSGNsuIqH3u6mRjW0',
	token_secret='v3Rb6arFYVYOklIlnajhQNHZONP2uZOxdA2BPXvh5Ttjz'
	)

# Iterate over the sample stream.
tweet_iter = stream.statuses.sample()
for tweet in tweet_iter:
# You must test that your tweet has text. It might be a delete
# or data message.
	if tweet.get('text'):
        	printNicely(tweet['text'])