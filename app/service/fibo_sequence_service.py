fibonaccisequence = []


def fetch_closer(number):
    if len(fibonaccisequence) < 2:
        fibonaccisequence.extend((0, 1))
    if number in fibonaccisequence:
        return number
    new_sequence = enrich_sequence(number, fibonaccisequence[-2:])
    if number in new_sequence:
        return number
    return calculate_closer(number, new_sequence[-2:])


def enrich_sequence(number, previous):
    x = previous[-2]
    y = previous[-1]
    previous.append(x + y)
    if x + y == number or x + y > number:
        return previous
    return enrich_sequence(number, previous)


def calculate_closer(number, previous):
    x = previous[-2]
    y = previous[-1]
    if number - x > y - number:
        return y
    return x
