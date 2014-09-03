from sys import argv, exit

BENCH_MAX = 6553600


def benchmark(benchmark_maximum, prime_func):
    for i in xrange(benchmark_maximum):
        prime_func(i)


def main(prime_func):
    if len(argv) >= 2:
        if argv[1] == '-b':
            benchmark_maximum = int(argv[2]) if len(argv) >= 3 else BENCH_MAX
            benchmark(benchmark_maximum, prime_func)
        else:
            num_to_check = int(argv[1])

            if prime_func(num_to_check):
                print "{} is prime.".format(num_to_check)
            else:
                print "{} is not prime.".format(num_to_check)

        exit(0)

    print "Usage: {} (-b to benchmark|<num to test primalness of>)".format(argv[0])

    exit(1)
