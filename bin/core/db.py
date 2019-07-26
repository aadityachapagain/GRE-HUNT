import pymongo

db = pymongo.MongoClient()['gre']
vocab = db.vocab