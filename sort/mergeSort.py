#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest


def sort(arr):
    len_a = len(arr)
    if len_a < 2:
        return arr
    elif len_a <= 4:
        for i in range(1, len_a):
            for j in range(i, 0, -1):
                if arr[j - 1] > arr[j]:
                    arr[j - 1], arr[j] = arr[j], arr[j - 1]
                else:
                    break
        return arr
    mid = len_a // 2
    left = sort(arr[:mid])
    right = sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


class TestSort(unittest.TestCase):
    def setUp(self):
        self.arr = [3, 5, 9, 8, 4, 2, 1, 0, -6, 12, -8]
        self.result = [-8, -6, 0, 1, 2, 3, 4, 5, 8, 9, 12]

    def test_merge(self):
        self.assertEqual(sort(self.arr), self.result)


if __name__ == '__main__':
    unittest.main()
