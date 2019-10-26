#pip install google-cloud-datastore
from google.cloud import datastore
from config import *

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS


datastore_client = datastore.Client()

def createUser(userObj):
    kind = "User"
    id = userObj["id"]
    user_key = datastore_client.key(kind, id)

    user = datastore.Entity(key=user_key)
    user.update(userObj)
    datastore_client.put(user)
    result = datastore_client.get(user_key)
    print(result)
    print("registered user " + str(id))

def getUser(id):
    query = datastore_client.query(kind='User')
    query.add_filter("id", "=", id)
    users = query.fetch(limit=10)
    for u in users:
        print(u)

def getUserById(id):
    user_key = datastore_client.key("User", id)
    print(datastore_client.get(user_key))

def getUsers():
    query = datastore_client.query(kind='User')
    users = query.fetch(limit=100)
    user = users.filter("id =", )
    for u in users:
        print(u)