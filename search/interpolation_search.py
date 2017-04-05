#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/4/5
"""
 data should be all sorted and uniform distribution, when read and compare cost much is better
 https://en.wikipedia.org/wiki/Interpolation_search
"""
import unittest


def search(arr, target):
    return interpolation_search(arr, target, 0, len(arr) - 1)


def interpolation_search(arr, target, low, high):
    while low <= high:
        # mid = (high + low) // 2
        mid = low + (high - low) * (target - arr[low]) // (arr[high] - arr[low])
        # print(low, mid, high)
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1


class SearchTestCase(unittest.TestCase):
    def setUp(self):
        self.arr = [i for i in range(9)]

    def tearDown(self):
        del self.arr

    def test_search(self):
        self.assertEqual(search(self.arr, 2), 2)
        self.assertEqual(search(self.arr, 8), 8)


if __name__ == '__main__':
    unittest.main()
