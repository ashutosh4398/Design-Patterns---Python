'''
    Approach 1 for implementing singleton pattern
'''

import logging

class Singleton:
    _shared = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._shared:
            cls._shared[cls] = super().__new__(cls)
        return cls._shared[cls]

class DBConnector(Singleton):
    
    status = "CLOSED"

    def __init__(self, name="", password="", port=""):
        if DBConnector.status == "CLOSED":
            print("CONNECTION INITIATED....")
            DBConnector.initate_connection()
    
    @property
    def db_status(self):
        return DBConnector.status
        
    @classmethod
    def initate_connection(cls):
        cls.status = "INITIATED"
    
    @classmethod
    def connect(cls):
        cls.status = "CONNECTED"
    
    @classmethod
    def disconnect(cls):
        cls.status = "CLOSED"

class Logger(Singleton):
    logger_instance = None

    def __init__(self):
        if self.logger_instance is None:
            Logger.__setup_config()
        print(self.logger_instance)

    @classmethod
    def __setup_config(cls):
        print("configuring logs....")
        cls.logger_instance = logging
        cls.logger_instance.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)
    
    def log(self, message):
        self.logger_instance.info(message)


logger = Logger()
print(logger)
logger.log("db program logging started...")

db = DBConnector(name="SQL", password="", port=4200)
print(db)
print(db.db_status)

db2 = DBConnector(name="SQL", password="", port=4200)
print(db2)
db2.connect()
print(db.db_status, db2.db_status)

db.disconnect()
print(db.db_status, db2.db_status)

new_inst = DBConnector(name="MONGO", password="", port=4300)
print(new_inst.db_status)

print(db.db_status, db2.db_status)


logger2 = Logger()
print(logger2)
logger2.log("db program logging stopped...")
