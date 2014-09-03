from math import ceil

def prime_test_max(number):
    return int(ceil(number ** 0.5))

def is_prime_naive(number):
    if number == 1:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    test_max = prime_test_max(number)

    for divisor in xrange(3, test_max + 1, 2):
        if number % divisor == 0:
            return False

    return True
