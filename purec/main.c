#include <stdio.h>
#include <con_math.h>
//#define BENCH_MAX 4294967295
#define BENCH_MAX 6553600

void benchmark(unsigned int benchmarkMaximum){
    unsigned int i;
    for(i = 0; i <= benchmarkMaximum; ++i)
        isPrimeNaive(i);
}

int main(const int argc, const char ** argv){
    if (argc >= 2) {
        if (strcmp(argv[1], "-b") == 0){
            unsigned int benchmarkMaximum;
            if (argc >= 3)
                benchmarkMaximum = (unsigned int)atoi(argv[2]);
            else
                benchmarkMaximum = BENCH_MAX;

            benchmark(benchmarkMaximum);
        } else {
            unsigned int numToCheck = (unsigned int)atoi(argv[1]);
            if (isPrimeNaive(numToCheck))
                printf("%u is prime.\n", numToCheck);
            else
                printf("%u is not prime.\n", numToCheck);
        }
        return 0;
    }

    printf("Usage: %s (-b to benchmark|<num to test primalness of>)\n", argv[0]);
    return 1;
}
