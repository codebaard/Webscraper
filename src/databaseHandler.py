from pymongo import MongoClient
import os

class databaseHandler(object):
    """This class handles the mongo stuff"""

    def __init__(self):
        self.connectionString = os.getenv('MONGO_CONNECTION')
        self.client = MongoClient(self.connectionString)
        self.db = self.client.pr0gramm