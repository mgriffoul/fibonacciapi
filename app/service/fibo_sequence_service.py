from app.bdd.dao import get_fibonacci_number, get_last_two_documents, insert_fibonacci_number, find_low_boundaries, \
    find_high_boundary
from app.utils.logger_factory import create_logger

logger = create_logger()


def fetch_closer(number):
    # le nombre est dans la suite et est en bdd
    if get_fibonacci_number(number) is not None:
        return number
    # le nombre n'est pas dans la suite, les nombres de la suite les plus proches sont en bdd
    low_boundary = find_low_boundaries(number)
    high_boundary = find_high_boundary(number)
    if low_boundary is not None and high_boundary is not None:
        return calculate_closer(number, [low_boundary, high_boundary])
    # le nombre est peut être dans la suite, mais la suite stockée n'est pas assez étendue
    previous = get_last_two_documents()
    logger.info('Fibonacci sequence enrichment starting')
    new_sequence = enrich_sequence(number, [previous[0]['value'], previous[1]['value']])
    logger.info('New sequence is : ' + str(new_sequence) + ' and number is = ' + str(number))
    if number in new_sequence:
        logger.info('Request number found in new calculated sequence' + str(new_sequence))
        return number
    logger.info('Request number is not in fibonacci sequence, calculating closer starting')
    return calculate_closer(number, new_sequence[-2:])


def enrich_sequence(number, previous):
    x = previous[-2]
    y = previous[-1]
    previous.append(x + y)
    insert_fibonacci_number(x + y)
    if x + y == number or x + y > number:
        return previous
    return enrich_sequence(number, previous)


def calculate_closer(number, previous):
    x = previous[-2]
    y = previous[-1]
    if number - x > y - number:
        return y
    return x
