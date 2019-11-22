#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/4/10
import unittest


def primes(n=10000):  # 1229
    arr = [True] * n
    arr[0] = arr[1] = False
    arr[4:n:2] = [False] * ((n - 1) // 2 - 1)
    for i in range(3, int((n - 1) ** 0.5) + 1):
        if arr[i]:
            arr[i * i:n:2 * i] = [False] * ((n - 1 - i * i) // (2 * i) + 1)
    # arr = [i for i, p in enumerate(arr) if p]
    return arr


sieve_of_eratosthenes = primes


def primes_directly(n):
    arr = [True] * n
    arr[0] = arr[1] = False
    for i in range(2, int((n - 1) ** 0.5) + 1):
        if arr[i]:
            arr[i*i:n:i] = [False] * ((n - 1) // i - i + 1)
    return arr, sum(arr)


def primes_old(n):
    arr = [True if i % 2 and i % 3 else False for i in range(n)]
    arr[1], arr[2], arr[3] = False, True, True
    for i in range(5, int(n ** 0.5) + 1):
        if arr[i]:
            arr[i*i:n:i] = [False] * ((n - 1) // i - i + 1)
    return arr, arr.count(True)


class TestCase(unittest.TestCase):
    def setUp(self):
        self.primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    def tearDown(self):
        del self.primes

    def test_prime(self):
        self.assertEqual(self.primes, [i for i, j in enumerate(primes_directly(100)[0]) if j])
        self.assertEqual(len(self.primes), primes_directly(100)[1])

        self.assertEqual(self.primes, [i for i, j in enumerate(primes(100)) if j])


if __name__ == '__main__':
    unittest.main()
