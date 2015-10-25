#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def bubbleSort(arr):
    aLen = len(arr)
    for i in range(aLen):
        for j in range(aLen - 1, i, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]            
    return arr

import unittest
class tBubbleSort(unittest.TestCase):
    def setUp(self):
        self.arr = [3,5,9,8,4,2,1,0,-6,12,-8]
        self.result = [-8,-6,0,1,2,3,4,5,8,9,12]

    def test_bubble(self):
        self.assertEqual(bubbleSort(self.arr), self.result)

if __name__ == '__main__':
    unittest.main()