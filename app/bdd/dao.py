from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage

from app.utils.logger_factory import create_logger

db = TinyDB('./app/bdd/fibonacci_sequence.json')
logger = create_logger()


def init_db():
    logger.info('Initializing data base')
    if len(db.all()) < 2:
        db.purge_tables()
        db.insert({'value': 0})
        db.insert({'value': 1})


def get_fibonacci_number(number):
    number_query = Query()
    result = db.get(number_query.value == number)
    if result is not None:
        logger.info('Request number found in database')
    return result


def get_last_two_documents():
    db_len = len(db)
    print('DB ALL ====================')
    print(db.all())
    dict1 = db.all()[db_len - 2]
    dict2 = db.all()[db_len - 1]
    logger.info('last two number in DB are : ' + str(dict1["value"]) + '  ' + str(dict2["value"]))
    return [dict1, dict2]


def insert_fibonacci_number(number):
    db.insert({'value': number})


def find_low_boundaries(number):
    boundary = Query()
    results = db.search(boundary.value < number)
    number_results = []
    for dict_result in results:
        number_results.append(dict_result['value'])
    if not number_results:
        return None
    return max(number_results)


def find_high_boundary(number):
    boundary = Query()
    results = db.search(boundary.value > number)
    number_results = []
    for dict_result in results:
        number_results.append(dict_result['value'])
    if not number_results:
        return None
    return min(number_results)
