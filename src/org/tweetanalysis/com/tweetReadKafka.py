from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaClient
from kafka import KafkaProducer
import tweetUtilites as TU

class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.send_messages("trump", data.encode('utf-8'))
        print (data)
        return True
    def on_error(self, status):
        print (status)

api=TU.readinifile("twitter")
kafka = KafkaClient("localhost:9092")
producer = KafkaProducer(kafka)
l = StdOutListener()
auth = TU.get_tweets(api)
stream = Stream(auth, l)
stream.filter(track="trump")