#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def pre(tarStr):
    p = {}
    shirt = 1
    for i in range(len(tarStr)):
        if tarStr[i] in p:
            p[tarStr[i]] |= shirt
        else:
            p[tarStr[i]] = shirt
        shirt <<= 1
    return p

def shift_and(findStr, tarStr, start = 0):
    mask = 1 << (len(tarStr) - 1)
    p = pre(tarStr)
    d = 0
    for i in range(start, len(findStr)):
        d = (d << 1 | 1) & p[findStr[i]]
        if d & mask: return i + 1 - len(tarStr) - start
    return -1

import unittest
class saTest(unittest.TestCase):
    def test_sa(self):
        self.assertEqual(shift_and('aababacb', 'ababac', start = 1), 0)
    def test_sa2(self):
        self.assertEqual(shift_and('aababacb', 'acb'), 5)

if __name__ == '__main__':
    unittest.main()