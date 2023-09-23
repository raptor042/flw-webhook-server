import logging

def get_user(db, query : dict) -> dict:
    try:
        user = db.collection["users"].find_one(query)
    except TimeoutError:
        logging.error("Cannot get user data to database, may be due to poor network connectivity")
    else:
        return user

def set_user(db, value : dict) -> dict:
    try:
        user = db.collection["users"].insert_one(value)
    except TimeoutError:
        logging.error("Cannot post user data to database, may be due to poor network connectivity")
    else:
        return user

def update_user(db, query: dict, value: dict) -> dict:
    try:
        user = db.collection["users"].update_one(query, value)
    except TimeoutError:
        logging.error("Cannot update user data to database, may be due to poor network connectivity")
    else:
        return user
    
def delete_user(db, query: dict) -> dict:
    try:
        user = db.collection["users"].delete_one(query)
    except TimeoutError:
        logging.error("Cannot delete user data to database, may be due to poor network connectivity")
    else:
        return user