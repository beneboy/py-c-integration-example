#!/usr/bin/env python
import unittest
from con_math import prime_test_max, is_prime_naive


class TestPrimeFunctions(unittest.TestCase):
    def test_test_max(self):
        self.assertEqual(prime_test_max(2), 2)
        self.assertEqual(prime_test_max(5), 3)
        self.assertEqual(prime_test_max(25), 5)
        self.assertEqual(prime_test_max(62), 8)
        self.assertEqual(prime_test_max(4294967295), 65536)

    def test_is_prime_naive(self):
        self.assertFalse(is_prime_naive(1))
        self.assertTrue(is_prime_naive(2))
        self.assertTrue(is_prime_naive(3))
        self.assertFalse(is_prime_naive(4))
        self.assertTrue(is_prime_naive(5))
        self.assertFalse(is_prime_naive(6))
        self.assertTrue(is_prime_naive(7))
        self.assertFalse(is_prime_naive(8))
        self.assertFalse(is_prime_naive(9))
        self.assertFalse(is_prime_naive(10))
        self.assertTrue(is_prime_naive(11))
        self.assertFalse(is_prime_naive(12))
        self.assertTrue(is_prime_naive(73))
        self.assertTrue(is_prime_naive(3571))
        self.assertTrue(is_prime_naive(93563))  # a centered heptagonal prime
        self.assertTrue(is_prime_naive(27644437))  # a bell number prime


if __name__ == '__main__':
    unittest.main()
