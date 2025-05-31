from pymongo import MongoClient
from datetime import datetime
import time

uri = 'mongodb://localhost:27017'
db_name = 'emotions_db'
collection_name = 'emotions_test'

def connect_to_db():
    client = MongoClient(uri)
    return client[db_name][collection_name]

collection = connect_to_db()

def store(user_id, emotion):
    time.sleep(0.001)
    timestamp = datetime.now()

    emotion_data = {
        'user_id': user_id,
        'emotion': emotion,
        'timestamp': timestamp
    }

    collection.insert_one(emotion_data)
    return 'Emotion stored successfully.'



def retrieve(user_id, limit):
    query = {'user_id': user_id}
    sort = [('timestamp', -1)]
    emotions = collection.find(query).sort(sort).limit(limit)
    emotion_values = [emotion['emotion'] for emotion in emotions]
    emotion_values.reverse()
    return emotion_values

