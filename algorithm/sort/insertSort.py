#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest


def sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break
    return arr


def sort2(arr):
    for i in range(1, len(arr)):
        j, check = i - 1, arr[i]
        while j >= 0 and arr[j] > check:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = check
    return arr


class TestSort(unittest.TestCase):
    def setUp(self):
        self.arr = [3, 5, 9, 8, 4, 2, 1, 0, -6, 12, -8]
        self.result = [-8, -6, 0, 1, 2, 3, 4, 5, 8, 9, 12]

    def test_insert(self):
        self.assertEqual(sort(self.arr), self.result)
        self.assertEqual(sort2(self.arr), self.result)


if __name__ == '__main__':
    unittest.main()
