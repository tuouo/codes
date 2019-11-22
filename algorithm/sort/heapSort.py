#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest


def sort(arr):
    arr = make_min_heap(arr)
    result = []
    for i in range(len(arr)):
        result.append(arr[0])
        arr = del_heap_min(arr)
    return result


def sort2(arr):
    temp = []
    for i in range(len(arr)):
        temp = insert_heap(temp, arr[i])
    result = []
    for i in range(len(temp)):
        result.append(temp[0])
        temp = del_heap_min(temp)
    return result


def make_min_heap(arr):
    for i in range((len(arr) - 1) >> 1, -1, -1):
        arr = fix_min_heap_down(arr, i)
    return arr


def fix_min_heap_down(arr, p=0):
    temp = arr[p]
    q = 2 * p + 1
    while q < len(arr):
        if (q + 1) < len(arr) and arr[q + 1] < arr[q]:
            q += 1
        if arr[q] > temp:
            break
        arr[p] = arr[q]
        p = q
        q = 2 * p + 1
    arr[p] = temp
    return arr


def del_heap_min(arr):
    if len(arr) < 2:
        return []
    elif len(arr) == 2:
        return [arr[1]]
    arr[0] = arr.pop()
    return fix_min_heap_down(arr)


def insert_heap(arr, elem):
    arr.append(elem)
    return fix_min_heap_up(arr)


def fix_min_heap_up(arr):
    k = len(arr) - 1
    p = (k - 1) >> 1
    while k > 0 and arr[p] > arr[k]:
        arr[p], arr[k] = arr[k], arr[p]
        k = p
        p = (k - 1) >> 1
    return arr


class TestSort(unittest.TestCase):
    def setUp(self):
        self.arr = [3, 5, 9, 8, 4, 2, 1, 0, -6, 12, -8]
        self.result = [-8, -6, 0, 1, 2, 3, 4, 5, 8, 9, 12]

    def test_heap(self):
        self.assertEqual(sort(self.arr), self.result)

    def test_heap2(self):
        self.assertEqual(sort2(self.arr), self.result)


if __name__ == '__main__':
    unittest.main()
