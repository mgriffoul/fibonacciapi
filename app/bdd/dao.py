from tinydb import TinyDB, Query

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
    dict1 = db.all()[db_len - 2]
    dict2 = db.all()[db_len - 1]
    return [dict1, dict2]


def persist_fibonacci_number(number):
    db.insert({'value': number})


def find_inferior_fibonacci_number(number):
    inferior_query = Query()
    results = db.search(inferior_query.value < number)
    number_results = []
    for dict_result in results:
        number_results.append(dict_result['value'])
    if not number_results:
        return None
    return max(number_results)


def find_superior_fibonacci_number(number):
    superior_query = Query()
    results = db.search(superior_query.value > number)
    number_results = []
    for dict_result in results:
        number_results.append(dict_result['value'])
    if not number_results:
        return None
    return min(number_results)
