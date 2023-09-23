from pymongo import MongoClient

import logging

def connect_db(uri : str):
    try:
        client = MongoClient(uri)
        db = client["p2p-betting-dev"]
    except TimeoutError:
        logging.error("Cannot connect to database, may be due to poor network connectivity")
        connect_db(uri=uri)
    else:
        return db