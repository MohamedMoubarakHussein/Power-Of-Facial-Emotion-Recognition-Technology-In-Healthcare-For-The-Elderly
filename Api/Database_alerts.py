from pymongo import MongoClient
from datetime import datetime

import time

uri = 'mongodb://localhost:27017'
db_name = 'alerts'
collection_name = 'alert'

def connectToDB():
    client = MongoClient(uri)
    return client[db_name][collection_name]

collection = connectToDB()

def save(user , message):
    alert = {
        'user': user,
        'message': message
    }

    collection.insert_one(alert)
    
def getAlerts(PatientName):
    ls = []
    doc = collection.find({"user":PatientName})
    for document in doc:
        ls.append(document['message'])
    remove(PatientName)
    
    return ls


def remove(usr):
    doc ={'user': usr}
    collection.delete_many(doc)
