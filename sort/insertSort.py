#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def insertSort(arr):
    aLen = len(arr)
    for i in range(1, aLen):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break

import unittest
class tInsertSort(unittest.TestCase):
    arr = [3,5,9,8,4,2,1,0,-6,12,-8]
    result = [-6,-8,0,1,2,3,4,5,8,9,12]
    def tis(self):
        self.assertEqual(insertSort(arr), result)

if __name__ == '__main__':
    unittest.main()