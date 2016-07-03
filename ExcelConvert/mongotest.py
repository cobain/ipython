__author__ = 'htzheng'

# coding:utf-8
import pymongo
import datetime

connection = pymongo.Connection('localhost', 27017)
print connection
db = connection.test_database
collection = db.test_collection
print collection

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}
posts = db.posts
print posts.insert(post)
print db.collection_names()

print posts.find_one()
print posts.find_one({"author": "Mike"})
print posts.count()

for post in posts.find():
    print post