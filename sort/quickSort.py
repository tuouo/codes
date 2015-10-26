#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def quickSort(arr):
    return quickSort1(arr, 0, len(arr) - 1)

def quickSort1(arr, l, r):
    if l > r:
        return
    x = arr[l]
    i, j = l, r
    while i < j:
        while i < j and arr[j] >= x:
            j -= 1
        if i < j:
            arr[i] = arr[j]
            i += 1
        while i < j and arr[i] <= x:
            i += 1
        if i < j:
            arr[j] = arr[i]
            j -= 1
    arr[i] = x
    quickSort1(arr, l, i - 1)
    quickSort1(arr, i + 1, r)
    return arr


# life is short, I wrote Python
def quickSort2(arr):
    if arr == []:
        return []
    x = arr[0]
    small = quickSort2([i for i in arr[1:] if i < x])
    big = quickSort2([i for i in arr[1:] if i >= x])
    return small + [x] + big

import unittest
class tQuickSort(unittest.TestCase):
    def setUp(self):
        self.arr = [3,5,9,8,4,2,1,0,-6,12,-8]
        self.result = [-8,-6,0,1,2,3,4,5,8,9,12]

    def test_quick(self):
        self.assertEqual(quickSort(self.arr), self.result)
    def test_quick2(self):
        self.assertEqual(quickSort2(self.arr), self.result)

if __name__ == '__main__':
    unittest.main()