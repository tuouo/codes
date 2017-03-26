#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/3/26


def bin_search_left(arr, target, left, right):
    end = right
    while left <= right:
        mid = (right + left) // 2
        if target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    if left > end or arr[left] != target:
        return - left - 1
    return left


def bin_search_left1(arr, target, left, right):
    end = right
    while left <= right:
        mid = (right + left) >> 1
        if target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    if left > end or arr[left] != target:
        return - left - 1
    return left


def bin_search_left2(arr, target, left, right):
    end = right
    while left <= right:
        mid = left + ((right - left) >> 1)
        if target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    if left > end or arr[left] != target:
        return - left - 1
    return left


def bin_search_left3(arr, target, start, end):
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


def test_bin_search_left(arr, target):
    bin_search_left(arr, target, 0, len(arr))


def test_bin_search_left1(arr, target):
    bin_search_left1(arr, target, 0, len(arr))


def test_bin_search_left2(arr, target):
    bin_search_left2(arr, target, 0, len(arr))


def test_bin_search_left3(arr, target):
    bin_search_left3(arr, target, 0, len(arr))

if __name__ == '__main__':
    import timeit
    arguments = "[3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7], 5"
    name, methods, set_up = "test_bin_search_left", ["", "1", "2", "3"], "from __main__ import "
    for item in methods:
        print(item, "\t", timeit.timeit("{0}{1}({2})".format(name, item, arguments),
                                        setup="{0}{1}{2}".format(set_up, name, item)))
