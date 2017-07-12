def add_numbers(a, b):
    '''Add two numbers

    :param a:
    :param b:
    :returns: sum of the numbers
    '''
    return a + b


def multiply(a, b):
    return a * b


def average(*numbers):
    return sum(numbers) / len(numbers)


def average2(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)
