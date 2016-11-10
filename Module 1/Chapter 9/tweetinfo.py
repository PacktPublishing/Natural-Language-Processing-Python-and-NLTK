import json
import sys
tweets = json.loads(open(sys.argv[1]).read())
tweet_texts = [ tweet['text']\
                 for tweet in tweets ]

tweet_source = [tweet ['source'] for tweet in tweets]

tweet_geo = [tweet['geo'] for tweet in tweets]

tweet_locations = [tweet['place'] for tweet in tweets]

hashtags = [ hashtag['text'] for tweet in tweets for hashtag in
tweet['entities']['hashtags'] ]

print tweet_texts
print tweet_locations
print tweet_geo
print hashtags