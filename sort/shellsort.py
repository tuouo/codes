#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def shellSort(arr):
    aLen = len(arr)
    step = 0
    while step < aLen // 3:
        step = step * 3 + 1
    while step >= 1:
        for i in range(step, aLen):
            for j in range(i, 0, -step):
                if j >= step and arr[j - step] > arr[j]:
                    arr[j - step], arr[j] = arr[j], arr[j - step]
        step //= 3
    return arr

import unittest
class tShellSort(unittest.TestCase):
    def setUp(self):
        self.arr = [3,5,9,8,4,2,1,0,-6,12,-8]
        self.result = [-8,-6,0,1,2,3,4,5,8,9,12]

    def test_shell(self):
        self.assertEqual(shellSort(self.arr), self.result)

if __name__ == '__main__':
    unittest.main()