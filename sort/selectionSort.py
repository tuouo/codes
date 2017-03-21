#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest


def sort(arr):
    for i in range(len(arr) - 1):
        mini = min(arr[i + 1:])
        if arr[i] > mini:
            j = arr.index(mini, i + 1)
            arr[i], arr[j] = arr[j], arr[i]
    return arr


def sort2(arr):
    for i in range(len(arr) - 1):
        min_pos = i
        for j in range(i + 1, len(arr)):
            if arr[min_pos] > arr[j]:
                min_pos = j
        arr[i], arr[min_pos] = arr[min_pos], arr[i]
    return arr


class TestSort(unittest.TestCase):
    def setUp(self):
        self.arr = [3, 5, 9, 8, 4, 2, 1, 0, -6, 12, -8]
        self.result = [-8, -6, 0, 1, 2, 3, 4, 5, 8, 9, 12]

    def test_select(self):
        self.assertEqual(sort(self.arr), self.result)

    def test_select2(self):
        self.assertEqual(sort2(self.arr), self.result)


if __name__ == '__main__':
    unittest.main()
