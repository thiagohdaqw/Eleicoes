from kafka import KafkaProducer
import tweepy
import os
import time
from dotenv import load_dotenv

load_dotenv()

TWITTER_BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')
TWITTER_INTERVAL_SECONDS = os.getenv('TWITTER_INTERVAL_SECONDS', 60)
KAFKA_SERVER = os.getenv("KAFKA_SERVER", '0.0.0.0:9092')
WORDS_TOPIC = os.getenv("WORDS_TOPIC", "wc")

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)

def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.offset)

def on_send_error(excp):
    print('I am an error callback', exc_info=excp)

candidates = ['Lula', 'Bolsonaro', 'Simone Tebet', 'Ciro Gomes']

while True:
    # send to candidate topic
    for candidate in candidates:
        tweets = client.search_recent_tweets(query=candidate, max_results=10)

        sentences = [tweet.text for tweet in tweets.data]

        for sentence in sentences:
            phrase = f'${candidate},${sentence}'
            producer.send(WORDS_TOPIC, phrase.encode()).add_callback(on_send_success).add_errback(on_send_error)
            producer.flush()

    print(f"Sleeping for {TWITTER_INTERVAL_SECONDS} seconds")
    time.sleep(TWITTER_INTERVAL_SECONDS)
