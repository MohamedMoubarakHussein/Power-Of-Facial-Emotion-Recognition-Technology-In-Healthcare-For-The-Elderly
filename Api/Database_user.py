from pymongo import MongoClient
from datetime import datetime
import time

uri = 'mongodb://localhost:27017'
db_name = 'auth'
collection_name = 'users'

def connect_to_db():
    client = MongoClient(uri)
    return client[db_name][collection_name]

collection = connect_to_db()

def signup(user , password , type , superVisorName):
    user = {
        'user': user,
        'password': password,
        'type': type,
        'superVisorName' : superVisorName
    }

    collection.insert_one(user)
    


def authPass(user , password):
    p = collection.find_one({ 'user': user })
    if p and p['password'] == password:
        return True
    else:
        return False
    
def authSupervisort(SuperVisor,PatientName):
    p = collection.find_one({ 'user': PatientName })
    if p and p['superVisorName'] == SuperVisor:
        return True
    else:
        return False
    
def getUsers(superVisorName):
    users = []
    for document in collection.find():
        if document['superVisorName'] == superVisorName:
            users.append(document['user'])
    return users

def getType(name):
    p = collection.find_one({ 'user': name })
    if p and p['type']:
        return p['type']
    
def checkSuperVisor(name):
    p = collection.find_one({ 'user': name })
    if p and p['type']:
        return p['type'] == 's'
    
def checkIfUserExist(name):
    p = collection.find_one({ 'user': name })
    if p and p['user'] == name:
        return True
    return False