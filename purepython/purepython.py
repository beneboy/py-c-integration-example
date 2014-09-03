#!/usr/bin/env python
from sys import path
path.append('..')
from pythonlib.con_math import is_prime_naive
from pythonlib.wrappers import main


if __name__ == '__main__':
    main(is_prime_naive)
