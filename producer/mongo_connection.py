from pymongo import MongoClient
import os


def get_connection():
    mongo_uri = os.getenv("MONGO_URI","mongodb://localhost:27017")
    mongo_db = os.getenv("MONGO_DB_NAME","my_data")
    mongo_collection = os.getenv("MONGO_COLLECTION","data")
    client = MongoClient(mongo_uri)

    mongo_db = client[mongo_db]

    coll = mongo_db[mongo_collection]

    return coll



