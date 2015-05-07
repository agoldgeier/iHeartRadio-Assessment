# Mongo boilerplate
from pymongo import MongoClient
client = MongoClient('localhost', 27017)

db = client.iHeartAssessment

artists = db.artists
listens = db.listens
users = db.users

# 1. Find total number of users
print(users.count())

# 2. Find total number of active users
print(len(listens.distinct("profile_id")))