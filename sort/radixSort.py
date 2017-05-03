#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/3/21
import math
import unittest


def sort(arr, radix=10):
    """
    :param arr: all item should >0
    :param radix: <=10
    :return:
    """
    digit = int(math.ceil(math.log(max(arr), radix)))
    for i in range(1, digit+1):
        bucket = [[] for _ in range(radix)]
        for item in arr:
            bucket[item % (radix**i) // (radix**(i-1))].append(item)
        del arr[:]
        for each in bucket:
            arr.extend(each)
    return arr


def sort2(arr, radix=10):
    digit = int(math.ceil(math.log(max(arr), radix)))
    bucket = [[] for _ in range(radix)]
    for i in range(1, digit+1):
        for item in arr:
            bucket[item % (radix**i) // (radix**(i-1))].append(item)
        del arr[:]
        for each in bucket:
            arr.extend(each)
            del each[:]
    return arr


class TestSort(unittest.TestCase):
    def setUp(self):
        self.arr = [3, 5, 9, 8, 4, 2, 1, 0, 12]
        self.result = [0, 1, 2, 3, 4, 5, 8, 9, 12]

    def test_sort(self):
        self.assertEqual(sort(self.arr), self.result)
        self.assertEqual(sort2(self.arr), self.result)


if __name__ == '__main__':
    unittest.main()
