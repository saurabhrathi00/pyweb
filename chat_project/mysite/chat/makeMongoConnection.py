from pymongo import *
from random import randint


client = MongoClient(port=27017)

def useDatabase(db_name):
    return client[db_name]