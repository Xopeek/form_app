from tinydb import TinyDB

db = TinyDB('db.json')


def save_template_to_db(fields):
    db.insert(fields)


def get_db_handle():
    return db
