from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys
consumer_key = 'ABCD012XXXXXXXXx'
consumer_secret = 'xyz123xxxxxxxxxxxxx'
access_token = '000000-ABCDXXXXXXXXXXX'
access_token_secret ='XXXXXXXXXgaw2KYz0VcqCO0F3U4'

class StdOutListener(StreamListener):

	def on_data(self, data):
		with open(sys.argv[1],'a') as tf:
			tf.write(data)
		return
    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['Apple watch'])