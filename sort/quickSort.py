#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest


def sort(arr):
    # return quickSort1(arr, 0, len(arr) - 1)
    return sort_optimize(arr, 0, len(arr) - 1)


def sort_optimize(arr, start, end):
    len_a = end - start
    if len_a < 2:
        return arr
    elif len_a < 4:  # deal with short arr
        for pos in range(1, len_a + 1):
            for high in range(start + pos, start, -1):
                if arr[high - 1] > arr[high]:
                    arr[high - 1], arr[high] = arr[high], arr[high - 1]
                else:
                    break
        return arr

    mid = start + ((end - start) >> 1)  # check a better sentry
    if arr[mid] > arr[end]:
        arr[mid], arr[end] = arr[end], arr[mid]
    if arr[start] > arr[end]:
        arr[start], arr[end] = arr[end], arr[start]
    if arr[mid] > arr[start]:
        arr[start], arr[mid] = arr[mid], arr[start]
    x = arr[start]

    low, left, right, high = start, start, end, end
    while low < high:
        while low < high and arr[high] >= x:
            if arr[high] == x:  # for same item
                arr[right], arr[high] = arr[high], arr[right]
                right -= 1
            high -= 1
        if low < high:
            arr[low] = arr[high]
            low += 1
        while low < high and arr[low] <= x:
            if arr[low] == x:  # for same item
                arr[left], arr[high] = arr[high], arr[left]
                left += 1
            low += 1
        if low < high:
            arr[high] = arr[low]
            high -= 1
    arr[low] = x

    len_left_same, len_right_same = left - start, end - right

    i, j = left, low - 1
    while i > start:  # move same item
        arr[i], arr[j] = arr[j], arr[i]
        i, j = i - 1, j - 1
    i, j = low + 1, right
    while j < end:
        arr[i], arr[j] = arr[j], arr[i]
        ii, j = i + 1, j + 1

    sort_optimize(arr, start, low - 1 - len_left_same)
    sort_optimize(arr, low + 1 + len_right_same, end)
    return arr


def sort_origin(arr, start, end):
    if start > end:
        return
    x = arr[start]
    low, high = start, end
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
    sort_origin(arr, start, low - 1)
    sort_origin(arr, low + 1, end)
    return arr


def sort_recursion(arr):
    if not arr:
        return arr
    x = arr[0]
    small = sort_recursion([low for low in arr[1:] if low < x])
    big = sort_recursion([low for low in arr[1:] if low >= x])
    return small + [x] + big


class TestSort(unittest.TestCase):
    def setUp(self):
        self.arr = [3, 5, 9, 8, 4, 2, 1, 0, -6, 12, -8]
        self.result = [-8, -6, 0, 1, 2, 3, 4, 5, 8, 9, 12]

    def test_quick(self):
        self.assertEqual(sort(self.arr), self.result)

    def test_quick2(self):
        self.assertEqual(sort_recursion(self.arr), self.result)


if __name__ == '__main__':
    unittest.main()
