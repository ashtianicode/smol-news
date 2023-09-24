```python
import socket
import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from config import CONFIG

# Twitter API credentials
consumer_key = CONFIG['TWITTER_CONSUMER_KEY']
consumer_secret = CONFIG['TWITTER_CONSUMER_SECRET']
access_token = CONFIG['TWITTER_ACCESS_TOKEN']
access_token_secret = CONFIG['TWITTER_ACCESS_TOKEN_SECRET']

class TweetListener(StreamListener):
    def __init__(self, socket):
        self.client_socket = socket

    def on_data(self, data):
        try:
            msg = json.loads(data)
            print(msg['text'].encode('utf-8')) 
            self.client_socket.send(msg['text'].encode('utf-8')) 
            return True
        except BaseException as e:
            print("Error: " + str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

def sendData(c_socket):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    twitter_stream = Stream(auth, TweetListener(c_socket))
    twitter_stream.filter(track=['stock'])

def stream_tweets():
    s = socket.socket() 
    host = "localhost" 
    port = 5555 
    s.bind((host, port)) 

    print("Listening on port: %s" % str(port))

    s.listen(5) 
    c, addr = s.accept() 

    print("Received request from: " + str(addr))

    sendData(c)
```
