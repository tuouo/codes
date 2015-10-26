#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def preprocess(tarStr):
	# get next offset to compare
    sLen = len(tarStr)
    p = [0] * sLen
    j = 0
    for i in range(1, sLen):
        while j > 0  and  tarStr[j] != tarStr[i]:
            j = p[j - 1]
        if tarStr[j] == tarStr[i]:
            j += 1
        p[i] = j
    return p

def kmp(findStr, tarStr, start = 0):
	# only return first begin index
    pre = preprocess(tarStr)
    tLen = len(tarStr)
    p = 0
    for i in range(start, len(findStr)):
        while p > 0 and tarStr[p] != findStr[i]:
            p = pre[p - 1]
        if tarStr[p] == findStr[i]:
            p += 1
        if p == tLen:
            return i - tLen + 1 - start
    return -1

import unittest
class kmpTest(unittest.TestCase):
    def test_pre(self):
        self.assertEqual(preprocess('ababacb'), [0,0,1,2,3,0,0])
    def test_kmp(self):
        self.assertEqual(kmp('aababacb', 'ababac', start = 1), 0)
    def test_kmp2(self):
        self.assertEqual(kmp('aababacb', 'acb'), 5)

if __name__ == '__main__':
    unittest.main()