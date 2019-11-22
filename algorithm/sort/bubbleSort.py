#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def sort(arr):
    len_a = len(arr)
    ok = 0
    while ok < len_a:
        start = ok
        ok = len_a
        for j in range(len_a - 1, start, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                ok = j
    return arr


def sort2(arr):
    len_a = len(arr)
    ok = len_a
    while ok > 0:
        start = ok
        ok = 0
        for j in range(1, start):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                ok = j
    return arr


class TestSort(unittest.TestCase):
    def setUp(self):
        self.arr = [3, 5, 9, 8, 4, 2, 1, 0, -6, 12, -8]
        self.result = [-8, -6, 0, 1, 2, 3, 4, 5, 8, 9, 12]

    def test_sort1(self):
        self.assertEqual(sort(self.arr), self.result)

    def test_sort2(self):
        self.assertEqual(sort2(self.arr), self.result)


if __name__ == '__main__':
    unittest.main()
