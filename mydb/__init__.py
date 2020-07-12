import myconfig
from flask_pymongo import pymongo

client = pymongo.MongoClient(myconfig.MONGO_URL)
db = client[myconfig.MONGO_DB]
collection = db[myconfig.MONGO_COLLECTION]
