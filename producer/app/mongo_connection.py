from pymongo import MongoClient
import os


def get_connection():
    mongo_uri = os.getenv("MONGO_URI","mongodb://localhost:27017")

    client = MongoClient(mongo_uri)

    mongo_db = client["my_data"]

    coll = mongo_db["data"]

    
    return coll



