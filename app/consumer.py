from confluent_kafka.avro import AvroConsumer
from pymongo import MongoClient

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client['user_db']
users_collection = db['users']

consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'user_updates_group',
    'schema.registry.url': 'http://localhost:8081',
    'auto.offset.reset': 'earliest'
}

consumer = AvroConsumer(consumer_config)
consumer.subscribe(['user_updates'])

def consume_user_updates():
    while True:
        try:
            msg = consumer.poll(10)
            print("Message in Consumer - ", msg)
            if msg is None:
                continue
            user_data = msg.value()

            # Update MongoDB with user data
            users_collection.update_one(
                {'user_id': user_data['user_id']},
                {'$set': user_data},
                upsert=True
            )
            print(f"User {user_data['user_id']} updated.")
        except Exception as e:
            print(f"Failed to consume message: {e}")

consume_user_updates()
