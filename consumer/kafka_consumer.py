from confluent_kafka import Consumer
import os
import json
from mysql_connection import *

kafka_server = os.getenv("KAFKA_SERVER","localhost:29092")

consumer_config = {
    "bootstrap.servers": kafka_server,
    "group.id": "data-tracker",
    "auto.offset.reset": "earliest"}

consumer = Consumer(consumer_config)

consumer.subscribe(["data"])


try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("❌ Error:", msg.error())
            continue

        value = msg.value().decode("utf-8")
        data = json.loads(value)
        for doc in data:
            if doc["type"] == "customer":
                insert_data_to_customers_table(doc)
            else:
                insert_data_to_orders_table(doc)
except KeyboardInterrupt:
    print("\n🔴 Stopping consumer")

finally:
    consumer.close()
