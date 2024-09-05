from confluent_kafka.avro import AvroProducer
from confluent_kafka.avro.serializer import SerializerError
from confluent_kafka import avro
from pymongo import MongoClient

# Kafka Schema Registry configuration
producer_config = {
    'bootstrap.servers': 'localhost:9092',
    'schema.registry.url': 'http://localhost:8081'
}

value_schema = avro.load('user_update.avsc')
def produce_user_update(user_data):

    print("Avro Schema - ", value_schema)

    producer = AvroProducer(producer_config, default_value_schema=value_schema)

    topic = 'user_updates'

    try:
        producer.produce(topic=topic, value=user_data)
        producer.flush()
    except SerializerError as e:
        print(f"Message serialization failed: {e}")
#
# # Example of user data update
# new_user_data = {
#     "user_id": "123",
#     "name": "John Doe",
#     "email": "john_updated@example.com",
#     "age": 31
# }
# produce_user_update(new_user_data)
