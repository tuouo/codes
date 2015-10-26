#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def quickSort(arr):
    #return quickSort1(arr, 0, len(arr) - 1)
    return quickSort0(arr, 0, len(arr) - 1)

def quickSort0(arr, l, r):
    sLen = r - l
    if sLen < 0:
        return
    if sLen < 4:				# not real len 
        for low in range(1, sLen):
            for high in range(low + l, l, -1):
                if arr[high - 1] > arr[high]:
                    arr[high - 1], arr[high] = arr[high], arr[high - 1]
                else:
                    break
        return arr

    mid = l + ((r - l) >> 1)
    if arr[mid] > arr[r]:
        arr[mid], arr[r] = arr[r], arr[mid]
    if arr[l] > arr[r]:
        arr[l], arr[r] = arr[r], arr[l]
    if arr[mid] > arr[l]:
        arr[l], arr[mid] = arr[mid], arr[l]
    x = arr[l]

    low, high = l, r
    left, right = l, r	#value's(same  of x) position end
    while low < high:
        while low < high and arr[high] >= x:
            if arr[high] == x:
                arr[right], arr[high] = arr[high], arr[right]
                right -= 1
            high -= 1
        if low < high:
            arr[low] = arr[high]
            low += 1
        while low < high and arr[low] <= x:
            if arr[low] == x:
                arr[left], arr[high] = arr[high], arr[left]
                left += 1
            low += 1
        if low < high:
            arr[high] = arr[low]
            high -= 1
    arr[low] = x

    leftLen = left - l
    rightLen = r - right
    i, j = left, low - 1
    while i > l:
        arr[i], arr[j] = arr[j], arr[i]
        i -= 1
        j -= 1
    i, j = low + 1, right
    while j < r:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j += 1 

    quickSort1(arr, l, low - 1 - leftLen)
    quickSort1(arr, low + 1 + rightLen, r)
    return arr

def quickSort1(arr, l, r):
    if l > r:
        return
    x = arr[l]
    low, high = l, r
    while low < high:
        while low < high and arr[high] >= x:
            high -= 1
        if low < high:
            arr[low] = arr[high]
            low += 1
        while low < high and arr[low] <= x:
            low += 1
        if low < high:
            arr[high] = arr[low]
            high -= 1
    arr[low] = x
    quickSort1(arr, l, low - 1)
    quickSort1(arr, low + 1, r)
    return arr


# life is short, I wrote Python
def quickSort2(arr):
    if arr == []:
        return []
    x = arr[0]
    small = quickSort2([low for low in arr[1:] if low < x])
    big = quickSort2([low for low in arr[1:] if low >= x])
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