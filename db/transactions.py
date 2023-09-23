import logging

def get_transaction(db, query : dict) -> dict:
    try:
        transaction = db.collection["transactions"].find_one(query)
    except TimeoutError:
        logging.error("Cannot get transaction data to database, may be due to poor network connectivity")
    else:
        return transaction

def set_transaction(db, value : dict) -> dict:
    try:
        transaction = db.collection["transactions"].insert_one(value)
    except TimeoutError:
        logging.error("Cannot post transaction data to database, may be due to poor network connectivity")
    else:
        return transaction

def update_transaction(db, query: dict, value: dict) -> dict:
    try:
        transaction = db.collection["transactions"].update_one(query, value)
    except TimeoutError:
        logging.error("Cannot update transaction data to database, may be due to poor network connectivity")
    else:
        return transaction
    
def delete_transaction(db, query: dict) -> dict:
    try:
        transaction = db.collection["transactions"].delete_one(query)
    except TimeoutError:
        logging.error("Cannot delete transaction data to database, may be due to poor network connectivity")
    else:
        return transaction