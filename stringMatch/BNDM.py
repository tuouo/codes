#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def pre(tarStr):
    p = {}
    slen = len(tarStr)
    shirt = 1 << (slen - 1)
    for i in range(slen):
        if tarStr[i] in p:
            p[tarStr[i]] |= shirt
        else:
            p[tarStr[i]] = shirt
        shirt >>= 1
    return p

def bndm(findStr, tarStr, start = 0):
    slen = len(tarStr) 
    mask = 1 << (slen - 1)
    p = pre(tarStr)
    i = start
    end = len(findStr) - len(tarStr) + 1
    while(i < end):
        move = slen
        l = slen - 1
        d = -1 & p[findStr[i + l]]
        while(d != 0):
            if d == mask:
                if l == 0:
                    return i - start
                else:
                    move = l
                    break;
            l -= 1
            d = (d << 1) & p[findStr[i + l]]
        i += move
    return -1

import unittest
class bndmTest(unittest.TestCase):
    def test_so(self):
        self.assertEqual(bndm('aababacb', 'ababacb', start = 1), 0)
    def test_so2(self):
        self.assertEqual(bndm('aababacb', 'acb'), 5)

if __name__ == '__main__':
    unittest.main()