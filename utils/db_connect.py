"""
    db_connect.py - This file is used to connect to the database and perform CRUD operations.

    Devs: [
        "INovomiast2" <idimnovdie1602@protonmail.com>
    ]
"""

import os
import json
from pymongo import MongoClient
from dotenv import load_dotenv
from schemas import user

# Load the environment variables
load_dotenv()

# Get the database URL
DB_URL = os.getenv("MONGO_URI")

# Connect to the database
def connectDB():
    try:
        client = MongoClient(DB_URL)
        db = client["web-db"]
        return db
    except Exception as e:
        return {
            "error": str(e)
        }
    
# Create a new collection
def createCollection(db, collection_name):
    try:
        collection = db[collection_name]
        return collection
    except Exception as e:
        return {
            "error": str(e)
        }
    
# Insert a new document
def insertDocument(collection, document):
    try:
        result = collection.insert_one(document)
        return result.inserted_id
    except Exception as e:
        return {
            "error": str(e)
        }

# Document Checker
"""
    This function is in charge of checking if the document format is correct.

    Params:
        @param document: The document to check.
        @type document: dict

        @param schema: The schema to check against.
        @type schema: dict
"""
def checkDocument(document, schema):
    for key in schema:
        if key not in document:
            return {"status": False, "key": f"Key '{key}' is missing."}
    return {"status": True, "document": document}

# TEST
if __name__ == "__main__":
    db = connectDB()
    collection = createCollection(db, "cli-user")
    document = {
        "username": "admin",
        "password": "admin"
    }
    insertDocument(collection, document)
    print("Document inserted.")
