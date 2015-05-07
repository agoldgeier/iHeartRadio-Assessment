# Mongo boilerplate
from pymongo import MongoClient
from bson.code import Code
import numpy as np

client = MongoClient('localhost', 27017)

db = client.iHeartAssessment

artists = db.artists
listens = db.listens
users = db.users

# 1. Average age of an active user
activeUsers = listens.distinct("profile_id")
numActiveUsers = len(activeUsers)

numActiveUsers = len(activeUsers)
cursor = db.users.aggregate([
		{ "$match": {"profile_id" : { "$in": activeUsers}}},
		{ "$group": {"_id": "active", "total": { "$sum": "$age"}}}
	])

print cursor.next()["total"]/numActiveUsers

# 2. Average age of inactive user
numInactiveUsers = users.count() - numActiveUsers
cursor = db.users.aggregate([
		{ "$match": {"profile_id" : { "$nin": activeUsers}}},
		{ "$group": {"_id": "inactive", "total": { "$sum": "$age"}}}
	])

print cursor.next()["total"]/numInactiveUsers

# 3. Compare standard deviations

# Active users
cursor = db.users.aggregate([
		{ "$match": {"profile_id" : { "$in": activeUsers}}},
		{ "$group": {"_id": "$age", "total": { "$sum": 1}}}
	])

x = np.array([])
for document in cursor:
	try:
		n = int(document["_id"])
		x = np.append(x, np.repeat(n, document["total"]))
	except ValueError:
		continue

activeUsersStd = np.std(x)
print activeUsersStd

# Inactive users
cursor = db.users.aggregate([
		{ "$match": {"profile_id" : { "$nin": activeUsers}}},
		{ "$group": {"_id": "$age", "total": { "$sum": 1}}}
	])

x = np.array([])
for document in cursor:
	try:
		n = int(document["_id"])
		x = np.append(x, np.repeat(n, document["total"]))
	except ValueError:
		continue

inactiveUsersStd = np.std(x)
print inactiveUsersStd