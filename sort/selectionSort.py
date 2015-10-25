#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def selectSort(arr):
    aLen = len(arr)
    for i in range(aLen - 1):
        mini = min(arr[i + 1:])
        if arr[i] > mini:
            j = arr.index(mini, i + 1)
            arr[i], arr[j] = arr[j], arr[i]
    return arr

import unittest
class tSelectSort(unittest.TestCase):
    def setUp(self):
        self.arr = [3,5,9,8,4,2,1,0,-6,12,-8]
        self.result = [-8,-6,0,1,2,3,4,5,8,9,12]

    def test_select(self):
        self.assertEqual(selectSort(self.arr), self.result)

if __name__ == '__main__':
    unittest.main()