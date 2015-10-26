#!/usr/bin/env python3 
# -*- coding:utf-8 -*-
def BoyerMooreHorspool(findStr, tarStr, start = 0):
    sLen = len(findStr)
    tLen = len(tarStr)
    if tLen > sLen: return -1
    skip =  [tLen] * 256	# treat as ascII, not utf-8
    for i in range(tLen - 1): skip[ord(tarStr[i])] = tLen - i - 1
    #skip = tuple(skip)
    k = tLen - 1 + start
    while k < sLen:
        i = k
        j = tLen - 1;
        while j >= 0 and findStr[i] == tarStr[j]:
            j -= 1;
            i -= 1;
        if j == -1: return i + 1 - start
        k += skip[ord(findStr[k])]
    return -1


import unittest
class bmhTest(unittest.TestCase):
    def test_bmh(self):
        self.assertEqual(BoyerMooreHorspool('aababacb', 'ababac', start = 1), 0)
    def test_bmh2(self):
        self.assertEqual(BoyerMooreHorspool('aababacb', 'acb'), 5)

if __name__ == '__main__':
    unittest.main()