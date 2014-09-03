#include "con_math.h"

unsigned int primeTestMax(const unsigned int number) {
    // returns the maximum value that should be tested when iterating of potential factors
    double root = sqrt((double)number);
    return (unsigned int)ceil(root);
}

bool isPrimeNaive(const unsigned int number) {
    // uses naive iterative method to test if a number is prime
    if (number == 1 || number % 2 == 0)
        return false;

    if (number == 2)
        return true;

    unsigned int testMax = primeTestMax(number), divisor;

    for(divisor = 3; divisor <= testMax; divisor += 2)
        if (number % divisor == 0)
            return false;

    return true;
}
