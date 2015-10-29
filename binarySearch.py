#！/usr/bin/env/python3
# -*- coding: utf-8 -*-

def binarySearch(arr, target):
    return binSearchLeft(arr, target, 0, len(arr) - 1)

def binSearchLeft(arr, target, start, end):
    left, right = start - 1, end + 1
    while left + 1 != right:
        mid = left + ((right - left) >> 1)
        if target > arr[mid]:
            left = mid
        else:
            right = mid
    if right > end or arr[right] != target:
        return - right - 1
    return right

def binSearchRight(arr, target, start, end):
    left, right = start - 1, end + 1
    while left + 1 != right:
        mid = left + ((right - left) >> 1)
        if target < arr[mid]:
            right = mid
        else:
            left = mid
    if left < 0 or arr[left] != target:
        print("left, right:", left, right, )
        return - left - 2
    return left

import unittest
class tBinSearch(unittest.TestCase):
    def setUp(self):
        self.arr = [3,5,5,5,5,5,5,5,5,5,5,5,7]

    def test_insert(self):
        self.assertEqual(binarySearch(self.arr, 2), -1)
        self.assertEqual(binarySearch(self.arr, 3), 0)
        self.assertEqual(binarySearch(self.arr, 4), -2)
        #self.assertEqual(binarySearch(self.arr, 5), 1)
        self.assertEqual(binarySearch(self.arr, 5), 11)
        self.assertEqual(binarySearch(self.arr, 6), -13)
        self.assertEqual(binarySearch(self.arr, 7), 12)
        self.assertEqual(binarySearch(self.arr, 8), -14)

if __name__ == '__main__':
    unittest.main()