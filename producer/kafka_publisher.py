from confluent_kafka import Producer
import os
import json
from mongo_connection import get_connection

coll = get_connection()

kafka_server = os.getenv("KAFKA_SERVER","localhost:9092")

producer_config = {"bootstrap.servers": kafka_server}

producer = Producer(producer_config)

def delivery_report(err, msg):
    if err:
        print(f"❌ Delivery failed: {err}")
    else:
        print(f"✅ Delivered {msg.value().decode("utf-8")}")
        print(f"✅ Delivered to {msg.topic()} : partition {msg.partition()} : at offset {msg.offset()}")

documents = coll.find()
len_data = len(documents.to_list())

skip = 0
limit = 50
while skip < len_data:
    documents = coll.find({},{"_id":0}).limit(limit).skip(skip)
    skip += limit
    for doc in documents:
        print(doc)
        value = json.dumps(doc).encode("utf-8")
        producer.produce(topic="data",value=value,callback=delivery_report)

    producer.flush()
