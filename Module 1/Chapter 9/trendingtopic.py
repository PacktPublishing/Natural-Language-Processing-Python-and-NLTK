import nltk
from nltk import word_tokenize,sent_tokenize
from nltk import FreqDist
tweets_tokens = []
for tweet in tweet_text:
    tweets_tokens.append(word_tokenize(tweet))
Topic_distribution = nltk.FreqDist(tweets_tokens)
Freq_dist_nltk.plot(50, cumulative=False)

# Better trending topic 

import nltk
Topics = []
for tweet in tweet_text:
    tagged = nltk.pos_tag(word_tokenize(tweet))
    Topics_token = [word for word,pos in ] in tagged if pos in ['NN','NNP']
    print Topics_token