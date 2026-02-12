from kafka import KafkaProducer
import os
import json
from mongo_connection import get_connection



coll = get_connection()


kafka_server = os.getenv("KAFKA_SERVER","localhost:29092")

producer = KafkaProducer(bootstrap_servers=kafka_server,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

documents = coll.find()
len_data = len(documents.to_list())

skip = 0
limit = 50
while skip < len_data:
    documents = coll.find({},{"_id":0}).limit(limit).skip(skip)
    skip += limit
    for doc in documents:
        producer.send("all_data",value=doc)

producer.flush()
