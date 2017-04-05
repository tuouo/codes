#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/4/5
import unittest


def search(arr, target):
    low, high, len_arr, k, fibs = 0, len(arr) - 1, len(arr), 0, list(fib(len(arr) - 1))
    while high > fibs[k]:
        k += 1
    tmp = arr + [arr[-1]] * (fibs[k] - high)
    while low <= high:
        mid = low + fibs[k-1]
        if tmp[mid] < target:
            low = mid + 1
            k -= 2
        elif tmp[mid] > target:
            high = mid - 1
            k -= 1
        else:
            return min(mid, len_arr - 1)
    return -1


def fib(n):
    return fib_search(n)


def fib_count(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def fib_num(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


def fib_search(n):
    a, b = 0, 1
    yield 0
    yield b - 1  # one num is used for check, so last remain b - 1
    while b <= n:
        a, b = b, a + b
        yield b - 1


class TestCase(unittest.TestCase):
    def setUp(self):
        self.arr = [i for i in range(13)]

    def tearDown(self):
        del self.arr

    def test_search(self):
        self.assertEqual(search(self.arr, -1), -1)
        self.assertEqual(search(self.arr, 0), 0)
        self.assertEqual(search(self.arr, 8), 8)
        self.assertEqual(search(self.arr, 12), 12)
        self.assertEqual(search(self.arr, 13), -1)


if __name__ == '__main__':
    unittest.main()
