#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Knuth-Morris-Pratt
"""
import unittest


def pre_process(pattern):
    # get next offset (k) to compare
    # target[0 ~ k-1] == target[j-k ~ j-1]
    j, p = 0, [0] * len(pattern)
    for i in range(1, len(pattern)):
        while j > 0 and pattern[j] != pattern[i]:
            j = p[j - 1]
        if pattern[j] == pattern[i]:
            j += 1
        p[i] = j
    return p


def kmp(text, pattern, start=0):
    # only return first target index
    pre = pre_process(pattern)
    p, len_tar = 0, len(pattern)
    for i in range(start, len(text)):
        while p > 0 and pattern[p] != text[i]:
            p = pre[p - 1]
        if pattern[p] == text[i]:
            p += 1
        if p == len_tar:
            return i - len_tar + 1 - start
    return -1


class KMPTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_pre(self):
        self.assertEqual(pre_process('ababacb'), [0, 0, 1, 2, 3, 0, 0])

    def test_kmp(self):
        self.assertEqual(kmp('aababacb', 'ababac', start=1), 0)

    def test_kmp2(self):
        self.assertEqual(kmp('aababacb', 'acb'), 5)


if __name__ == '__main__':
    unittest.main()
