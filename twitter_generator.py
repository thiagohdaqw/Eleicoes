from kafka import KafkaProducer
import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

TWITTER_BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')
KAFKA_SERVER = '0.0.0.0:9092'
MESSAGE_TOPIC = 'message'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)

def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.offset)

def on_send_error(excp):
    print('I am an error callback', exc_info=excp)

candidates = ['Lula', 'Bolsonaro', 'Simone Tebet', 'Ciro Gomes']

for candidate in candidates:
    # generate sentences based on candidate search
    tweets = client.search_recent_tweets(query=candidate, max_results=10)

    sentences = [tweet.text for tweet in tweets.data]

    # Send the sentence to kafka topic
    for sentence in sentences:
        producer.send(MESSAGE_TOPIC, sentence.encode()).add_callback(on_send_success).add_errback(on_send_error)
        producer.flush()