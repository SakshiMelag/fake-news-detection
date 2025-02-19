#from pymongo import MongoClient

# Connect to MongoDB Atlas (Replace with your actual MongoDB connection string)
#client = MongoClient("mongodb+srv://sakshimelag:7FTGWQ6j2hcRgjgg@cluster0.okioo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#db = client["newsDB"]
#collection = db["predictions"]

#def save_to_mongo(text, result):
 #   """Save prediction results to MongoDB."""
 #   collection.insert_one({"text": text, "prediction": result})
from pymongo import MongoClient

# Directly use the MongoDB connection string (replace with your actual credentials)
mongo_uri = "mongodb+srv://sakshimelag:7FTGWQ6j2hcRgjgg@cluster0.okioo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Establish the MongoDB connection
client = MongoClient(mongo_uri)
db = client["newsDB"]  # Use the correct database name
collection = db["predictions"]  # The collection where you'll store predictions

def save_to_mongo(text, result, model_type):
    """Save prediction results to MongoDB."""
    collection.insert_one({"text": text, "prediction": result, "model_used": model_type})
