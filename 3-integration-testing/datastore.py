# jednostavan in-memory datastore
database = {}


def store_value(key, value):
    database[key] = value


def get_value(key):
    return database.get(key, None)


def delete_value(key):
    if key in database:
        del database[key]
        return True
    return False


def list_keys():
    return list(database.keys())