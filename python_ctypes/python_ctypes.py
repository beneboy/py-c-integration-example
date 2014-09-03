#!/usr/bin/env python
from sys import path
path.append('..')
from ctypes import CDLL
from pythonlib.wrappers import main


if __name__ == '__main__':
    lib = CDLL('../lib/libcon_math.so')
    main(lib.isPrimeNaive)
