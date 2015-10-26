#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def makeMinHeap(arr):  
    for i in range((len(arr) -1) >> 1, -1, -1):
        arr = fixMinHeapDown(arr, i)
    return arr

def fixMinHeapUp(arr):
    k = len(arr) - 1    
    p = (k - 1) >> 1
    while k > 0 and arr[p] > arr[k]:
        arr[p], arr[k] = arr[k], arr[p]
        k = p
        p = (k - 1) >> 1
    return arr

def insertHeap(arr, elem):
    arr.append(elem)
    return fixMinHeapUp(arr)

def fixMinHeapDown(arr, p = 0):
    aLen = len(arr)
    temp = arr[p]
    q = 2 * p + 1
    while q < aLen:
        if (q + 1) < aLen and arr[q + 1] < arr[q]:
            q += 1
        if arr[q] > temp:
            break
        arr[p] = arr[q]
        p = q
        q = 2 * p + 1
    arr[p] = temp
    return arr

def delHeapMin(arr):
    aLen = len(arr)
    if aLen < 2:
        return []
    elif aLen == 2:
        return [arr[1]]
    arr[0] = arr.pop()
    return fixMinHeapDown(arr)

def heapSort(arr):
    arr = makeMinHeap(arr)
    result = []
    for i in range(len(arr)):
        result.append(arr[0])
        arr = delHeapMin(arr)
    return result

def heapSort2(arr):
    temp = []
    for i in range(len(arr)):
        temp = insertHeap(temp, arr[i])
    result = []
    for i in range(len(temp)):
        result.append(temp[0])
        temp = delHeapMin(temp)
    return result

import unittest
class tHeapSort(unittest.TestCase):
    def setUp(self):
        self.arr = [3,5,9,8,4,2,1,0,-6,12,-8]
        self.result = [-8,-6,0,1,2,3,4,5,8,9,12]

    def test_heap(self):
        self.assertEqual(heapSort(self.arr), self.result)
    def test_heap2(self):
        self.assertEqual(heapSort2(self.arr), self.result)

if __name__ == '__main__':
    unittest.main()