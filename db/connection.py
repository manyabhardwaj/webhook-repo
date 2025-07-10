from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Connect to MongoDB
mongo_uri = os.getenv("MONGO_URI")
db_name = os.getenv("DB_NAME")
collection_name = os.getenv("COLLECTION_NAME")

client = MongoClient(mongo_uri)
db = client[db_name]
collection = db[collection_name]  # ✅ This is what we import in app.py
