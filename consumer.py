from kafka import KafkaConsumer
import os
from dotenv import load_dotenv

load_dotenv()

topic_name = "shop_testing"

consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=os.getenv("KAFKA_SERVER"),
    auto_offset_reset="latest",
    value_deserializer=bytes
    )

print("connected", consumer.bootstrap_connected())
print("Receiving data from", topic_name)

for message in consumer:
    email,food,date = message.value.decode('utf-8').split(",")
    print(f"{email} bought {food} on {date}")